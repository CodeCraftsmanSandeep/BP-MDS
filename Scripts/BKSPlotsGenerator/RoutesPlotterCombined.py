#!/usr/bin/env python3
"""
RoutesPlotterCombined — side-by-side route plots for paired instances.

Default pairs (AGS-style *1 / *2):
  Antwerp1|Antwerp2, Brussels1|Brussels2, Flanders1|Flanders2,
  Ghent1|Ghent2, Leuven1|Leuven2

Add more pairs later via --pairs or by editing DEFAULT_PAIRS.
"""

import os
import sys
import time
import argparse

# Reuse parsers / cost formatting / style helpers from RoutesPlotter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from RoutesPlotter import parse_vrp, parse_sol, _fmt_cost  # noqa: E402


# (left_name, right_name) — stem without extension
DEFAULT_PAIRS = [
    ('Antwerp1', 'Antwerp2'),
    ('Brussels1', 'Brussels2'),
    ('Flanders1', 'Flanders2'),
    ('Ghent1', 'Ghent2'),
    ('Leuven1', 'Leuven2'),
]


def _print_usage_and_exit(message=None):
    text = """
RoutesPlotterCombined — side-by-side route plots for paired instances

USAGE
  python RoutesPlotterCombined.py <input_dir> <output_dir> [flags]
  python RoutesPlotterCombined.py --input <input_dir> --output <output_dir> [flags]

REQUIRED
  input_dir    Directory with matching .vrp + .sol files (e.g. Inputs/CVRPLIB/AGS)
  output_dir   Directory where combined plots will be written

FLAGS (all optional; off by default)
  --pdf        Also write static BKS_*_combined.pdf
  --pairs a,b;c,d   Extra / override pairs (name stems). Example:
               --pairs Flanders1,Flanders2;Brussels1,Brussels2
  -h, --help   Show this help

DEFAULT
  Only BKS_*_combined.png is written.
  Built-in AGS pairs: Antwerp, Brussels, Flanders, Ghent, Leuven (1 vs 2).

EXAMPLES
  python RoutesPlotterCombined.py Inputs/CVRPLIB/AGS Results/BKSPlots/combined
  python RoutesPlotterCombined.py Inputs/CVRPLIB/AGS Results/combined --pdf
""".strip()
    if message:
        print(f"ERROR: {message}\n", file=sys.stderr)
    print(text, file=sys.stderr)
    sys.exit(2)


def _find_instance(input_dir, stem):
    """Return (vrp_path, sol_path) for stem, searching under input_dir."""
    for root, _, files in os.walk(input_dir):
        for f in files:
            if f == stem + '.vrp' or f == stem + '.VRP':
                vrp = os.path.join(root, f)
                sol = os.path.splitext(vrp)[0] + '.sol'
                return vrp, sol
    return None, None


def _load_instance(input_dir, stem):
    vrp, sol = _find_instance(input_dir, stem)
    if vrp is None:
        return None, f'missing {stem}.vrp under {input_dir}'
    if not os.path.exists(sol):
        return None, f'missing {stem}.sol (expected next to {vrp})'
    coords, depot_id = parse_vrp(vrp)
    routes, cost = parse_sol(sol)
    return {
        'name': stem,
        'coords': coords,
        'depot_id': depot_id,
        'routes': routes,
        'cost': cost,
    }, None


def _data_aspect(inst):
    """Width/height of padded data box (for equal-aspect figure sizing)."""
    coords = inst['coords']
    all_x = [xy[0] for xy in coords.values()]
    all_y = [xy[1] for xy in coords.values()]
    span_x = max(max(all_x) - min(all_x), 1.0)
    span_y = max(max(all_y) - min(all_y), 1.0)
    return (span_x * 1.06) / (span_y * 1.06)


def _draw_panel(ax, inst, show_ylabel=True, yticks_right=False, panel_label=None):
    """Draw one instance onto ax (shared style with RoutesPlotter)."""
    coords = inst['coords']
    routes = inst['routes']
    depot_id = inst['depot_id']

    coords0 = {nid - 1: xy for nid, xy in coords.items()}
    depot0 = depot_id - 1 if depot_id is not None else None

    for route in routes:
        seq = ([depot0] + route + [depot0]) if depot0 is not None else route
        xs = [coords0[n][0] for n in seq if n in coords0]
        ys = [coords0[n][1] for n in seq if n in coords0]
        ax.plot(xs, ys, marker='o', markersize=0.9, linewidth=0.4, zorder=2)

    if depot0 is not None and depot0 in coords0:
        dx, dy = coords0[depot0]
        # White halo so the star stays readable over dense route lines
        ax.plot(
            dx, dy,
            linestyle='None', marker='*', markersize=19,
            color='white', markeredgewidth=0, zorder=9,
        )
        ax.plot(
            dx, dy,
            linestyle='None', marker='*', markersize=14,
            color='red', markeredgecolor='black', markeredgewidth=1.2,
            zorder=10,
        )

    all_x = [xy[0] for xy in coords0.values()]
    all_y = [xy[1] for xy in coords0.values()]
    xmin, xmax = min(all_x), max(all_x)
    ymin, ymax = min(all_y), max(all_y)
    span_x = max(xmax - xmin, 1.0)
    span_y = max(ymax - ymin, 1.0)
    pad_x, pad_y = 0.03 * span_x, 0.03 * span_y
    ax.set_xlim(xmin - pad_x, xmax + pad_x)
    ax.set_ylim(ymin - pad_y, ymax + pad_y)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, linestyle='--', linewidth=0.5)

    cost_str = _fmt_cost(inst['cost'])
    prefix = f'({panel_label})  ' if panel_label else ''
    ax.set_title(
        f"{prefix}{inst['name']}  —  Cost: {cost_str}",
        fontname='Times New Roman', fontsize=9,
    )
    ax.set_xlabel('', fontname='Times New Roman', fontsize=8)
    if show_ylabel:
        ax.set_ylabel('Y Coordinate', fontname='Times New Roman', fontsize=8)
    else:
        ax.set_ylabel('')
    # Put right-panel ticks on the outer edge so panels can sit flush
    if yticks_right:
        ax.yaxis.tick_right()
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontname('Times New Roman')
        label.set_fontsize(7)


def plot_pair(left, right, output_base, formats=('.png',)):
    try:
        import matplotlib.pyplot as plt
        from matplotlib.lines import Line2D
    except ImportError:
        print(
            "ERROR: matplotlib is required.\n"
            "  pip install -r Scripts/requirements.txt",
            file=sys.stderr,
        )
        sys.exit(1)

    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif', 'serif'],
        'mathtext.fontset': 'stix',
    })

    # Inch-accurate panel placement so equal-aspect axes fill exactly
    # (GridSpec left leftover gap when fig width ≠ axes height × aspects).
    a0 = _data_aspect(left)
    a1 = _data_aspect(right)
    gap_in = 0.06          # space between the two plot frames
    margin_l = 0.55        # Y label + left ticks
    margin_r = 0.38        # right-panel outer Y ticks
    margin_b = 0.40        # X labels
    margin_t = 0.42        # shared legend + titles
    ax_h = 2.70            # panel height (controls overall figure height)
    ax_w0 = ax_h * a0
    ax_w1 = ax_h * a1
    fig_w = margin_l + ax_w0 + gap_in + ax_w1 + margin_r
    fig_h = margin_b + ax_h + margin_t

    fig = plt.figure(figsize=(fig_w, fig_h), facecolor='white')
    ax0 = fig.add_axes([
        margin_l / fig_w,
        margin_b / fig_h,
        ax_w0 / fig_w,
        ax_h / fig_h,
    ])
    ax1 = fig.add_axes([
        (margin_l + ax_w0 + gap_in) / fig_w,
        margin_b / fig_h,
        ax_w1 / fig_w,
        ax_h / fig_h,
    ])
    ax0.set_facecolor('white')
    ax1.set_facecolor('white')

    # Right panel: no Y label; ticks on the right so panels sit close
    _draw_panel(ax0, left, show_ylabel=True, yticks_right=False, panel_label='a')
    _draw_panel(ax1, right, show_ylabel=False, yticks_right=True, panel_label='b')

    # One shared X label centered under both plot frames (after equal-aspect
    # shrink), so it sits in the middle of the pair — not under one panel.
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    inv = fig.transFigure.inverted()
    b0 = ax0.get_window_extent(renderer)
    b1 = ax1.get_window_extent(renderer)
    x0, y0 = inv.transform((b0.x0, b0.y0))
    x1, _ = inv.transform((b1.x1, b1.y0))
    ax_xlabel = fig.add_axes([x0, max(0.01, y0 - 0.11), x1 - x0, 0.07])
    ax_xlabel.set_axis_off()
    ax_xlabel.text(
        0.5, 0.4, 'X Coordinate',
        ha='center', va='center',
        fontname='Times New Roman', fontsize=8,
        transform=ax_xlabel.transAxes,
    )

    # Shared Depot / Customer legend — top center, above both panels
    handles = [
        Line2D(
            [0], [0], linestyle='None',
            marker='*', markersize=9,
            markerfacecolor='red', markeredgecolor='black',
            markeredgewidth=1.0,
        ),
        Line2D(
            [0], [0], linestyle='None',
            marker='o', markersize=3.5,
            markerfacecolor='black', markeredgecolor='black',
        ),
    ]
    labels = ['Depot', 'Customer']
    leg = fig.legend(
        handles, labels,
        loc='upper center',
        ncol=2,
        fontsize=7,
        frameon=False,
        borderpad=0.3,
        handletextpad=0.4,
        columnspacing=1.0,
        bbox_to_anchor=(0.5, 0.985),
    )
    for text in leg.get_texts():
        text.set_fontname('Times New Roman')

    out_dir = os.path.dirname(output_base)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    saved = []
    for ext in formats:
        if not ext.startswith('.'):
            ext = '.' + ext
        path = output_base + ext
        fig.savefig(
            path, dpi=300, bbox_inches='tight', pad_inches=0.06,
            facecolor='white',
        )
        saved.append(path)
    plt.close(fig)
    return tuple(saved)


def _parse_pairs_arg(text):
    """Parse 'A,B;C,D' into [('A','B'), ('C','D')]."""
    pairs = []
    for chunk in text.split(';'):
        chunk = chunk.strip()
        if not chunk:
            continue
        parts = [p.strip() for p in chunk.split(',') if p.strip()]
        if len(parts) != 2:
            _print_usage_and_exit(
                f"bad --pairs entry '{chunk}' (want name1,name2)"
            )
        pairs.append((parts[0], parts[1]))
    return pairs


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('input_pos', nargs='?', default=None)
    parser.add_argument('output_pos', nargs='?', default=None)
    parser.add_argument('--input', '-i', dest='input_opt', default=None)
    parser.add_argument('--output', '-o', dest='output_opt', default=None)
    parser.add_argument('--pdf', action='store_true')
    parser.add_argument(
        '--pairs', default=None,
        help='Override/extend pairs: name1,name2;name3,name4',
    )
    parser.add_argument('-h', '--help', action='store_true')

    try:
        args, unknown = parser.parse_known_args()
    except SystemExit:
        _print_usage_and_exit()

    if args.help:
        _print_usage_and_exit()
    if unknown:
        _print_usage_and_exit(f"unknown argument(s): {' '.join(unknown)}")

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
        _print_usage_and_exit(f"input_dir is not a directory: {input_dir}")

    pairs = _parse_pairs_arg(args.pairs) if args.pairs else list(DEFAULT_PAIRS)

    formats = ['.png']
    if args.pdf:
        formats.append('.pdf')

    os.makedirs(output_dir, exist_ok=True)

    bar = '─' * 56
    print()
    print(bar)
    print('  RoutesPlotterCombined')
    print(bar)
    print(f'  input   : {input_dir}')
    print(f'  output  : {output_dir}')
    print(f'  write   : {", ".join(e.lstrip(".").upper() for e in formats)}')
    print(f'  pairs   : {len(pairs)}')
    print(bar)

    n_ok = 0
    n_skip = 0
    t0 = time.time()

    for left_name, right_name in pairs:
        left, err_l = _load_instance(input_dir, left_name)
        right, err_r = _load_instance(input_dir, right_name)
        if err_l or err_r:
            print(f'  ✗ {left_name} | {right_name}')
            if err_l:
                print(f'      {err_l}')
            if err_r:
                print(f'      {err_r}')
            n_skip += 1
            continue

        pair_stem = f'BKS_{left_name}_{right_name}_combined'
        out_base = os.path.join(output_dir, pair_stem)
        plot_pair(left, right, out_base, formats=tuple(formats))
        tags = ' '.join(e.lstrip('.').upper() for e in formats)
        print(
            f'  ✓ {left_name:<12} | {right_name:<12}  {tags:<8}  '
            f'cost={_fmt_cost(left["cost"])} / {_fmt_cost(right["cost"])}'
        )
        n_ok += 1

    elapsed = time.time() - t0
    print()
    print(bar)
    print(f'  done   ✓ {n_ok} pairs   ✗ {n_skip} skipped   {elapsed:.1f}s')
    print(f'  output → {output_dir}')
    print(bar)
    print()


if __name__ == '__main__':
    main()
