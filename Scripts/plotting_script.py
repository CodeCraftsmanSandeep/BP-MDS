import os
import glob
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter, MaxNLocator
from numpy.polynomial import Polynomial

# ==========================================
# 0. Global Helper for Publication Theme
# ==========================================
os.makedirs('./Plots', exist_ok=True)

def setup_style(style="ticks", font_size=14, labelsize=14, titlesize=15, 
                xtick=12, ytick=12, dpi=600, extra_rc=None):
    """Sets standard academic rcParams cleanly across all functions."""
    plt.style.use('default')
    sns.set_theme(style=style)
    rc = {
        'font.family': 'serif',
        'mathtext.fontset': 'stix',
        'font.size': font_size,
        'axes.labelsize': labelsize,
        'axes.titlesize': titlesize,
        'xtick.labelsize': xtick,
        'ytick.labelsize': ytick,
        'figure.dpi': dpi,
        'axes.edgecolor': 'black',
        'axes.linewidth': 1.2
    }
    if extra_rc:
        rc.update(extra_rc)
    plt.rcParams.update(rc)


# ==========================================
# 1. Plotting Functions
# ==========================================
def plot_bucket_analysis():
    """Generates bucket size distribution and runtime correlation (1x3 grid)."""
    print("Running plot_bucket_analysis...")
    instances = ['Flanders1', 'Flanders2', 'Brussels1', 'Brussels2']
    all_data = [pd.read_csv(f'./Bucket_metrics/{inst}.csv').assign(Instance=inst) 
                for inst in instances if os.path.exists(f'./Bucket_metrics/{inst}.csv')]
    
    df_all = pd.concat(all_data, ignore_index=True) if all_data else None
    if not all_data:
        print("Warning: No bucket metric files found in ./Bucket_metrics/!")

    # --- KEEP YOUR ORIGINAL STYLE & FIGSIZE HERE ---
    grid_rc = {'axes.grid.axis': 'y', 'grid.linestyle': '--', 'grid.alpha': 0.6, 'grid.color': '#B0B0B0'}
    setup_style(style="whitegrid", font_size=12, labelsize=13.25, titlesize=14.5, xtick=12.5, ytick=11, dpi=300, extra_rc=grid_rc)
    
    # 1. Two-color palette for the histograms (Blue and Orange)
    hist_palette = ["#0486D1", "#FC6E01"]
    
    # 2. Four-color palette for the scatter plot (so all 4 instances are distinguishable)
    palette_4 = ["#0486D1", "#FC6E01", "#1ABF93", "#FFC13B"]
    color_map_scatter = {inst: palette_4[i] for i, inst in enumerate(instances)}
    
    fig, axes = plt.subplots(1, 3, figsize=(16, 3.6)) 

    if df_all is not None:
        df_brussels = df_all[df_all['Instance'].isin(['Brussels1', 'Brussels2'])]
        df_flanders = df_all[df_all['Instance'].isin(['Flanders1', 'Flanders2'])]
        
        # Plot (a): Brussels Distribution (Forced thin bins, Blue/Orange colors)
        sns.histplot(data=df_brussels, x='num_customers', hue='Instance', element='step', fill=True, 
                     alpha=0.6, linewidth=2, stat='count', kde=False, bins=40, palette=hist_palette, ax=axes[0])
        
        # Plot (b): Flanders Distribution (Forced thin bins, Blue/Orange colors)
        sns.histplot(data=df_flanders, x='num_customers', hue='Instance', element='step', fill=True, 
                     alpha=0.6, linewidth=2, stat='count', kde=False, bins=40, palette=hist_palette, ax=axes[1])

        # Plot (c): Scatter plot of Execution Time vs. Bucket Size (All Data, 4 colors)
        sns.scatterplot(data=df_all, x='num_customers', y='execution_time', hue='Instance', 
                        style='Instance', s=85, alpha=1, palette=color_map_scatter, ax=axes[2])

    # Titles and Labels
    axes[0].set(title='(a) Bucket Size Distribution (Brussels)', xlabel='Bucket Size', ylabel='Number of Buckets')
    axes[1].set(title='(b) Bucket Size Distribution (Flanders)', xlabel='Bucket Size', ylabel='Number of Buckets')
    axes[2].set(title='(c) Execution Time vs. Size', xlabel='Bucket Size', ylabel='Execution Time (s)')
    
    # Formatting
    for ax in axes:
        ax.locator_params(axis='x', nbins=4)

    # Legends
    if axes[0].get_legend():
        sns.move_legend(axes[0], title='', loc='upper right', frameon=True, framealpha=0.95, facecolor='white')
    if axes[1].get_legend():
        sns.move_legend(axes[1], title='', loc='upper right', frameon=True, framealpha=0.95, facecolor='white')
    if axes[2].get_legend():
        axes[2].legend(title='', loc='upper left', frameon=True, framealpha=0.95, facecolor='white')

    plt.tight_layout()
    out_pdf = './Plots/Bucket_Analysis.pdf'
    plt.savefig(out_pdf, format='pdf', bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {out_pdf}")

def plot_node_results():
    """Generates optimal alpha, execution time, and peak memory versus customer nodes subplots."""
    print("Running plot_node_results...")
    try:
        df = pd.read_csv('Outputs/Outputs.csv')
    except FileNotFoundError:
        print("Warning: 'Outputs.csv' not found!")
        return

    cvrp_nodes = {
        'Antwerp1': 6000, 'Antwerp2': 7000, 'Brussels1': 15000, 'Brussels2': 16000,
        'Flanders1': 20000, 'Flanders2': 30000, 'Ghent1': 10000, 'Ghent2': 11000,
        'Leuven1': 3000, 'Leuven2': 4000, 'CMT4': 150, 'CMT5': 199,
        'Golden_9': 255, 'Golden_10': 323, 'Golden_11': 399, 'Golden_12': 483,
        'Golden_13': 252, 'Golden_14': 320, 'Golden_15': 396, 'Golden_16': 480,
        'Golden_17': 240, 'Golden_18': 300, 'Golden_19': 360, 'Golden_20': 420
    }

    df['nodes'] = df['input'].map(cvrp_nodes).fillna(df['input'].str.extract(r'XML(\d+)', expand=False).astype(float))
    df_nodes = df.dropna(subset=['nodes']).sort_values('nodes')
    present_sizes = [s for s in ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL'] if s in df_nodes['size'].unique()]

    # =========================================================================
    # CALCULATE SLOPE 'm' (POWER-LAW REGRESSION)
    # =========================================================================
    # Filter for valid execution times (> 0) to prevent log10 math errors
    valid_time_df = df_nodes[df_nodes['time(sec)'] > 0]
    log_x = np.log10(valid_time_df['nodes'])
    log_y = np.log10(valid_time_df['time(sec)'])
    
    # Fit linear polynomial: log(y) = m * log(x) + c_log
    m, c_log = np.polyfit(log_x, log_y, 1)
    c = 10**c_log
    
    print("\n" + "="*45)
    print("EMPIRICAL TIME COMPLEXITY FIT")
    print("="*45)
    print(f"Slope (m)     : {m:.4f}")
    print(f"Intercept (c) : {c:.4e}")
    print(f"Equation      : Time = {c:.4e} * Nodes^{m:.4f}")
    print("="*45 + "\n")

    setup_style(style="ticks", font_size=14, labelsize=14, titlesize=15, xtick=12, ytick=12)
    fig, axes = plt.subplots(1, 3, figsize=(16, 3.8))
    scatter_kws = {'s': 80, 'edgecolor': 'black', 'linewidth': 0.8, 'alpha': 0.8}

    plots = [
        ('time(sec)', '(a) Execution Time vs. Customers', 'Execution Time (s)', True),
        ('max_memory_diff(MB)', '(b) Peak Memory vs. Customers', 'Peak Memory (MB)', False),
        ('alpha', r'(c) Optimal $\alpha$ vs. Customers', r'Optimal $\alpha$ (°)', False)
    ]

    for ax, (y_col, title, ylabel, log_y) in zip(axes, plots):
        sns.scatterplot(ax=ax, data=df_nodes, x='nodes', y=y_col, hue='size', hue_order=present_sizes, palette='viridis', **scatter_kws)
        ax.set_xscale('log')
        if log_y: ax.set_yscale('log')
        ax.set(title=title, xlabel='Number of Customers ($N_{{c}}$)', ylabel=ylabel)
        ax.grid(axis='y', linestyle='--', alpha=0.6)
        ax.minorticks_off()
        if ax.get_legend(): ax.get_legend().remove()

    # =========================================================================
    # PLOT TRENDLINE & ANNOTATION ON SUBPLOT (a)
    # =========================================================================
    # Generate points for the trendline across the x-axis range
    x_trend = np.logspace(np.log10(valid_time_df['nodes'].min()), np.log10(valid_time_df['nodes'].max()), 100)
    y_trend = c * (x_trend ** m)
    
    # Plot the red dashed line
    axes[0].plot(x_trend, y_trend, color='red', linestyle='--', linewidth=2.5, zorder=1, label='Trendline')
    
    # Calculate a specific point on the line for the arrow to point to
    x_arrow_target = np.percentile(valid_time_df['nodes'], 30)
    y_arrow_target = c * (x_arrow_target ** m)

    # Add a text box highlighting the complexity with a straight arrow pointing to the line
    #eq_text = f"Time = ${c:.2e} * N_{{c}}^{{{m:.2f}}}$"
    mantissa, exp = f"{c:.2e}".split('e')
    eq_text = f"Time = ${mantissa} \\times 10^{{{int(exp)}}} \\times N_{{c}}^{{{m:.2f}}}$"
    axes[0].annotate(
        eq_text,
        xy=(x_arrow_target, y_arrow_target),  # Point exactly on the red dashed line
        xycoords='data',                      # Use the actual graph coordinates for the tip
        xytext=(0.05, 0.85),                  # Position of the text box (top left)
        textcoords='axes fraction',           # Keep the text box pinned relative to the axes
        fontsize=13,
        bbox=dict(facecolor='white', edgecolor='#B0B0B0', boxstyle='round,pad=0.4', alpha=0.95),
        arrowprops=dict(
            arrowstyle='-|>',                 # Solid arrow head
            color="#7E7E7E",                  # Dark grey arrow so it doesn't clash with the red line
            linewidth=1.5                     # Removed connectionstyle to make the line straight
        ),
        zorder=5                              # Ensure the arrow and text draw on top of everything
    )

    # =========================================================================
    # LEGEND HANDLING
    # =========================================================================
    handles, labels = axes[0].get_legend_handles_labels()
    
    # Filter out the 'Trendline' from the global top legend to keep it clean
    clean_handles, clean_labels = [], []
    for h, l in zip(handles, labels):
        if l != 'Trendline':
            clean_handles.append(h)
            clean_labels.append(l)

    fig.legend(clean_handles, clean_labels, loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=len(clean_labels),
               frameon=False, fontsize=12.5, title_fontsize=12.5, columnspacing=1.0, handletextpad=0.3)

    plt.tight_layout(pad=0.3, w_pad=1.0, rect=[0, 0, 1, 0.92])
    plt.savefig('./Plots/node_Results.pdf', format='pdf', bbox_inches='tight')
    plt.close(fig)
    print("Saved ./Plots/node_Results.pdf")

def plot_parMDS():
    """Generates Speedup, Memory Efficiency, and Gap Reduction vs ParMDS bar charts."""
    print("Running plot_bar_charts...")
    data = [
        ('CMT4', 'S', 7.28, 0.12, 12.85, 4.99), ('Golden_18', 'S', 4.88, 0.17, 4.97, 10.26),
        ('Golden_19', 'S', 8.09, 0.49, 9.50, 6.15), ('Golden_20', 'S', 11.80, 0.67, 10.65, 4.23),
        ('Avg S', 'S', 7.43, 0.36, 11.15, 9.16), ('Leuven2', 'M', 9.37, 79.52, 14.41, 0.38),
        ('Antwerp1', 'M', 30.20, 14.30, 7.27, 1.31), ('Antwerp2', 'M', 19.44, 153.11, 13.01, 0.41),
        ('Ghent1', 'M', 42.88, 231.30, 7.30, 1.24), ('Avg M', 'M', 27.17, 81.62, 11.01, 0.61),
        ('Ghent2', 'L', 12.65, 387.12, 13.32, 0.80), ('Brussels2', 'L', 19.78, 584.78, 13.45, 0.72),
        ('Flanders2', 'L', 24.41, 1491.93, 11.19, 0.55), ('XML25000_1173_01', 'L', 31.51, 38.88, 9.80, 0),
        ('XML50000_1173_01', 'L', 46.91, 153.12, 12.60, 0), ('Avg L', 'L', 28.35, 705.94, 11.75, 0.59)
    ]

    df = pd.DataFrame(data, columns=['Instance', 'Class', 'Speedup', 'Mem.Eff.', 'Gap(%)', 'Gap Reduced(%)'])
    df_gap = df[~df['Instance'].str.contains('XML')].reset_index(drop=True)
    color_map = {'S': "#0486D1", 'M': "#FC6E01", 'L': "#01B887"}

    setup_style(font_size=14, labelsize=14, titlesize=15, xtick=11.75, ytick=11.75)
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.25))

    format_lbl = lambda l: f"$\\mathbf{{{l.replace(' ', '~')}}}$" if "Avg" in l else l

    charts = [
        (axes[0], df, 'Speedup', 'Speedup (X)', '(a) Speedup vs. ParMDS', False, None),
        (axes[1], df, 'Mem.Eff.', 'Memory Efficiency (X)', '(b) Memory Efficiency vs. ParMDS', True, None),
        (axes[2], df_gap, 'Gap Reduced(%)', 'Gap Reduction (%)', '(c) Gap Reduction vs. ParMDS', False, (0, 12))
    ]

    for ax, data_df, col, ylabel, title, log_y, ylim in charts:
        x = np.arange(len(data_df))
        ax.bar(x, data_df[col], color=data_df['Class'].map(color_map).tolist(), alpha=0.9, edgecolor='black', linewidth=1.0)
        if log_y: ax.set_yscale('log')
        if ylim: ax.set_ylim(*ylim)
        ax.set(ylabel=ylabel, title=title)
        ax.set_xticks(x)
        ax.set_xticklabels([format_lbl(l) for l in data_df['Instance']], rotation=35, ha='right')
        ax.minorticks_off()
        ax.grid(axis='y', linestyle='--', alpha=0.6)
        ax.set_axisbelow(True)

    legend_elements = [Patch(facecolor=color_map[k], edgecolor='black', label=k) for k in color_map]
    fig.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, frameon=False, fontsize=14, columnspacing=2.0)

    plt.tight_layout(pad=0.5, w_pad=1.5, rect=[0, 0, 1, 0.95])
    out_path = './Plots/parMDS.pdf'
    plt.savefig(out_path, format='pdf', bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {out_path}")

def plot_ablation_analysis():
    """Generates execution time, peak memory, and DFS vs BFS gap comparisons (1x3 grid)."""
    print("Running plot_ablation_analysis...")
    try:
        df_time = pd.read_csv('benchmark_execution_times.csv')
        df_mem = pd.read_csv('benchmary_memory_usage.csv')
    except FileNotFoundError:
        print("Warning: Benchmark CSVs not found!")
        return

    cat_order = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']
    instances = ['CMT4', 'Antwerp2', 'Brussels2', 'Flanders2', 'XML500000_1173_01', 'XML2000000_1173_01', 'XML2000000_3161_01']

    for df_curr in (df_time, df_mem):
        df_curr['size category'] = pd.Categorical(df_curr['size category'], categories=cat_order, ordered=True)
        df_curr['instance_clean'] = df_curr['instance name'].str.replace('.vrp', '', regex=False)

    df_time = df_time[df_time['instance_clean'].isin(instances)].sort_values(by=['size category', 'BPMDS(Custom_MinHeap+Lazy_DFS)'])
    df_mem = df_mem[df_mem['instance_clean'].isin(instances)].sort_values(by=['size category', 'BPMDS(Custom_MinHeap+Lazy_DFS)'])

    x_labels = df_time['instance_clean'].tolist()
    x, width = np.arange(len(x_labels)), 0.25

    # --- NEW: BFS GAP DATA LOADING ---
    df_melt = None
    gaps_csv_path = 'BFS_Gaps.csv'
    if os.path.exists(gaps_csv_path):
        df_gaps = pd.read_csv(gaps_csv_path)
        df_melt = df_gaps.melt(id_vars=['input', 'size'], value_vars=['Gap_DFS(%)', 'Gap_BFS(%)'], 
                               var_name='Strategy', value_name='Gap')
        df_melt['Strategy'] = df_melt['Strategy'].map({'Gap_DFS(%)': 'DFS', 'Gap_BFS(%)': 'BFS'})

    # --- KEEP YOUR ORIGINAL STYLE HERE ---
    grid_rc = {'legend.fontsize': 11, 'hatch.color': "#FFFFFF", 'hatch.linewidth': 0.1, 
               'axes.grid.axis': 'y', 'grid.linestyle': '--', 'grid.alpha': 0.6, 'grid.color': '#B0B0B0'}
    setup_style(font_size=14, labelsize=14, titlesize=15, xtick=12, ytick=12, extra_rc=grid_rc)

    # Note: Adjust the 24 to match whatever ratio your original 1x2 grid used! (e.g. if 1x2 was 16 wide, 1x3 should be 24 wide).
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.2)) 
    
    sub_data = [
        (axes[0], df_time, 'Execution Time (s)', '(a) Execution Time Comparison', (0.01, 4500)),
        (axes[1], df_mem, 'Peak Memory (MB)', '(b) Peak Memory Comparison',  (0.1, 30000))
    ]

    # Plot Panel (a) and (b)
    for ax, df_curr, ylabel, title, ylim in sub_data:
        ax.bar(x - width, df_curr['BPMDS(Custom_MinHeap+Lazy_DFS)'], width, label='BP-MDS (Custom MinHeap + Lazy DFS)', color='#0486D1', edgecolor='black', alpha=0.9)
        ax.bar(x, df_curr['CPP_Set'], width, label='CPP STL Set', color='#FC6E01', edgecolor='black', alpha=0.9)
        ax.bar(x + width, df_curr['Non_Lazy_DFS'], width, label='Non-Lazy DFS', color='#01B887', edgecolor='black', alpha=0.9)
        
        ax.set_yscale('log')
        ax.set_ylabel(ylabel)
        if ylim: ax.set_ylim(*ylim)
        ax.yaxis.set_minor_locator(ticker.NullLocator())
        ax.set_xticks(x)
        ax.set_xticklabels(x_labels, rotation=22.5, ha='right')
        ax.grid(True, axis='y', linestyle='--', alpha=0.6)
        ax.set_axisbelow(True)
        ax.legend(loc='upper left', frameon=False)
        ax.set_title(title, pad=10)

    # --- NEW: Plot Panel (c) Gap Analysis ---
    if df_melt is not None:
        sns.barplot(data=df_melt, x='input', y='Gap', hue='Strategy', palette=["#0486D1", "#FC6E01"], 
                    saturation=1, edgecolor='black', linewidth=1, alpha=0.9, ax=axes[2])
        axes[2].set(title='(c) Gap to BKS(%): DFS vs. BFS', xlabel='', ylabel='Gap to BKS (%)')
        axes[2].set_xticks(axes[2].get_xticks())
        axes[2].set_xticklabels(axes[2].get_xticklabels(), rotation=22.5, ha='right', rotation_mode='anchor')
        axes[2].legend(title='', loc='upper left', frameon=False, framealpha=1, facecolor='white')
        axes[2].grid(True, axis='y', linestyle='--', alpha=0.6)
        axes[2].set_axisbelow(True)

    plt.tight_layout()
    out_path = './Plots/Combined_Ablation_Analysis_Patterns.pdf'
    fig.savefig(out_path, bbox_inches='tight', dpi=600)
    plt.close(fig)
    print(f"Saved {out_path}")

def plot_alpha_metrics(input_dir="Outputs/XXL", output_dir="Plots/alpha"):
    """Iterates through instance outputs to generate alpha tuning plots."""
    print(f"Running plot_alpha_metrics for {input_dir}...")
    os.makedirs(output_dir, exist_ok=True)
    csv_files = glob.glob(os.path.join(input_dir, "*.csv"))
    
    if not csv_files:
        print(f"Warning: No CSV files found in '{input_dir}' directory.")
        return

    grid_rc = {'axes.grid.axis': 'y', 'grid.linestyle': '--', 'grid.alpha': 0.6, 'grid.color': '#B0B0B0'}
    setup_style(font_size=14, labelsize=15, titlesize=15, xtick=12, ytick=12, extra_rc=grid_rc)

    metrics = [
        ('cost', r'(a) Cost vs. $\alpha$', r'Routing Cost ($\times 10^8$)', '#004488', True),
        ('time(sec)', r'(b) Execution Time vs. $\alpha$', 'Execution Time (s)', '#d62728', False),
        ('max_memory_diff(MB)', r'(c) Peak Memory vs. $\alpha$', 'Peak Memory (MB)', '#2ca02c', False)
    ]

    for file_path in csv_files:
        try:
            instance_name = os.path.basename(file_path).replace('.csv', '')
            df = pd.read_csv(file_path)
            if not {'alpha', 'cost', 'time(sec)', 'max_memory_diff(MB)'}.issubset(df.columns):
                continue

            fig, axes = plt.subplots(1, 3, figsize=(16, 3.5))

            for ax, (col, title, ylabel, color, is_cost) in zip(axes, metrics):
                ax.plot(df['alpha'], df[col], color=color, linewidth=2.0, zorder=3)
                ax.set(title=title, xlabel=r'Partition Angle $\alpha$ (°)', ylabel=ylabel)
                if is_cost:
                    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, pos: f'{y * 1e-8:g}'))

                min_idx = df[col].idxmin()
                best_alpha, best_val = df['alpha'][min_idx], df[col][min_idx]

                ax.axvline(best_alpha, color='black', linewidth=1, alpha=0.6, zorder=1)
                ax.axhline(best_val, color='black', linewidth=1, alpha=0.6, zorder=1)
                ax.scatter(best_alpha, best_val, color='black', s=40, zorder=5)
                ax.annotate(f"({best_alpha:.2f}, {best_val:.2f})", xy=(best_alpha, best_val),
                            xytext=(5, 10), textcoords="offset points", ha='left', va='bottom',
                            rotation=45, color='black', fontsize=11, zorder=10)
                ax.grid(True, axis='y', which='major', linestyle='--', alpha=0.6, zorder=0)
                ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=8))

            plt.tight_layout(pad=0.5, w_pad=1.5)
            save_path = os.path.join(output_dir, f"{instance_name}_metrics.pdf")
            plt.savefig(save_path, format='pdf', bbox_inches='tight') 
            plt.close(fig)
            print(f"Generated strict academic plot: {save_path}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

def plot_parameter_sensitivity():
    """Generates cost gap vs rho, exec time vs rho, and speedup vs threads scaling charts."""
    print("Running plot_parameter_sensitivity...")
    bks_dict = {
        'Outputs_Rho/L/Brussels1.csv': 501719.0, 'Outputs_Rho/L/Brussels2.csv': 345468.0,
        'Outputs_Rho/L/Flanders1.csv': 7240118.0, 'Outputs_Rho/L/Flanders2.csv': 4373244.0
    }

    time_files = [
        'Outputs_Rho/S/Golden_12.csv', 'Outputs_Rho/M/Antwerp1.csv',
        'Outputs_Rho/L/Brussels1.csv', 'Outputs_Rho/XL/XML100000_2173_01.csv',
        'Outputs_Rho/XXXL/XML2000000_1173_01.csv'
    ]

    line_styles = {
        'Outputs_Rho/S/Golden_12.csv': {'color': 'black', 'marker': 's', 'linestyle': '-', 'label': 'Golden12 (S)'},
        'Outputs_Rho/M/Antwerp1.csv': {'color': 'red', 'marker': 'o', 'linestyle': '--', 'label': 'Antwerp1 (M)'},
        'Outputs_Rho/L/Brussels1.csv': {'color': 'blue', 'marker': 'v', 'linestyle': '-', 'label': 'Brussels1 (L)'}, 
        'Outputs_Rho/XL/XML100000_2173_01.csv': {'color': '#2ca02c', 'marker': '*', 'linestyle': '-', 'label': 'XML-100k (XL)'},
        'Outputs_Rho/XXXL/XML2000000_1173_01.csv': {'color': '#9467bd', 'marker': 'd', 'linestyle': '-.', 'label': 'XML-2M (XXXL)'}, 
        'Outputs_Rho/L/Brussels2.csv': {'color': 'red', 'marker': 'o', 'linestyle': '--', 'label': 'Brussels2 (L)'},
        'Outputs_Rho/L/Flanders1.csv': {'color': 'black', 'marker': 's', 'linestyle': '-', 'label': 'Flanders1 (L)'}, 
        'Outputs_Rho/L/Flanders2.csv': {'color': '#9467bd', 'marker': '*', 'linestyle': '-.', 'label': 'Flanders2 (L)'},   
    }

    scaling_instances = {
        'Scaling_Outputs/Golden_12.csv': 'S (484 nodes) Golden_12',
        'Scaling_Outputs/Antwerp1.csv': 'M (6000 nodes) Antwerp1',
        'Scaling_Outputs/Brussels1.csv': 'L (15,000 nodes) Brussels1', 
        'Scaling_Outputs/XML100000_2173_01.csv': 'XL (100,000 nodes)',
        'Scaling_Outputs/XML2000000_1173_01.csv': 'XXXL (2M nodes)'
    }

    scaling_styles = {
        'S (484 nodes) Golden_12': {'color': 'black', 'marker': 's', 'linestyle': '-', 'label': 'Golden12 (S)'},
        'M (6000 nodes) Antwerp1': {'color': 'red', 'marker': 'o', 'linestyle': '--', 'label': 'Antwerp1 (M)'},
        'L (15,000 nodes) Brussels1': {'color': 'blue', 'marker': 'v', 'linestyle': '-', 'label': 'Brussels1 (L)'},
        'XL (100,000 nodes)': {'color': '#2ca02c', 'marker': '*', 'linestyle': '-', 'label': 'XML-100k (XL)'},
        'XXXL (2M nodes)': {'color': '#9467bd', 'marker': 'd', 'linestyle': '-.', 'label': 'XML-2M (XXXL)'} 
    }

    setup_style(font_size=13, labelsize=15, titlesize=15, xtick=12, ytick=12)
    fig, axes = plt.subplots(1, 3, figsize=(16, 3.5))

    # Panel (a): Gap vs Rho
    for filepath, bks_val in bks_dict.items():
        try:
            df_gap = pd.read_csv(filepath).sort_values(by='rho')
            df_gap = df_gap[df_gap['rho'].isin([1, 10, 100, 1000, 10000, 100000, 1000000])]
            st = line_styles[filepath]
            axes[0].plot(df_gap['rho'], ((df_gap['cost'] - bks_val) / bks_val) * 100, 
                         color=st['color'], marker=st['marker'], linestyle=st['linestyle'], 
                         linewidth=1.5, markersize=5, markeredgecolor='black', label=st['label'])
        except Exception: pass

    axes[0].set(title=r'(a) Gap vs. $\rho$', xlabel=r'Exploration Parameter $\rho$', ylabel='Gap to BKS (%)')
    axes[0].set_xscale('log')
    axes[0].set_ylim(4, 23)

    # Panel (b): Exec Time vs Rho
    for filepath in time_files:
        try:
            df_time = pd.read_csv(filepath).sort_values(by='rho')
            df_time = df_time[df_time['rho'].isin([1, 10, 100, 1000, 10000, 100000, 1000000])]
            st = line_styles[filepath]
            axes[1].plot(df_time['rho'], df_time['time(sec)'], color=st['color'], marker=st['marker'], 
                         linestyle=st['linestyle'], linewidth=1.5, markersize=5, markeredgecolor='black', label=st['label'])
        except Exception: pass

    axes[1].set(title=r'(b) Execution Time vs. $\rho$', xlabel=r'Exploration Parameter $\rho$', ylabel='Execution Time (s)')
    axes[1].set_yscale('log')
    axes[1].set_xscale('log')
    axes[1].set_ylim(0.01, 50000)

    for ax in (axes[0], axes[1]):
        ax.minorticks_off()
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        # Removed edgecolor='black' to use default light border
        ax.legend(loc='upper left', fontsize=11, frameon=True, framealpha=0.8, borderpad=0.3, labelspacing=0.2)

    # Panel (c): Speedup vs Threads
    for filepath, label in scaling_instances.items():
        try:
            subset = pd.read_csv(filepath).sort_values(by='Threads')
            st = scaling_styles.get(label, {'color': 'gray', 'marker': 'o', 'linestyle': '-', 'label': label})
            axes[2].plot(subset['Threads'], subset['Speedup'], color=st['color'], marker=st['marker'], 
                         linestyle=st['linestyle'], linewidth=1.5, markersize=5, markeredgecolor='black', label=st['label'])
        except Exception: pass

    x_ticks = [1, 2, 4, 8, 16, 24, 32, 40]
    axes[2].set(title='(c) Speedup vs. Threads', xlabel='Number of Threads', ylabel='Speedup (X)')
    axes[2].set_xlim(0, 42)
    axes[2].set_xticks(x_ticks)
    axes[2].set_xticklabels([str(x) for x in x_ticks])
    axes[2].set_ylim(0, 27)
    axes[2].minorticks_off()
    axes[2].grid(axis='y', linestyle='--', alpha=0.7)
    
    # Removed edgecolor='black' to use default light border
    axes[2].legend(loc='upper left', ncol=2, fontsize=11, frameon=True, framealpha=0.8, columnspacing=0.5, borderpad=0.3, labelspacing=0.2, handletextpad=0.3)

    plt.tight_layout(pad=0.5, w_pad=1.0, h_pad=1.5)
    out_path = './Plots/Parameter_sensitivity.pdf'
    plt.savefig(out_path, format='pdf', bbox_inches='tight')
    plt.close(fig)
    print(f"Generated {out_path}")

def plot_time_characteristics():
    """Generates execution time breakdowns according to route size, depot, and customer distributions."""
    print("Running plot_time_characteristics...")
    try:
        df = pd.read_csv('char.csv')
    except FileNotFoundError:
        print("Warning: csv not found.")
        return

    xml_df = df[df['input'].str.startswith('XML')].copy()
    xml_df[['n', 'depot', 'cust', 'demand', 'route']] = xml_df['input'].str.extract(r'XML(\d+)_(\d)(\d)(\d)(\d)').astype(float)
    xml_df = xml_df.dropna(subset=['n'])
    xml_df['n'] = xml_df['n'].astype(int)

    size_map = {1000: '1K(S)', 10000: '10K(L)', 100000: '100K(XL)', 2000000: '2M(XXXL)'}
    depot_map = {1: 'Random', 2: 'Centered', 3: 'Cornered'}
    cust_map = {1: 'Random', 2: 'Clustered', 3: 'Random-Clustered'}
    demand_map = {2: 'Small, Large Var.', 3: 'Small, Small Var.', 4: 'Large, Large Var.', 
                  5: 'Large, Small Var.', 6: 'Quadrant', 7: 'Few Large, Many Small'}
    route_map = {1: 'Very Short', 2: 'Short', 3: 'Medium', 4: 'Long', 5: 'Very Long', 6: 'Ultra Long'}

    xml_df['Graph Size'] = xml_df['n'].map(size_map)

    setup_style(style="whitegrid", font_size=14, labelsize=14, titlesize=15, xtick=12, ytick=12)
    palette = ["#0486D1", "#FC6E01", "#01B887", "#FFC13B"]  
    hue_order = ['1K(S)', '10K(L)', '100K(XL)', '2M(XXXL)']

    fig, axes = plt.subplots(1, 4, figsize=(16, 4), gridspec_kw={'width_ratios': [6, 3.75, 3.75, 6]})

    configs = [
        (axes[0], xml_df[(xml_df['depot']==2) & (xml_df['cust']==1) & (xml_df['demand']==2)], 'route', route_map, '(a) Average Route Size'),
        (axes[1], xml_df[(xml_df['cust']==1) & (xml_df['demand']==2) & (xml_df['route']==3)], 'depot', depot_map, '(b) Depot Positioning'),
        (axes[2], xml_df[(xml_df['depot']==2) & (xml_df['demand']==2) & (xml_df['route']==3)], 'cust', cust_map, '(c) Customer Positioning'),
        (axes[3], xml_df[(xml_df['depot']==2) & (xml_df['cust']==1) & (xml_df['route']==3)], 'demand', demand_map, '(d) Demand Distribution')
    ]

    for ax, df_subset, col, map_dict, title in configs:
        df_plot = df_subset.copy()
        df_plot[col] = df_plot[col].map(map_dict)
        df_plot['norm_time'] = df_plot.groupby('Graph Size')['time(sec)'].transform(lambda x: x / x.mean())
        x_order = [map_dict[k] for k in sorted(map_dict.keys()) if map_dict[k] in df_plot[col].values]

        sns.barplot(ax=ax, data=df_plot, x=col, y='norm_time', hue='Graph Size', hue_order=hue_order,
                    order=x_order, palette=palette, edgecolor='black', linewidth=1, errorbar=None, saturation=1, alpha=0.9)
        
        ax.set(title=title, ylabel='Relative Time' if ax == axes[0] else '', xlabel='')
        ax.axhline(1.0, color='red', linestyle='--', linewidth=1, alpha=0.6)
        ax.set_xticks(range(len(x_order)))
        ax.set_xticklabels(x_order, rotation=20, ha='right', rotation_mode='anchor')
        if ax.get_legend(): ax.get_legend().remove()

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 0.99), ncol=4, frameon=False, fontsize=15, columnspacing=3.0, handletextpad=0.5)

    plt.tight_layout(w_pad=0.3, rect=[0, 0, 1, 0.90])
    plt.subplots_adjust(wspace=0.2, top=0.77)
    out_path = './Plots/time_plot.pdf'
    plt.savefig(out_path, format='pdf', bbox_inches='tight')
    plt.close(fig)
    print(f"Generated {out_path}")


# ==========================================
# 2. Execution Entry Point
# ==========================================

if __name__ == "__main__":
    print("Beginning artifact plot generation...")
    
    # Toggle individual function calls on/off as needed:
    plot_bucket_analysis()
    plot_node_results()
    plot_parMDS()
    plot_ablation_analysis()
    plot_alpha_metrics(input_dir="Outputs/XXL", output_dir="Plots/alpha")
    plot_parameter_sensitivity()
    plot_time_characteristics()
    
    print("All configured artifact plots have been processed!")