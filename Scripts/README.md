# Scripts

Helper scripts for inputs, benchmarks, and BKS route plots.

## BKS route plots (quick)

From the **repo root**:

```bash
bash Scripts/BKSPlotsGenerator/run_bks_plots.sh --pdf --html
```

Creates/activates `.venv`, installs deps, runs both plotters, then deactivates.

| Output | Contents |
|:-------|:---------|
| `Results/BKSPlots/separated/` | Individual plots for all of `Inputs/` (mirrored layout) |
| `Results/BKSPlots/combined/` | Side-by-side AGS pair plots |

PNG only: `bash Scripts/BKSPlotsGenerator/run_bks_plots.sh`  
`--html` → separated only; `--pdf` → both.

### Manual plotters

```bash
python Scripts/BKSPlotsGenerator/RoutesPlotter.py \
  Inputs Results/BKSPlots/separated --pdf --html

python Scripts/BKSPlotsGenerator/RoutesPlotterCombined.py \
  Inputs/CVRPLIB/AGS Results/BKSPlots/combined --pdf
```

## OutputParser.py

```bash
python Scripts/BKSPlotsGenerator/OutputParser.py --vrp_file path.vrp --exe_out path.exe_sol
```

## BatchSolver.py

```bash
python Scripts/BKSPlotsGenerator/BatchSolver.py \
  --input_dir path_to_vrps \
  --exe path_to_solver \
  --output_dir path_to_output
```

## ParamBatchSolver.py

```bash
python Scripts/BKSPlotsGenerator/ParamBatchSolver.py \
  --input_dir path_to_vrps \
  --exe path_to_solver \
  --output_dir path_to_output \
  --alpha={10,20,30} --rho={1,10}
```

## More

- Instance generation: [`Inputs-generation/`](Inputs-generation/)
- Instance catalog: [`../Inputs/README.md`](../Inputs/README.md)
