import os
import sys
import time
import argparse
import html as html_lib
import json
import re


def parse_vrp(filepath):
    coords = {}
    depot_id = None
    in_coord = in_depot = False
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line == 'NODE_COORD_SECTION': in_coord = True; continue
            if line == 'DEMAND_SECTION': in_coord = False; continue
            if line == 'DEPOT_SECTION': in_depot = True; in_coord = False; continue
            if in_coord:
                parts = line.split()
                if len(parts) >= 3:
                    coords[int(parts[0])] = (float(parts[1]), float(parts[2]))
                continue
            if in_depot:
                if line in ('-1','EOF'): in_depot = False
                else:
                    try: depot_id = int(line)
                    except ValueError: pass
    return coords, depot_id


def parse_sol(filepath):
    routes = []
    cost = None
    route_pat = re.compile(r"Route #\d+:\s*(.*)")
    cost_pat = re.compile(r"Cost\s+(\d+(?:\.\d+)?)")
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            m = route_pat.match(line)
            if m:
                nums = [int(x) for x in m.group(1).split() if x.isdigit()]
                routes.append(nums)
                continue
            c = cost_pat.match(line)
            if c:
                cost = float(c.group(1))
    return routes, cost


def _fmt_cost(cost):
    """Format cost for titles/logs: no trailing .0 unless a real fractional part."""
    if cost is None:
        return '—'
    c = float(cost)
    if abs(c - round(c)) < 1e-9:
        return str(int(round(c)))
    # Keep meaningful decimals; drop useless trailing zeros (e.g. 1042.120 -> 1042.12)
    text = f'{c:.10f}'.rstrip('0').rstrip('.')
    return text


def plot_static(coords, routes, depot_id, output_base, cost, show_legend=False, formats=None):
    """Static PNG/PDF: Times New Roman, depot on top, Depot/Customer legend top-right."""
    try:
        import matplotlib.pyplot as plt
        from matplotlib.lines import Line2D
    except ImportError:
        print(
            "ERROR: matplotlib is required for PNG/PDF plots.\n"
            "  pip install -r Scripts/requirements.txt",
            file=sys.stderr,
        )
        sys.exit(1)

    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif', 'serif'],
        'mathtext.fontset': 'stix',
        'axes.titlesize': 9,
        'axes.labelsize': 8,
        'xtick.labelsize': 7,
        'ytick.labelsize': 7,
    })

    coords0 = {nid - 1: xy for nid, xy in coords.items()}
    depot0 = depot_id - 1 if depot_id is not None else None

    all_x = [xy[0] for xy in coords0.values()]
    all_y = [xy[1] for xy in coords0.values()]
    xmin, xmax = min(all_x), max(all_x)
    ymin, ymax = min(all_y), max(all_y)
    span_x = max(xmax - xmin, 1.0)
    span_y = max(ymax - ymin, 1.0)
    pad_x = 0.03 * span_x
    pad_y = 0.03 * span_y
    aspect = (span_x + 2 * pad_x) / (span_y + 2 * pad_y)

    # Compact figure: follow data aspect, moderate height for PNG/PDF.
    target_w = 8.5
    fig_h = target_w / aspect
    fig_h = max(3.4, min(fig_h, 5.0))   # middle ground (not too tall / short)
    fig_w = fig_h * aspect
    fig_w = max(5.5, min(fig_w, 12.0))
    fig_h = fig_w / aspect
    fig_h = max(3.4, min(fig_h, 5.0))

    fig, ax = plt.subplots(figsize=(fig_w, fig_h), facecolor='white')
    ax.set_facecolor('white')

    # Routes under the depot (low zorder); customer markers colored with each route
    for i, route in enumerate(routes, start=1):
        seq = ([depot0] + route + [depot0]) if depot0 is not None else route
        xs = [coords0[n][0] for n in seq if n in coords0]
        ys = [coords0[n][1] for n in seq if n in coords0]
        ax.plot(
            xs, ys,
            marker='o', markersize=0.9, linewidth=0.4,
            zorder=2,
            label=f'Route {i}' if show_legend else None,
        )

    # Invisible proxy for "Customer" in the always-on key
    customer_proxy = Line2D(
        [0], [0],
        linestyle='None',
        marker='o', markersize=5,
        markerfacecolor='black', markeredgecolor='black',
        label='Customer',
    )

    # Depot last / highest zorder so it never sits under routes
    depot_handle = None
    if depot0 is not None and depot0 in coords0:
        dx, dy = coords0[depot0]
        # White halo so the star stays readable over dense route lines
        ax.plot(
            dx, dy,
            linestyle='None', marker='*', markersize=19,
            color='white', markeredgewidth=0, zorder=9,
        )
        depot_handle, = ax.plot(
            dx, dy,
            linestyle='None', marker='*', markersize=14,
            color='red', markeredgecolor='black', markeredgewidth=1.2,
            zorder=10,
        )
    else:
        print(f"WARNING: Depot ID {depot_id} not found in coords.")

    cost_str = _fmt_cost(cost)
    ax.set_title(f'Routes - Cost: {cost_str}', fontname='Times New Roman', fontsize=9)
    ax.set_xlabel('X Coordinate', fontname='Times New Roman', fontsize=8)
    ax.set_ylabel('Y Coordinate', fontname='Times New Roman', fontsize=8)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontname('Times New Roman')
        label.set_fontsize(7)

    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.set_xlim(xmin - pad_x, xmax + pad_x)
    ax.set_ylim(ymin - pad_y, ymax + pad_y)
    ax.set_aspect('equal', adjustable='box')

    # Always: Depot + Customer at upper right (matches reference plots)
    handles = []
    labels = []
    if depot_handle is not None:
        handles.append(
            Line2D(
                [0], [0],
                linestyle='None',
                marker='*', markersize=12,
                markerfacecolor='red', markeredgecolor='black',
                markeredgewidth=1.2,
            )
        )
        labels.append('Depot')
    handles.append(customer_proxy)
    labels.append('Customer')

    if show_legend:
        # Optional per-route entries after Depot/Customer
        rh, rl = ax.get_legend_handles_labels()
        for h, lab in zip(rh, rl):
            if lab.startswith('Route'):
                handles.append(h)
                labels.append(lab)

    leg = ax.legend(
        handles, labels,
        loc='upper right',
        fontsize=8,
        frameon=True,
        fancybox=False,
        edgecolor='black',
        framealpha=1.0,
        facecolor='white',
        borderpad=0.4,
        handlelength=1.4,
    )
    for text in leg.get_texts():
        text.set_fontname('Times New Roman')

    fig.tight_layout(pad=0.4)
    out_dir = os.path.dirname(output_base)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    if formats is None:
        formats = ('.png',)
    saved = []
    for ext in formats:
        if not ext.startswith('.'):
            ext = '.' + ext
        path = output_base + ext
        fig.savefig(
            path, dpi=300, bbox_inches='tight', pad_inches=0.08,
            facecolor='white',
        )
        saved.append(path)
    plt.close(fig)
    return tuple(saved)

def plot_interactive_html(coords, routes, depot_id, input_name, cost, output_path, show_legend=False):
    # show_legend is unused for HTML: interactive view always shows the route legend
    _ = show_legend
    try:
        import plotly.graph_objects as go
    except ImportError:
        print(
            "ERROR: plotly is required for --html output.\n"
            "  pip install -r Scripts/requirements.txt",
            file=sys.stderr,
        )
        sys.exit(1)

    coords0 = {nid - 1: xy for nid, xy in coords.items()}
    depot0 = depot_id - 1 if depot_id is not None else None

    fig = go.Figure()

    # Customers first (under routes)
    cust_ids = [nid for nid in coords0 if nid != depot0]
    if cust_ids:
        fig.add_trace(go.Scatter(
            x=[coords0[n][0] for n in cust_ids],
            y=[coords0[n][1] for n in cust_ids],
            mode='markers',
            name='Customers',
            marker=dict(size=5, color='#64748b', opacity=0.85),
            hovertemplate='Customer %{text}<br>(%{x}, %{y})<extra></extra>',
            text=[str(n) for n in cust_ids],
            showlegend=False,
        ))
        customers_idx = 0
    else:
        customers_idx = None

    route_indices = []
    for i, route in enumerate(routes, start=1):
        seq = ([depot0] + route + [depot0]) if depot0 is not None else route
        xs = [coords0[n][0] for n in seq if n in coords0]
        ys = [coords0[n][1] for n in seq if n in coords0]
        fig.add_trace(go.Scatter(
            x=xs, y=ys,
            mode='lines',
            name=f'Route {i}',
            line=dict(width=1.4),
            hovertemplate=f'Route {i}<br>(%{{x}}, %{{y}})<extra></extra>',
            showlegend=True,
        ))
        route_indices.append(len(fig.data) - 1)

    # Depot last so it renders on top of route lines
    depot_idx = None
    if depot0 is not None and depot0 in coords0:
        x, y = coords0[depot0]
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers',
            name='Depot',
            marker=dict(symbol='star', size=16, color='#e11d48', line=dict(width=1.2, color='#000')),
            hovertemplate=f'Depot<br>({x}, {y})<extra></extra>',
            showlegend=False,
        ))
        depot_idx = len(fig.data) - 1

    # Equal aspect without scaleanchor (scaleanchor breaks pan/zoom in Plotly).
    all_x = [xy[0] for xy in coords0.values()]
    all_y = [xy[1] for xy in coords0.values()]
    xmin, xmax = min(all_x), max(all_x)
    ymin, ymax = min(all_y), max(all_y)
    cx, cy = (xmin + xmax) / 2.0, (ymin + ymax) / 2.0
    half = max(xmax - xmin, ymax - ymin, 1.0) * 0.55
    x_range = [cx - half, cx + half]
    y_range = [cy - half, cy + half]

    fig.update_layout(
        title=None,
        template='plotly_white',
        showlegend=True,
        dragmode='pan',
        legend=dict(
            title=dict(text='Routes (click to toggle)'),
            font=dict(size=11),
            bgcolor='rgba(255,255,255,0.92)',
            bordercolor='#e2e8f0',
            borderwidth=1,
            itemclick='toggle',
            itemdoubleclick='toggleothers',
        ),
        margin=dict(l=40, r=20, t=20, b=40),
        xaxis=dict(
            title='X', zeroline=False, showgrid=True, gridcolor='#e2e8f0',
            range=x_range, fixedrange=False,
        ),
        yaxis=dict(
            title='Y', zeroline=False, showgrid=True, gridcolor='#e2e8f0',
            range=y_range, fixedrange=False,
        ),
        hovermode='closest',
        plot_bgcolor='#f8fafc',
        paper_bgcolor='#ffffff',
    )

    cost_str = _fmt_cost(cost)
    display_name = html_lib.escape(os.path.splitext(input_name)[0])
    n_customers = len(cust_ids)
    n_routes = len(routes)

    fig_dict = fig.to_dict()
    payload = json.dumps({
        'data': fig_dict['data'],
        'layout': fig_dict['layout'],
        'customersIdx': customers_idx,
        'depotIdx': depot_idx,
        'routeIndices': route_indices,
    })

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{display_name} — CVRP BKS Routes</title>
  <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
  <style>
    :root {{
      --bar: #0f2744;
      --accent: #38bdf8;
      --panel: #f1f5f9;
      --text: #0f172a;
      --muted: #64748b;
      --border: #cbd5e1;
    }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; padding: 0; height: 100%; font-family: "Segoe UI", system-ui, sans-serif; color: var(--text); background: #fff; }}
    .topbar {{
      background: linear-gradient(90deg, #0f2744 0%, #1e3a5f 100%);
      color: #fff;
      padding: 14px 22px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 10px 24px;
      border-bottom: 3px solid var(--accent);
    }}
    .topbar h1 {{ margin: 0; font-size: 1.15rem; font-weight: 650; letter-spacing: 0.02em; }}
    .topbar .eyebrow {{ margin: 0 0 2px; font-size: 0.72rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--accent); opacity: 0.95; }}
    .topbar .instance {{ margin: 0; font-size: 1.15rem; font-weight: 650; letter-spacing: 0.02em; }}
    .meta {{ display: flex; flex-wrap: wrap; gap: 8px 10px; }}
    .chip {{
      background: rgba(255,255,255,0.12);
      border: 1px solid rgba(255,255,255,0.18);
      border-radius: 999px;
      padding: 4px 12px;
      font-size: 0.85rem;
    }}
    .chip strong {{ font-weight: 650; }}
    .toolbar {{
      background: var(--panel);
      border-bottom: 1px solid var(--border);
      padding: 10px 22px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px 18px;
    }}
    .toolbar .label {{ color: var(--muted); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.06em; margin-right: 4px; }}
    .toolbar label {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.92rem;
      cursor: pointer;
      user-select: none;
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 6px 12px;
    }}
    .toolbar input {{ width: 15px; height: 15px; accent-color: #0f2744; cursor: pointer; }}
    #plot {{ width: 100%; height: calc(100vh - 200px); min-height: 420px; }}
    .credits {{
      border-top: 1px solid var(--border);
      background: #f8fafc;
      padding: 14px 22px 18px;
      color: var(--muted);
      font-size: 0.78rem;
      line-height: 1.45;
    }}
    .credits .label {{
      display: block;
      margin-bottom: 6px;
      color: #334155;
      font-size: 0.72rem;
      font-weight: 650;
      letter-spacing: 0.07em;
      text-transform: uppercase;
    }}
    .credits ul {{
      margin: 0;
      padding: 0;
      list-style: none;
      display: flex;
      flex-wrap: wrap;
      gap: 6px 18px;
    }}
    .credits li {{ white-space: nowrap; }}
    .credits .note {{ margin: 6px 0 0; font-size: 0.72rem; color: #94a3b8; }}
  </style>
</head>
<body>
  <header class="topbar">
    <div>
      <p class="eyebrow">CVRP BKS Routes</p>
      <h1 class="instance">{display_name}</h1>
    </div>
    <div class="meta">
      <span class="chip">Cost <strong>{html_lib.escape(cost_str)}</strong></span>
      <span class="chip">Routes <strong>{n_routes}</strong></span>
      <span class="chip">Customers <strong>{n_customers}</strong></span>
    </div>
  </header>
  <div class="toolbar">
    <span class="label">Layers</span>
    <label><input type="checkbox" id="tog-customers" checked/> Customers</label>
    <label><input type="checkbox" id="tog-depot" checked/> Depot</label>
    <label><input type="checkbox" id="tog-routes" checked/> All routes</label>
  </div>
  <div id="plot"></div>
  <footer class="credits">
    <span class="label">Work by</span>
    <ul>
      <li>Chekkala Sandeep Reddy*</li>
      <li>Lakshya Rani P</li>
      <li>Somesh Singh</li>
      <li>Rajesh Pandian Muniasamy</li>
      <li>Rupesh Nasre</li>
    </ul>
    <p class="note">* Primary contact</p>
  </footer>
  <script>
    const payload = {payload};
    const config = {{
      responsive: true,
      scrollZoom: true,
      displaylogo: false,
      modeBarButtonsToRemove: [
        'lasso2d', 'select2d', 'autoScale2d',
        'hoverClosestCartesian', 'hoverCompareCartesian',
        'toggleSpikelines'
      ],
      toImageButtonOptions: {{ format: 'png', filename: 'BKS_{display_name}_routes' }}
    }};

    Plotly.newPlot('plot', payload.data, payload.layout, config).then(() => {{
      const setVisible = (indices, visible) => {{
        // Note: customersIdx can be 0 — do not use truthiness checks.
        if (indices === null || indices === undefined) return;
        if (Array.isArray(indices) && indices.length === 0) return;
        Plotly.restyle('plot', {{ visible }}, indices);
      }};

      document.getElementById('tog-customers').addEventListener('change', (e) => {{
        if (payload.customersIdx !== null) setVisible(payload.customersIdx, e.target.checked);
      }});
      document.getElementById('tog-depot').addEventListener('change', (e) => {{
        if (payload.depotIdx !== null) setVisible(payload.depotIdx, e.target.checked);
      }});
      document.getElementById('tog-routes').addEventListener('change', (e) => {{
        // Use 'legendonly' (not false) so routes stay in the legend and can be
        // re-enabled one-by-one by clicking legend items.
        setVisible(payload.routeIndices, e.target.checked ? true : 'legendonly');
      }});
    }});
  </script>
</body>
</html>
"""
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(page)
    return output_path


def _print_usage_and_exit(message=None):
    text = """
RoutesPlotter — plot vehicle routes from matching .vrp + .sol pairs

USAGE
  python RoutesPlotter.py <input_dir> <output_dir> [flags]
  python RoutesPlotter.py --input <input_dir> --output <output_dir> [flags]

REQUIRED
  input_dir    Directory containing matching .vrp and .sol files
  output_dir   Directory where plots will be written

FLAGS (all optional; off by default)
  --html       Also write interactive BKS_*_routes.html
  --pdf        Also write static BKS_*_routes.pdf
  --legend     Also list per-route entries (Depot/Customer always shown)
  -h, --help   Show this help

DEFAULT
  Only BKS_*_routes.png is written.

EXAMPLES
  python RoutesPlotter.py Inputs/CVRPLIB/CMT Results/routes
  python RoutesPlotter.py --input Inputs/CVRPLIB/CMT --output Results/routes --html
  python RoutesPlotter.py Inputs/CVRPLIB/CMT Results/routes --pdf --legend
""".strip()
    if message:
        print(f"ERROR: {message}\n", file=sys.stderr)
    print(text, file=sys.stderr)
    sys.exit(2)


def _fmt_tags(formats, wrote_html):
    tags = []
    for ext in formats:
        tags.append(ext.lstrip('.').upper())
    if wrote_html:
        tags.append('HTML')
    return ' '.join(tags)


def main():
    parser = argparse.ArgumentParser(
        description="Plot VRP routes with cost (PNG by default).",
        add_help=False,
    )
    parser.add_argument('input_pos', nargs='?', default=None)
    parser.add_argument('output_pos', nargs='?', default=None)
    parser.add_argument('--input', '-i', dest='input_opt', default=None)
    parser.add_argument('--output', '-o', dest='output_opt', default=None)
    parser.add_argument(
        '--html', action='store_true',
        help='Also write interactive BKS_*_routes.html (off by default)',
    )
    parser.add_argument(
        '--pdf', action='store_true',
        help='Also write static BKS_*_routes.pdf (off by default)',
    )
    parser.add_argument(
        '--legend', action='store_true',
        help='Show route legend on static plots (off by default)',
    )
    parser.add_argument('-h', '--help', action='store_true')

    try:
        args, unknown = parser.parse_known_args()
    except SystemExit:
        _print_usage_and_exit()

    if args.help:
        _print_usage_and_exit()

    if unknown:
        _print_usage_and_exit(
            f"unknown argument(s): {' '.join(unknown)}"
        )

    input_dir = args.input_opt or args.input_pos
    output_dir = args.output_opt or args.output_pos

    missing = []
    if not input_dir:
        missing.append('input_dir')
    if not output_dir:
        missing.append('output_dir')
    if missing:
        _print_usage_and_exit(
            f"missing required field(s): {', '.join(missing)}"
        )

    if not os.path.isdir(input_dir):
        _print_usage_and_exit(
            f"input_dir is not a directory: {input_dir}"
        )

    os.makedirs(output_dir, exist_ok=True)

    formats = ['.png']
    if args.pdf:
        formats.append('.pdf')

    # Discover jobs grouped by relative directory
    groups = {}  # rel_dir -> [(file, vrp_path, sol_path, base)]
    for root, _, files in os.walk(input_dir):
        for file in sorted(files):
            if not file.lower().endswith('.vrp'):
                continue
            vrp_path = os.path.join(root, file)
            sol_path = os.path.splitext(vrp_path)[0] + '.sol'
            rel = os.path.relpath(vrp_path, input_dir)
            base = os.path.splitext(rel)[0]
            rel_dir = os.path.dirname(rel) or '.'
            groups.setdefault(rel_dir, []).append(
                (file, vrp_path, sol_path, base)
            )

    if not groups:
        _print_usage_and_exit(f"no .vrp files found under: {input_dir}")

    n_vrp = sum(len(v) for v in groups.values())
    fmt_label = ', '.join(ext.lstrip('.').upper() for ext in formats)
    if args.html:
        fmt_label += ', HTML'

    bar = '─' * 56
    print()
    print(bar)
    print('  RoutesPlotter')
    print(bar)
    print(f'  input   : {input_dir}')
    print(f'  output  : {output_dir}')
    print(f'  write   : {fmt_label}')
    print(f'  legend  : {"on" if args.legend else "off"}')
    print(f'  found   : {n_vrp} .vrp file(s) in {len(groups)} folder(s)')
    print(bar)

    n_ok = 0
    n_missing_sol = 0
    t0 = time.time()

    for rel_dir in sorted(groups.keys()):
        jobs = groups[rel_dir]
        folder_label = rel_dir if rel_dir != '.' else os.path.basename(
            os.path.abspath(input_dir)
        )
        print()
        print(f'▸ {folder_label}  ({len(jobs)} instance{"s" if len(jobs) != 1 else ""})')

        name_width = max(len(os.path.splitext(f)[0]) for f, *_ in jobs)
        name_width = min(max(name_width, 12), 40)

        for file, vrp_path, sol_path, base in jobs:
            name = os.path.splitext(file)[0]
            if not os.path.exists(sol_path):
                print(f'  ✗ {name:<{name_width}}  missing .sol')
                n_missing_sol += 1
                continue

            coords, depot_id = parse_vrp(vrp_path)
            routes, cost = parse_sol(sol_path)

            # Mirror Inputs/ tree under output_dir; BKS_ only on the filename
            rel_subdir = os.path.dirname(base)
            stem = os.path.basename(base)
            out_subdir = (
                os.path.join(output_dir, rel_subdir) if rel_subdir else output_dir
            )
            os.makedirs(out_subdir, exist_ok=True)
            out_base = os.path.join(out_subdir, f'BKS_{stem}_routes')
            plot_static(
                coords, routes, depot_id, out_base, cost,
                show_legend=args.legend,
                formats=tuple(formats),
            )

            wrote_html = False
            if args.html:
                out_html = os.path.join(out_subdir, f'BKS_{stem}_routes.html')
                plot_interactive_html(
                    coords, routes, depot_id, file, cost, out_html,
                    show_legend=args.legend,
                )
                wrote_html = True

            tags = _fmt_tags(formats, wrote_html)
            cost_str = _fmt_cost(cost)
            n_routes = len(routes)
            print(
                f'  ✓ {name:<{name_width}}  {tags:<12}  '
                f'routes={n_routes:<4}  cost={cost_str}'
            )
            n_ok += 1

    elapsed = time.time() - t0
    print()
    print(bar)
    print(
        f'  done   ✓ {n_ok} plotted'
        f'   ✗ {n_missing_sol} skipped'
        + f'   {elapsed:.1f}s'
    )
    print(f'  output → {output_dir}')
    print(bar)
    print()


if __name__ == '__main__':
    main()
