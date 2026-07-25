import os
import argparse
import subprocess
import sys
import csv
import itertools

def parse_arg_list(arg_str):
    """
    Parse a string of the form "{a,b,c}" or "a,b,c" into a Python list.
    Empty or None returns [''] (no-arg placeholder).
    """
    if not arg_str:
        return [""]
    s = arg_str.strip()
    if s.startswith('{') and s.endswith('}'):
        s = s[1:-1]
    items = [item.strip() for item in s.split(',') if item.strip()]
    return items if items else [""]


def find_and_process(input_dir, exe_path, output_dir, param_lists):
    os.makedirs(output_dir, exist_ok=True)

    param_names = list(param_lists.keys())
    value_lists = [param_lists[name] for name in param_names]

    for comb in itertools.product(*value_lists):
        # Build named argument list in the same order as param_names
        named_args = [f"--{name}={val}" for name, val in zip(param_names, comb) if val]

        # Directory naming: name-val_name2-val2 or 'noargs'
        if named_args:
            pairs = [f"{name}-{val}" for name, val in zip(param_names, comb) if val]
            comb_dir_name = '_'.join(pairs)
        else:
            comb_dir_name = 'noargs'

        comb_output_dir = os.path.join(output_dir, comb_dir_name)
        os.makedirs(comb_output_dir, exist_ok=True)

        acc_file = os.path.join(comb_output_dir, 'accumulated_results.csv')
        # Collect all rows before writing
        rows = []

        for root, dirs, files in os.walk(input_dir):
            dirs.sort()
            files.sort()
            for file in files:
                if not file.endswith('.vrp'):
                    continue
                vrp_path = os.path.join(root, file)
                base_name = os.path.splitext(file)[0]

                # Define output subdirectory
                rel_dir = os.path.relpath(root, input_dir)
                if rel_dir in ('.', os.curdir):
                    out_subdir = os.path.join(comb_output_dir, base_name)
                else:
                    out_subdir = os.path.join(comb_output_dir, rel_dir, base_name)
                os.makedirs(out_subdir, exist_ok=True)

                sol_file = os.path.join(out_subdir, f"{base_name}.exe_sol")
                cmd = [exe_path, vrp_path] + named_args
                try:
                    with open(sol_file, 'w') as solf:
                        subprocess.run(cmd, stdout=solf, check=True)
                    print(f"Solved {vrp_path} with args {named_args} -> {sol_file}")
                except subprocess.CalledProcessError as e:
                    print(f"Error on {vrp_path} with args {named_args}: {e}", file=sys.stderr)
                    continue

                # Parse solver output
                try:
                    subprocess.run([
                        sys.executable, 'OutputParser.py',
                        '--vrp_file', vrp_path,
                        '--exe_out', sol_file
                    ], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Parse error for {vrp_path}: {e}", file=sys.stderr)
                    continue

                parsed_sol = os.path.join(out_subdir, f"{base_name}.sol")
                if os.path.exists(parsed_sol):
                    with open(parsed_sol) as pf:
                        lines = pf.readlines()
                    if len(lines) >= 2:
                        parts = [p.strip() for p in lines[1].split(',')]
                        file_col = base_name
                        time_loop = parts[1] if len(parts) > 1 else ''
                        total_time = parts[2] if len(parts) > 2 else ''
                        min_cost = parts[3] if len(parts) > 3 else ''
                        correctness = parts[4] if len(parts) > 4 else ''
                        rows.append([file_col, time_loop, total_time, min_cost, correctness])
                    else:
                        print(f"Warning: {parsed_sol} has <2 lines", file=sys.stderr)
                else:
                    print(f"Missing parsed sol: {parsed_sol}", file=sys.stderr)

        # After walking all files, sort rows by file-name
        rows.sort(key=lambda r: r[0])

        # Write header + sorted rows
        with open(acc_file, 'w', newline='') as csvf:
            writer = csv.writer(csvf)
            writer.writerow(['file-name', 'time_till_loop', 'total_elapsed_time', 'minCost', 'correctness'])
            writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="Batch-run VRP solver with named argument combos.")
    parser.add_argument('--input_dir', required=True, help='Root directory with .vrp files')
    parser.add_argument('--exe', required=True, help='Path to VRP solver executable')
    parser.add_argument('--output_dir', required=True, help='Base output directory')
    args, unknown = parser.parse_known_args()

    # Build param_lists: key -> list of values
    param_lists = {}
    for token in unknown:
        if token.startswith('--') and '=' in token:
            key, val = token[2:].split('=', 1)
            values = parse_arg_list(val)
            param_lists.setdefault(key, []).extend(values)

    # Dedupe preserving order
    for key, vals in param_lists.items():
        seen = set(); unique = []
        for v in vals:
            if v not in seen:
                seen.add(v); unique.append(v)
        param_lists[key] = unique

    find_and_process(args.input_dir, args.exe, args.output_dir, param_lists)

if __name__ == '__main__':
    main()
