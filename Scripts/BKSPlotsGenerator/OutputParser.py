import os
import shutil
import argparse
import subprocess
import tempfile
import sys
import csv

# Parse blocks separated by lines of dashes

def parse_blocks(lines):
    blocks = []
    current = []
    for line in lines:
        if line.startswith('----'):
            if current:
                blocks.append(current)
                current = []
        else:
            current.append(line.rstrip())
    if current:
        blocks.append(current)
    return blocks


def write_file(path, lines):
    with open(path, 'w') as f:
        for l in lines:
            f.write(l + '\n')


def main():
    parser = argparse.ArgumentParser(description="Parse exe output and generate graphs/routes files")
    parser.add_argument('--vrp_file', required=True, help='path to .vrp file')
    parser.add_argument('--exe_out', required=True, help='path to executable output file')
    args = parser.parse_args()

    vrp_path = os.path.abspath(args.vrp_file)
    exe_out_path = os.path.abspath(args.exe_out)
    work_dir = os.path.dirname(exe_out_path)
    base_name = os.path.splitext(os.path.basename(vrp_path))[0]

    # Script directory where this parser, GraphPlotter.py, and RoutesPlotter.py reside
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Prepare temporary working directory
    temp_dir = os.path.join(work_dir, 'temp')
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    shutil.copy(vrp_path, temp_dir)

    # Read and split executable output
    with open(exe_out_path) as f:
        lines = f.readlines()
    blocks = parse_blocks(lines)

    cost_data = []

    for blk in blocks:
        if not blk:
            continue
        heading = blk[0].strip().rstrip(':')
        content = blk[1:]

        # GRAPH block
        if heading.startswith('GRAPH'):
            graph_file = os.path.join(temp_dir, f"{base_name}.graph")
            write_file(graph_file, content)
            # Invoke GraphPlotter from script directory
            subprocess.run([
                sys.executable,
                os.path.join(script_dir, 'GraphPlotter.py'),
                temp_dir,
                heading
            ], check=True)
            # Move any generated .png/.html back to work_dir
            for fname in os.listdir(temp_dir):
                if fname.endswith('.png') or fname.endswith('.html'):
                    shutil.move(os.path.join(temp_dir, fname), os.path.join(work_dir, fname))
            os.remove(graph_file)

        # ROUTES blocks (iteration, loop, refinement)
        elif heading.startswith('ROUTES'):
            sol_file = os.path.join(temp_dir, f"{base_name}.sol")
            write_file(sol_file, content)
            # Extract cost from last line
            if content and content[-1].startswith('Cost'):
                _, val = content[-1].split(maxsplit=1)
                cost_data.append((heading, val))
            # Invoke RoutesPlotter
            subprocess.run([
                sys.executable,
                os.path.join(script_dir, 'RoutesPlotter.py'),
                '--input', temp_dir,
                '--output', temp_dir
            ], check=True)
            # Move and rename the generated files
            pngs = [f for f in os.listdir(temp_dir) if f.endswith('.png')]
            htmls = [f for f in os.listdir(temp_dir) if f.endswith('.html')]
            if pngs and htmls:
                src_png = os.path.join(temp_dir, pngs[0])
                src_html = os.path.join(temp_dir, htmls[0])
                shutil.move(src_png, os.path.join(work_dir, f"{heading}.png"))
                shutil.move(src_html, os.path.join(work_dir, f"{heading}.html"))
            os.remove(sol_file)

        # FINAL_OUTPUT block
        elif heading == 'FINAL_OUTPUT':
            final_sol = os.path.join(work_dir, f"{base_name}.sol")
            write_file(final_sol, content)
            shutil.rmtree(temp_dir)

    # Generate CSV and HTML plot if costs were recorded
    if cost_data:
        csv_path = os.path.join(work_dir, f"{base_name}_costs.csv")
        with open(csv_path, 'w', newline='') as cf:
            writer = csv.writer(cf)
            writer.writerow(['step', 'value'])
            for step, val in cost_data:
                writer.writerow([step, val])

        html_path = os.path.join(work_dir, f"{base_name}_costs.html")
        steps = [s for s, _ in cost_data]
        values = [float(v) for _, v in cost_data]
        html_content = f"""
<!DOCTYPE html>
<html>
<head><meta charset=\"utf-8\"/><script src=\"https://cdn.plot.ly/plotly-latest.min.js\"></script></head>
<body>
<div id=\"plot\"></div>
<script>
var data = [ {{ x: {steps}, y: {values}, mode: 'lines+markers', name: 'Cost' }} ];
var layout = {{ title: 'Cost over steps', xaxis: {{ title: 'Step' }}, yaxis: {{ title: 'Cost' }} }};
Plotly.newPlot('plot', data, layout);
</script>
</body>
</html>
"""
        with open(html_path, 'w') as hf:
            hf.write(html_content)

if __name__ == '__main__':
    main()
