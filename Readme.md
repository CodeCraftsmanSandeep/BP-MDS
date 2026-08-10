# BP-MDS: Bucket-Partitioned MDS CVRP Solver (Million Scale)

![2-D partitions](Results/2-d-partitions-refined/2-d-partitions-refined.png)

Parallel **Bucket-Partitioned Minimum-Degree Search** for the Capacitated Vehicle Routing Problem (CVRP), built to handle million-customer instances.

The plane is partitioned into angular buckets from the depot (angle **α**). Each bucket is solved via an MST plus **ρ** randomized DFS iterations, with buckets processed in parallel (OpenMP).

---

## Platforms

| Platform | Build / run | Notes |
|:---------|:------------|:------|
| **Linux** | Supported (recommended) | Cluster target. OpenMP + memory stats (`/proc`, `getrusage`) work as intended. |
| **macOS** | Works for local runs | Use Homebrew GCC: `make CXX=g++-15` (Apple Clang has no `-fopenmp`). Solve/cost/routes OK; expect a harmless `/proc/self/status` warning; **MB line in `.sol` is unreliable**. |
| **Windows** | Not supported natively | No `/proc` / Unix `getrusage` as used here; Makefile is Unix/GCC-oriented. Use **WSL** (Ubuntu) and follow the Linux instructions. |

---

## Quick start

**Needs:** C++17 + OpenMP.

```bash
# Build (macOS: make CXX=g++-15)
make

# Run on the tiny sample instance
mkdir -p Results/Output/Sample
./Bin/bucket-partitioned-MDS \
  --alpha=30 \
  --rho=100 \
  --input=Inputs/Sample/toy.vrp \
  --output=Results/Output/Sample/toy.sol
```

Solution is written to `Results/Output/Sample/toy.sol` (cost + routes).

| Flag | Meaning |
|:-----|:--------|
| `--alpha` | Partition angle (degrees, `0 < α ≤ 360`) |
| `--rho` | Number of randomized DFS iterations |
| `--input` | Path to a `.vrp` instance |
| `--output` | Path for the solution file |

---

## Plot routes (BKS figures)

From the repo root, one command sets up the venv and generates the plots:

```bash
bash Scripts/BKSPlotsGenerator/run_bks_plots.sh --pdf --html
```

That writes:

- `Results/BKSPlots/separated/` — individual plots for **all** of `Inputs/` (same folder layout, e.g. `separated/CVRPLIB/AGS/BKS_Antwerp1_routes.png`)
- `Results/BKSPlots/combined/` — side-by-side AGS pairs (`BKS_*_combined.png` / `.pdf`)

PNG-only: omit the flags (`bash Scripts/BKSPlotsGenerator/run_bks_plots.sh`).  
`--html` applies only to separated plots; `--pdf` applies to both.

For manual / advanced usage, see [`Scripts/BKSPlotsGenerator/`](Scripts/BKSPlotsGenerator/).

---

## Project structure

```text
.
├── Src/Main.cpp              # Entry point
├── Include/                  # Headers
├── Lib/                      # Implementation
│   ├── Bucket_Partitioned_MDS/
│   ├── Utils/
│   ├── Command_Line_Args.cpp
│   └── Initializer.cpp
├── Inputs/                   # Catalog + Sample; full sets via Releases
│   ├── Sample/               # Tiny toys for local checks
│   ├── instances.csv
│   └── README.md             # CVRPLIB / FILO2 / Synthetic via GitHub Releases
├── Results/                  # Figures & result artifacts
├── Scripts/                  # Benchmark / plot / generation tools
└── Makefile
```

---

## Build

```bash
make              # Linux
make CXX=g++-15   # macOS (Homebrew GCC; Apple clang lacks -fopenmp)
# → Bin/bucket-partitioned-MDS
```

Ablation / benchmarking solvers (`-set`, `-dfs`, BFS, buckets) live under `Results/ExperimentalEvaluation/Code/` and are built from **BPMDS_Scripts**, not this Makefile.

---

## More detail

- Instance catalog & BKS: [`Inputs/README.md`](Inputs/README.md)
- Pipeline / scaling / ρ sweeps: [`Scripts/`](Scripts/)
- Route plots: [`Scripts/BKSPlotsGenerator/run_bks_plots.sh`](Scripts/BKSPlotsGenerator/run_bks_plots.sh)
