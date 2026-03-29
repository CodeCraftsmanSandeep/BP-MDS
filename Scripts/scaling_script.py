import os
import re
import subprocess
import csv

# --- Configuration ---
INPUTS_DIR = "Inputs-bench"
OUTPUTS_CSV = "Outputs/Outputs.csv"
SCALING_OUT_DIR = "Scaling_Outputs"
EXECUTABLE = "./Bin/bucket-partitioned-MDS"
RUNS_PER_THREAD = 3
THREAD_COUNTS = [1, 2, 4, 8, 16, 32, 40]

def load_optimal_parameters():
    """Loads Outputs.csv using the built-in csv module."""
    lookup = {}
    try:
        with open(OUTPUTS_CSV, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            headers = [h.strip() for h in reader.fieldnames]
            reader.fieldnames = headers

            for row in reader:
                instance_name = str(row['input']).strip()
                alpha = float(row['alpha'])
                if 'rho' in headers and row['rho'].strip():
                    rho = int(float(row['rho'])) 
                else:
                    rho = 5000
                lookup[instance_name] = {'alpha': alpha, 'rho': rho}
                
        print(f"Loaded optimal parameters for {len(lookup)} instances.")
        return lookup
    except FileNotFoundError:
        print(f"Error: {OUTPUTS_CSV} not found.")
        return None
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None

def extract_time(output_text):
    """Uses Regex to find the exact execution time from the C++ console output."""
    match = re.search(r"Execution time for solving \(sec\):\s*([0-9.]+)", output_text)
    if match:
        return float(match.group(1))
    return None

def main():
    lookup = load_optimal_parameters()
    if not lookup:
        return

    os.makedirs(SCALING_OUT_DIR, exist_ok=True)

    env = os.environ.copy()
    env['OMP_PLACES'] = 'cores'
    env['OMP_PROC_BIND'] = 'close'

    print(f"\nStarting Automated BP_MDS Scaling Pipeline...")
    print(f"Results will be saved to: ./{SCALING_OUT_DIR}/<filename>.csv")
    print("="*60)

    for root, dirs, files in os.walk(INPUTS_DIR):
        for file in files:
            if file.endswith('.vrp'):
                filepath = os.path.join(root, file)
                base_name = file.replace('.vrp', '')

                match_name = None
                if base_name in lookup:
                    match_name = base_name
                else:
                    for k in lookup.keys():
                        if base_name.startswith(k) or k.startswith(base_name):
                            match_name = k
                            break
                
                if not match_name:
                    continue 

                params = lookup[match_name]
                alpha_val = params['alpha']
                rho_val = params['rho']

                print(f"\nBenchmarking: {file}")
                
                out_csv_path = os.path.join(SCALING_OUT_DIR, f"{base_name}.csv")
                with open(out_csv_path, 'w', newline='', encoding='utf-8') as f:
                    f.write("Threads,Avg_Time_Sec,Speedup,Efficiency\n")

                baseline_time = 0.0

                for threads in THREAD_COUNTS:
                    env['OMP_NUM_THREADS'] = str(threads)
                    total_time = 0.0
                    success = True

                    for run in range(RUNS_PER_THREAD):
                        cmd = [
                            EXECUTABLE, 
                            f"--input={filepath}", 
                            f"--alpha={alpha_val}", 
                            f"--rho={rho_val}"
                        ]
                        
                        # ---> THE PYTHON 3.6 FIX IS HERE <---
                        result = subprocess.run(
                            cmd, 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE, 
                            universal_newlines=True, 
                            env=env
                        )
                        
                        time_sec = extract_time(result.stdout)
                        
                        if time_sec is None:
                            print(f"\nERROR parsing output on {threads} threads for {file}.")
                            print("Raw Output:\n", result.stdout)
                            success = False
                            break
                        
                        total_time += time_sec

                    if not success:
                        break 

                    avg_time = total_time / RUNS_PER_THREAD
                    
                    if threads == 1:
                        baseline_time = avg_time
                        speedup = 1.0
                        efficiency = 1.0
                    else:
                        speedup = baseline_time / avg_time if avg_time > 0 else 0
                        efficiency = speedup / threads

                    print(f"   [{threads:2d} Threads] Time: {avg_time:8.4f}s | Speedup: {speedup:6.2f}x | Eff: {efficiency:.2f}")

                    with open(out_csv_path, 'a', newline='', encoding='utf-8') as f:
                        f.write(f"{threads},{avg_time:.4f},{speedup:.4f},{efficiency:.4f}\n")

    print("\n" + "="*60)
    print(f"Full pipeline complete! All individual CSVs are safely stored in '{SCALING_OUT_DIR}/'.")

if __name__ == "__main__":
    main()
