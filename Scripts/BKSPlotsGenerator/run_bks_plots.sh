#!/usr/bin/env bash
# Run RoutesPlotter + RoutesPlotterCombined with the project venv.
#
# Usage (from repo root):
#   bash Scripts/BKSPlotsGenerator/run_bks_plots.sh
#   bash Scripts/BKSPlotsGenerator/run_bks_plots.sh --pdf
#   bash Scripts/BKSPlotsGenerator/run_bks_plots.sh --pdf --html
#
# Outputs:
#   Results/BKSPlots/separated/   — individual plots (mirrors Inputs/ tree)
#   Results/BKSPlots/combined/    — side-by-side AGS pair plots
#
# Separated input:  Inputs/          (all .vrp+.sol under Inputs)
# Combined input:   Inputs/CVRPLIB/AGS
#
# Flag routing:
#   --pdf     → both scripts
#   --html    → RoutesPlotter only (combined has no HTML)
#   --legend  → RoutesPlotter only
#   --pairs   → RoutesPlotterCombined only (value required)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
cd "${REPO_ROOT}"

INDIV_FLAGS=()
COMBINED_FLAGS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --pdf)
      INDIV_FLAGS+=(--pdf)
      COMBINED_FLAGS+=(--pdf)
      shift
      ;;
    --html|--legend)
      INDIV_FLAGS+=("$1")
      shift
      ;;
    --pairs)
      if [[ $# -lt 2 ]]; then
        echo "ERROR: --pairs needs a value (e.g. Antwerp1,Antwerp2)" >&2
        exit 2
      fi
      COMBINED_FLAGS+=(--pairs "$2")
      shift 2
      ;;
    -h|--help)
      sed -n '2,20p' "$0"
      exit 0
      ;;
    *)
      echo "ERROR: unknown flag: $1" >&2
      echo "Supported: --pdf  --html  --legend  --pairs <a,b;c,d>" >&2
      exit 2
      ;;
  esac
done

VENV_DIR="${REPO_ROOT}/.venv"
if [[ ! -d "${VENV_DIR}" ]]; then
  echo "Creating venv at ${VENV_DIR} ..."
  python3 -m venv "${VENV_DIR}"
fi

# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"

pip install -q -r Scripts/requirements.txt

INPUT_ALL="Inputs"
INPUT_AGS="Inputs/CVRPLIB/AGS"
SEPARATED_OUT="Results/BKSPlots/separated"
COMBINED_OUT="Results/BKSPlots/combined"

echo
echo "==> RoutesPlotter (separated)  ${INPUT_ALL} → ${SEPARATED_OUT}"
echo "    (mirrors Inputs/ folder layout under separated/)"
python Scripts/BKSPlotsGenerator/RoutesPlotter.py \
  "${INPUT_ALL}" \
  "${SEPARATED_OUT}" \
  "${INDIV_FLAGS[@]+"${INDIV_FLAGS[@]}"}"

echo
echo "==> RoutesPlotterCombined (combined)  ${INPUT_AGS} → ${COMBINED_OUT}"
python Scripts/BKSPlotsGenerator/RoutesPlotterCombined.py \
  "${INPUT_AGS}" \
  "${COMBINED_OUT}" \
  "${COMBINED_FLAGS[@]+"${COMBINED_FLAGS[@]}"}"

deactivate
echo
echo "Done. venv deactivated."
echo "  separated → ${SEPARATED_OUT}"
echo "  combined  → ${COMBINED_OUT}"
