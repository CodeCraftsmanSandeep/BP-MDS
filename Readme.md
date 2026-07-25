# BP-MDS: Bucket-Partitioned MDS CVRP Solver (Million Scale)

![2-D partitions](Results/2-d-partitions-refined/2-d-partitions-refined.png)

Parallel **Bucket-Partitioned Minimum-Degree Search** for the Capacitated Vehicle Routing Problem (CVRP), built to handle million-customer instances.

The plane is partitioned into angular buckets from the depot (angle **α**). Each bucket is solved via an MST plus **ρ** randomized DFS iterations, with buckets processed in parallel (OpenMP).

---

## Quick start

**Needs:** C++17 compiler with OpenMP.

```bash
make

./Bin/bucket-partitioned-MDS \
  --alpha=30 \
  --rho=100 \
  --input=Inputs/Sample/toy.vrp \
  --output=solution.sol
```

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
├── Inputs/                   # Instances + BKS solutions
│   ├── CVRPLIB/              # CMT, Golden, X, AGS
│   ├── FILO2/I/              # Large Italian regions
│   ├── Synthetic/            # XML-style generated instances
│   ├── Sample/               # Tiny toys for local checks
│   ├── instances.csv
│   └── README.md
├── Results/                  # Figures & result artifacts
├── Scripts/                  # Benchmark / plot / generation tools
└── Makefile
```

---

## Build targets

| Binary | Role |
|:-------|:-----|
| `Bin/bucket-partitioned-MDS` | Main solver (custom min-heap + lazy DFS) |
| `Bin/bucket-partitioned-MDS-set` | Baseline using `std::set` for MST |
| `Bin/bucket-partitioned-MDS-dfs` | Non-lazy DFS variant |

---

## More detail

- Instance catalog & BKS: [`Inputs/README.md`](Inputs/README.md)
- Pipeline / scaling / ρ sweeps: [`Scripts/`](Scripts/)
- Route plots: [`Scripts/BKSPlotsGenerator/run_bks_plots.sh`](Scripts/BKSPlotsGenerator/run_bks_plots.sh)
