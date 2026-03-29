import os
import csv
import subprocess

# --- Configuration ---
BIN_DIR = "./Bin"
INPUTS_DIR = "Inputs-bench"
REFERENCE_CSV = "Outputs/Outputs.csv"
RHO_VALUE = 5000  
NUM_EXECUTIONS = 3  

# Mapping of executables to the column names
VARIANT_MAP = {
    "BPMDS(Custom_MinHeap+Lazy_DFS)": "bucket-partitioned-MDS",
    "CPP_Set": "bucket-partitioned-MDS-set",
    "Non_Lazy_DFS": "bucket-partitioned-MDS-dfs"
}

# Ordered list of columns for the output CSVs
COLUMNS = ["instance name", "size category", "BPMDS(Custom_MinHeap+Lazy_DFS)", "CPP_Set", "Non_Lazy_DFS"]

TIME_CSV = "benchmark_execution_times.csv"
MEM_CSV = "benchmark_memory_usage.csv"

def load_best_alphas(csv_path):
    """Loads optimal alpha for each instance from the provided Outputs.csv."""
    best_alphas = {}
    if not os.path.exists(csv_path):
        print("Error: Reference CSV not found.")
        return best_alphas

    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            instance = row['input'].strip()
            alpha = float(row['alpha'])
            cost = float(row['cost'])
            if instance not in best_alphas or cost < best_alphas[instance]['cost']:
                best_alphas[instance] = {'alpha': alpha, 'cost': cost}
    return best_alphas

def parse_metrics(file_path):
    """Parses the temporary output file created by the C++ solver."""
    ex_time, memory = "N/A", "N/A"
    if not os.path.exists(file_path):
        return ex_time, memory

    with open(file_path, 'r') as f:
        for line in f:
            if "Execution time" in line:
                ex_time = line.split()[-1]
            elif "Maximum memory" in line:
                memory = line.split()[-1]
    return ex_time, memory

def main():
    print("Initializing benchmark for variants...")
    best_alphas = load_best_alphas(REFERENCE_CSV)
    
    # Open both files in 'w' mode to write headers initially
    for csv_file in [TIME_CSV, MEM_CSV]:
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=COLUMNS)
            writer.writeheader()

    # Walk through Inputs-bench/
    for root, dirs, files in os.walk(INPUTS_DIR):
        category = os.path.basename(root)
        
        for file in files:
            if file.endswith(".vrp"):
                input_path = os.path.join(root, file)
                instance_base = file.replace('.vrp', '')
                
                if instance_base not in best_alphas:
                    print(f"Skipping {file}: No alpha found in reference.")
                    continue
                
                alpha = best_alphas[instance_base]['alpha']
                print(f"Benchmarking {file} (Category: {category}, Alpha: {alpha})")

                # Prepare result rows for this specific instance
                t_row = {"instance name": file, "size category": category}
                m_row = {"instance name": file, "size category": category}

                for col_name, exe_name in VARIANT_MAP.items():
                    binary = os.path.join(BIN_DIR, exe_name)
                    temp_out = f"temp_out.txt"
                    
                    cmd = [
                        binary,
                        f"--alpha={alpha}",
                        f"--rho={RHO_VALUE}",
                        f"--input={input_path}",
                        f"--output={temp_out}"
                    ]
                    
                    sum_t = 0.0
                    sum_m = 0.0
                    success_runs = 0

                    for _ in range(NUM_EXECUTIONS):
                        try:
                            subprocess.run(
                                cmd, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE, 
                                universal_newlines=True, 
                                check=True
                            )
                            
                            t, m = parse_metrics(temp_out)
                            if t != "N/A" and m != "N/A":
                                sum_t += float(t)
                                sum_m += float(m)
                                success_runs += 1
                                
                        except Exception as e:
                            print(f"Error with {col_name} on {file}: {e}")
                    
                    if success_runs == NUM_EXECUTIONS:
                        t_row[col_name] = f"{sum_t / NUM_EXECUTIONS:.6f}"
                        m_row[col_name] = f"{sum_m / NUM_EXECUTIONS:.6f}"
                    else:
                        t_row[col_name] = "ERROR"
                        m_row[col_name] = "ERROR"
                
                # Append the completed row to the CSV files
                with open(TIME_CSV, 'a', newline='') as tf, open(MEM_CSV, 'a', newline='') as mf:
                    t_writer = csv.DictWriter(tf, fieldnames=COLUMNS)
                    m_writer = csv.DictWriter(mf, fieldnames=COLUMNS)
                    
                    t_writer.writerow(t_row)
                    m_writer.writerow(m_row)
                    
                    # Ensure data is physically written to disk
                    tf.flush()
                    mf.flush()

    print(f"\nAll variants benchmarked successfully.")
    print(f"Times saved to: {TIME_CSV}")
    print(f"Memory saved to: {MEM_CSV}")

if __name__ == "__main__":
    main()
