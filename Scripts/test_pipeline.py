import os
import subprocess
import csv
import glob
import re

def compile_binaries():
    print("\n" + "="*60)
    print(">>> COMPILING C++ BINARIES FOR AQUA")
    print("="*60)
    try:
        # First, wipe old binaries
        subprocess.run(["make", "clean"], check=True)
        # Then, build all targets
        subprocess.run(["make"], check=True)
        print("\nAll binaries compiled successfully and placed in ./Bin/")
    except subprocess.CalledProcessError as e:
        print(f"\nCompilation failed! Exiting pipeline. Error: {e}")
        exit(1)

# ==============================================================================
# STEP 0: FAST TRACK (Recalibrate P100 Data for Aqua for best alpha and rho values)
# ==============================================================================
def step0_fast_track():
    print("\n" + "="*60)
    print(">>> EXECUTING FAST TRACK: Recalibrating Time & Mem from Old_Outputs.csv")
    print("="*60)

    OLD_CSV = "Old_Outputs.csv" 
    NEW_CSV = "Outputs/Outputs.csv"
    INPUTS_DIR = "Inputs-all"  
    EXECUTABLE = "./Bin/bucket-partitioned-MDS"
    NUM_EXECUTIONS = 5 

    if not os.path.exists(OLD_CSV):
        print(f"Error: '{OLD_CSV}' not found! Skipping Fast Track.")
        return

    # Safely handle directory creation if NEW_CSV includes a path
    new_csv_dir = os.path.dirname(NEW_CSV)
    if new_csv_dir:
        os.makedirs(new_csv_dir, exist_ok=True)

    # 1. Load the P100 optimal parameters
    tasks = []
    with open(OLD_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = [h.strip() for h in reader.fieldnames]
        reader.fieldnames = headers
        
        for row in reader:
            input_name = row['input'].strip()
            if not input_name.endswith('.vrp'):
                input_name += '.vrp'
            
            alpha = float(row['alpha'])
            rho = int(float(row['rho'])) if 'rho' in row else 5000
            size = row['size'] if 'size' in row else 'UNKNOWN'
            tasks.append({'file': input_name, 'alpha': alpha, 'rho': rho, 'size': size})

    # 2. Map filenames to paths in Inputs directory
    print(f"🔍 Mapping files to paths in {INPUTS_DIR}...")
    file_map = {}
    for root, _, files in os.walk(INPUTS_DIR):
        for file in files:
            if file.endswith('.vrp'):
                file_map[file] = os.path.join(root, file)

    # 3. Execute and recalibrate
    with open(NEW_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["size", "input", "alpha", "rho", "time(sec)", "max_memory_diff(MB)", "cost"])
        
        for task in tasks:
            file_name = task['file']
            if file_name not in file_map:
                continue
            
            input_path = file_map[file_name]
            alpha = task['alpha']
            rho = task['rho']
            base_name = file_name.replace('.vrp', '')
            
            print(f"Fast-Tracking: {base_name} (Alpha: {alpha}, Rho: {rho})")
            
            sum_time = 0.0
            sum_mem = 0.0
            sum_cost = 0.0
            success_runs = 0
            
            for _ in range(NUM_EXECUTIONS):
                temp_output = "local_temp_output.txt"
                cmd = [
                    EXECUTABLE,
                    f"--alpha={alpha}",
                    f"--rho={rho}",
                    f"--input={input_path}",
                    f"--output={temp_output}"
                ]
                
                try:
                    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
                    with open(temp_output, 'r') as tf:
                        content = tf.read()
                        ex_time = float(next((l.split()[-1] for l in content.split('\n') if "Execution time" in l), 0))
                        memory = float(next((l.split()[-1] for l in content.split('\n') if "Maximum memory" in l), 0))
                        cost = float(next((l.split()[-1] for l in content.split('\n') if "Cost:" in l), 0))
                        
                        sum_time += ex_time
                        sum_mem += memory
                        sum_cost += cost
                        success_runs += 1
                except Exception:
                    pass
            
            if success_runs == NUM_EXECUTIONS:
                avg_time = sum_time / NUM_EXECUTIONS
                avg_mem = sum_mem / NUM_EXECUTIONS
                avg_cost = sum_cost / NUM_EXECUTIONS
                writer.writerow([task['size'], base_name, alpha, rho, f"{avg_time:.6f}", f"{avg_mem:.6f}", f"{avg_cost:.6f}"])
            else:
                writer.writerow([task['size'], base_name, alpha, rho, "ERROR", "ERROR", "ERROR"])
            
            # This instantly writes the row to the disk
            f.flush()
            
    if os.path.exists("local_temp_output.txt"):
        os.remove("local_temp_output.txt")
    print(f"\nFast track complete! Fresh Aqua metrics saved to '{NEW_CSV}'")

# ==============================================================================
# STEP 1: script.py (Run across various values of alpha and save reults in Outputs directory)
# ==============================================================================
def step1_script():
    print("\n" + "="*60)
    print(">>> EXECUTING STEP 1: Parameter Sweeping (script.py)")
    print("="*60)

    num_executions = 5
    rho_values = [10000]

    inputs_dir      = "Inputs"
    output_base_dir = "Outputs"
    binary_path     = "./Bin/bucket-partitioned-MDS"

    # Size categories
    SMALL_SIZES = ["S","M","L","XS"]
    LARGE_SIZES = ["XL","XXL","XXXL"]

    # Ensure output base dir
    os.makedirs(output_base_dir, exist_ok=True)

    for root, _, files in os.walk(inputs_dir):
        # Skip root folder "Inputs"
        if root == inputs_dir:
            continue

        # Detect first folder after Inputs/
        relative = os.path.relpath(root, inputs_dir)
        first_folder = relative.split(os.sep)[0]

        # Determine alpha range
        if first_folder == "XS":
            alpha_values = list(range(1, 360 + 1))
        elif first_folder == "S":
            alpha_values = list(range(1, 360 + 1))
        elif first_folder == "M":
            alpha_values = list(range(1, 180 + 1))
        elif first_folder == "L":
            # 0.5 to 60.0 in 0.5 steps
            alpha_values = [x * 0.5 for x in range(1, 121)]
        elif first_folder == "XL":
            alpha_values = list(range(1, 60 + 1))
        elif first_folder == "XXL":
            # 0.1 to 2.0 in 0.1 steps, then integers 3 to 15
            float_alphas = [round(x * 0.1, 2) for x in range(1, 21)]
            alpha_values = float_alphas + list(range(3, 16))
        elif first_folder == "XXXL":
            # 0.1 to 1.0 in 0.1 steps, then integers 2 to 10
            float_alphas = [round(x * 0.1, 2) for x in range(1, 11)]
            alpha_values = float_alphas + list(range(2, 11))
        else:
            continue
        
        for file in files:
            input_path    = os.path.join(root, file)
            relative_path = os.path.relpath(root, inputs_dir)
            output_subdir = os.path.join(output_base_dir, relative_path)

            os.makedirs(output_subdir, exist_ok=True)

            file_base = os.path.splitext(file)[0]
            csv_path  = os.path.join(output_subdir, file_base + ".csv")

            if os.path.exists(csv_path):
                print(f"Skipping {file}: '{csv_path}' already exists.")
                continue

            with open(csv_path, "w") as csv_file:
                csv_file.write("alpha,rho,time(sec),max_memory_diff(MB),cost\n")
                csv_file.flush()
                
                for rho in rho_values:
                    for alpha in alpha_values:

                        total_time = 0.0
                        total_max_memory_diff = 0.0
                        total_cost = 0.0

                        for _ in range(num_executions):

                            temp_output = os.path.join(output_subdir, "temp_output.txt")

                            cmd = [
                                binary_path,
                                f"--alpha={alpha}",
                                f"--rho={rho}",
                                f"--input={input_path}",
                                f"--output={temp_output}"
                            ]

                            print("Running:", " ".join(cmd))
                            subprocess.call(cmd)

                            with open(temp_output, "r") as f:
                                line1 = f.readline().strip()
                                line2 = f.readline().strip()
                                line3 = f.readline().strip()

                            os.remove(temp_output)

                            time_val = float(line1.split(":")[1].strip())
                            max_memory_diff = float(line2.split(":")[1].strip())
                            cost_val = float(line3.split(":")[1].strip())

                            print("Time: ", time_val)
                            print("Mem: ", max_memory_diff)
                            print("Cost: ", cost_val)

                            total_time += time_val
                            total_max_memory_diff += max_memory_diff
                            total_cost += cost_val

                        avg_time = total_time / num_executions
                        avg_max_memory_diff = total_max_memory_diff / num_executions
                        avg_cost = total_cost / num_executions

                        csv_file.write(f"{alpha},{rho},{avg_time:.6f},{avg_max_memory_diff:.6f},{avg_cost:.6f}\n")
                        csv_file.flush()

            print(f"✔ CSV created: {csv_path}")

# ==============================================================================
# STEP 2: take_min_cost.py (Aggregate best alpha value for each input and create Outputs/Outputs.csv)
# ==============================================================================
def step2_take_min_cost():
    print("\n" + "="*60)
    print(">>> EXECUTING STEP 2: Aggregating Best Alphas (take_min_cost.py)")
    print("="*60)

    outputs_dir = "Outputs"
    sub_directories = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
    header_fields = ["input", "alpha", "rho", "time(sec)", "max_memory_diff(MB)", "cost"]

    def aggregate_size_directories(base_dir, sizes):
        print("--- Starting Level 1 Aggregation (Best 'cost' per input file) ---")
        
        for size_dir_name in sizes:
            size_path = os.path.join(base_dir, size_dir_name)
            if not os.path.isdir(size_path):
                print(f"Directory not found: {size_path}. Skipping.")
                continue
                
            summary_csv_path = os.path.join(size_path, f"{size_dir_name}.csv")
            all_best_rows = []
            
            for root, dirs, files in os.walk(size_path):
                if root != size_path and files:
                    csv_files = [f for f in files if f.endswith(".csv")]
                    
                    for csv_file in csv_files:
                        input_name = os.path.splitext(csv_file)[0]
                        path = os.path.join(root, csv_file)

                        min_cost = float("inf")
                        best_row = None
                        
                        try:
                            with open(path, "r", newline="") as fin:
                                reader = csv.reader(fin)
                                try:
                                    next(reader)
                                except StopIteration:
                                    continue # Empty file

                                for row in reader:
                                    if len(row) < 5:
                                        continue
                                    try:
                                        cost = float(row[4])
                                        if cost < min_cost:
                                            min_cost = cost
                                            best_row = (input_name, row[0], row[1], float(row[2]), float(row[3]), cost)
                                    except ValueError:
                                        continue

                        except FileNotFoundError:
                            print(f"File not found: {path}")
                            continue
                            
                        if best_row:
                            all_best_rows.append(best_row)

            all_best_rows.sort(key=lambda x: x[0])
            
            if all_best_rows:
                print(f"Creating summary CSV: {summary_csv_path}")
                with open(summary_csv_path, "w", newline="") as fout:
                    writer = csv.writer(fout)
                    writer.writerow(header_fields)
                    writer.writerows(all_best_rows)
                print(f"✔ Created: {summary_csv_path} with {len(all_best_rows)} entries.")
            else:
                print(f"No valid data found to create summary CSV for {size_dir_name}.")

    def combine_final_output(base_dir, sizes):
        print("\n--- Starting Level 2 Aggregation (Final 'Outputs.csv') ---")
        final_output_path = os.path.join(base_dir, "Outputs.csv")
        all_final_rows = []
        
        for size_dir_name in sizes:
            summary_csv_path = os.path.join(base_dir, size_dir_name, f"{size_dir_name}.csv")
            
            if not os.path.exists(summary_csv_path):
                print(f"Summary CSV not found: {summary_csv_path}. Skipping.")
                continue
                
            print(f"Reading data from: {summary_csv_path}")
            try:
                with open(summary_csv_path, "r", newline="") as fin:
                    reader = csv.reader(fin)
                    try:
                        next(reader) 
                    except StopIteration:
                        continue 
                        
                    for row in reader:
                        all_final_rows.append(row)
            except Exception as e:
                print(f"Error reading {summary_csv_path}: {e}")

        all_final_rows.sort(key=lambda x: x[0])

        if all_final_rows:
            print(f"Creating final combined CSV: {final_output_path}")
            with open(final_output_path, "w", newline="") as fout:
                writer = csv.writer(fout)
                final_header = ["size"] + header_fields
                writer.writerow(final_header)
                
                final_data_with_size = []
                for size_dir_name in sizes:
                    summary_csv_path = os.path.join(base_dir, size_dir_name, f"{size_dir_name}.csv")
                    if not os.path.exists(summary_csv_path):
                        continue
                        
                    with open(summary_csv_path, "r", newline="") as fin:
                        reader = csv.reader(fin)
                        try:
                            next(reader) 
                        except StopIteration:
                            continue
                            
                        for row in reader:
                            final_data_with_size.append([size_dir_name] + row)

                final_data_with_size.sort(key=lambda x: x[1])
                writer.writerows(final_data_with_size)
            print(f"Successfully created final output: {final_output_path} with {len(final_data_with_size)} entries.")
        else:
            print("No data found to create the final Outputs.csv.")

    aggregate_size_directories(outputs_dir, sub_directories)
    combine_final_output(outputs_dir, sub_directories)

# ==============================================================================
# STEP 3: rho_test.py (Check best value of alpha from Outputs.csv for inputs and 
# run the program with this alpha across various rho values)
# ==============================================================================
def step3_rho_test():
    print("\n" + "="*60)
    print(">>> EXECUTING STEP 3: Benchmarking Rho Convergence (rho_test1.py)")
    print("="*60)

    EXECUTABLE = "./Bin/bucket-partitioned-MDS"  
    INPUTS_DIR = "Inputs"
    OUTPUTS_BASE_DIR = "Outputs_Rho"
    REFERENCE_CSV = "Outputs/Outputs.csv"  
    NUM_EXECUTIONS = 5 

    RHO_VALUES = [1, 10, 100, 1000, 10000, 100000, 1000000]

    CSV_COL_FILENAME = "input" 
    CSV_COL_ALPHA = "alpha"
    CSV_COL_COST = "cost"

    def load_best_alphas(csv_path):
        best_alphas = {}
        if not os.path.exists(csv_path):
            print(f"Error: Reference CSV '{csv_path}' not found.")
            return best_alphas

        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                filename_base = row[CSV_COL_FILENAME].strip()
                alpha = float(row[CSV_COL_ALPHA])
                cost = float(row[CSV_COL_COST])
                
                if filename_base not in best_alphas or cost < best_alphas[filename_base]['cost']:
                    best_alphas[filename_base] = {'alpha': alpha, 'cost': cost}
                    
        return best_alphas

    def parse_solver_output(file_content):
        cost = "N/A"
        ex_time = "N/A"
        memory = "N/A"
        for line in file_content.split('\n'):
            if line.startswith("Cost:"):
                cost = line.split()[-1]
            elif line.startswith("Execution time"):
                ex_time = line.split()[-1]
            elif line.startswith("Maximum memory"):
                memory = line.split()[-1]
        return cost, ex_time, memory

    def main():
        print("Parsing reference CSV for best alphas...")
        best_alphas = load_best_alphas(REFERENCE_CSV)
        
        if not best_alphas:
            print("No alpha data loaded. Exiting.")
            return

        print(f"Found best alphas for {len(best_alphas)} unique instances.\n")

        for root, dirs, files in os.walk(INPUTS_DIR):
            for file in files:
                if file.endswith(".vrp"):
                    input_path = os.path.join(root, file)
                    file_base = file.replace('.vrp', '')
                    match_name = None
                    
                    if file_base in best_alphas:
                        match_name = file_base
                    else:
                        for k in best_alphas.keys():
                            if file_base.startswith(k):
                                match_name = k
                                break
                    
                    if not match_name:
                        print(f"Warning: No best alpha found for {file}. Skipping.")
                        continue
                    
                    best_alpha = best_alphas[match_name]['alpha']
                    
                    rel_path = os.path.relpath(root, INPUTS_DIR)
                    out_dir = os.path.join(OUTPUTS_BASE_DIR, rel_path)
                    os.makedirs(out_dir, exist_ok=True)
                    
                    out_csv_path = os.path.join(out_dir, f"{file_base}.csv")

                    if os.path.exists(out_csv_path):
                        print(f"Skipping {file}: '{out_csv_path}' already exists.")
                        continue
                    
                    print(f"Processing: {file} (Using Best Alpha: {best_alpha})")
                    
                    with open(out_csv_path, 'w', newline='') as out_f:
                        writer = csv.writer(out_f)
                        writer.writerow(["alpha", "rho", "time(sec)", "max_memory_diff(MB)", "cost"])
                        
                        for rho in RHO_VALUES:
                            temp_output = os.path.join(out_dir, "temp_output.txt")
                            
                            cmd = [
                                EXECUTABLE,
                                f"--alpha={best_alpha}",
                                f"--rho={rho}",
                                f"--input={input_path}",
                                f"--output={temp_output}"
                            ]
                            
                            sum_time = 0.0
                            sum_mem = 0.0
                            sum_cost = 0.0
                            success_runs = 0
                            
                            for i in range(NUM_EXECUTIONS):
                                try:
                                    subprocess.run(
                                        cmd, 
                                        stdout=subprocess.PIPE, 
                                        stderr=subprocess.PIPE, 
                                        universal_newlines=True, 
                                        check=True
                                    )
                                    
                                    with open(temp_output, 'r', encoding='utf-8') as f:
                                        file_content = f.read()
                                    
                                    cost, ex_time, memory = parse_solver_output(file_content)
                                    
                                    sum_time += float(ex_time)
                                    sum_mem += float(memory)
                                    sum_cost += float(cost)
                                    success_runs += 1
                                    
                                except subprocess.CalledProcessError as e:
                                    print(f"Error running {file} with Rho={rho} on run {i+1}: {e}")
                                    break
                                except FileNotFoundError:
                                    print(f"Output file not found for {file} with Rho={rho} on run {i+1}")
                                    break
                                except ValueError:
                                    print(f"Failed to parse numerical output for {file} with Rho={rho} on run {i+1}")
                                    break
                            
                            if success_runs == NUM_EXECUTIONS:
                                avg_time = sum_time / NUM_EXECUTIONS
                                avg_mem = sum_mem / NUM_EXECUTIONS
                                avg_cost = sum_cost / NUM_EXECUTIONS
                                writer.writerow([
                                    best_alpha, 
                                    rho, 
                                    f"{avg_time:.4f}", 
                                    f"{avg_mem:.4f}", 
                                    f"{avg_cost:.4f}"
                                ])
                            else:
                                writer.writerow([best_alpha, rho, "ERROR", "ERROR", "ERROR"])
                                
                            out_f.flush() 

        print(f"\nAll benchmarking complete. Averaged results saved in the '{OUTPUTS_BASE_DIR}/' directory.")

    main()

# ==============================================================================
# STEP 4: benchmark.py (Store benchmarking outputs comparing custom minheap and lazy dfs benefits)
# ==============================================================================
def step4_benchmark():
    print("\n" + "="*60)
    print(">>> EXECUTING STEP 4: Algorithm Variant Benchmarking (benchmark.py)")
    print("="*60)

    BIN_DIR = "./Bin"
    INPUTS_DIR = "Inputs"
    REFERENCE_CSV = "Outputs/Outputs.csv"
    RHO_VALUE = 5000  
    NUM_EXECUTIONS = 5  

    VARIANT_MAP = {
        "BPMDS(Custom_MinHeap+Lazy_DFS)": "bucket-partitioned-MDS",
        "CPP_Set": "bucket-partitioned-MDS-set",
        "Non_Lazy_DFS": "bucket-partitioned-MDS-dfs"
    }

    COLUMNS = ["instance name", "size category", "BPMDS(Custom_MinHeap+Lazy_DFS)", "CPP_Set", "Non_Lazy_DFS"]

    TIME_CSV = "benchmark_execution_times.csv"
    MEM_CSV = "benchmark_memory_usage.csv"

    def load_best_alphas(csv_path):
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
        
        for csv_file in [TIME_CSV, MEM_CSV]:
            with open(csv_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=COLUMNS)
                writer.writeheader()

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
                    
                    with open(TIME_CSV, 'a', newline='') as tf, open(MEM_CSV, 'a', newline='') as mf:
                        t_writer = csv.DictWriter(tf, fieldnames=COLUMNS)
                        m_writer = csv.DictWriter(mf, fieldnames=COLUMNS)
                        
                        t_writer.writerow(t_row)
                        m_writer.writerow(m_row)
                        
                        tf.flush()
                        mf.flush()

        if os.path.exists("temp_out.txt"):
            os.remove("temp_out.txt")

        print(f"\nAll variants benchmarked successfully.")
        print(f"Times saved to: {TIME_CSV}")
        print(f"Memory saved to: {MEM_CSV}")

    main()

# ==============================================================================
# STEP 5: threads.py (Store Speedup and efficiency of using different number of threads)
# ==============================================================================
def step5_threads():
    print("\n" + "="*60)
    print(">>> EXECUTING STEP 5: OpenMP Scaling Benchmark (threads.py)")
    print("="*60)

    INPUTS_DIR = "Inputs"
    OUTPUTS_CSV = "Outputs/Outputs.csv"
    SCALING_OUT_DIR = "Scaling_Outputs"
    EXECUTABLE = "./Bin/bucket-partitioned-MDS"
    RUNS_PER_THREAD = 5  
    THREAD_COUNTS = [1, 2, 4, 8, 16, 32, 40]

    def load_optimal_parameters():
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

                    out_csv_path = os.path.join(SCALING_OUT_DIR, f"{base_name}.csv")
                    
                    if os.path.exists(out_csv_path):
                        print(f"Skipping {file}: '{out_csv_path}' already exists.")
                        continue

                    print(f"\nBenchmarking: {file}")
                    
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

    main()

# ==============================================================================
# STEP 6: Generate Bucket Metrics
# ==============================================================================
def step6_bucket_metrics():
    print("\n" + "="*60)
    print(">>> EXECUTING STEP 6: Generating Bucket Metrics")
    print("="*60)

    EXECUTABLE = "./Bin/bucket-partitioned-MDS-buckets"
    OUTPUT_DIR = "Bucket_metrics"
    REFERENCE_CSV = "Outputs/Outputs.csv"
    INPUTS_DIR = "Inputs-all"
    
    TARGET_INSTANCES = [
        'Inputs-all/L/Flanders/Flanders1',
        'Inputs-all/L/Flanders/Flanders2',
        'Inputs-all/L/Brussels/Brussels1',
        'Inputs-all/L/Brussels/Brussels2'
    ]

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    best_params = {}
    if os.path.exists(REFERENCE_CSV):
        with open(REFERENCE_CSV, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                instance = row['input'].strip()
                alpha = float(row['alpha'])
                rho = int(float(row['rho'])) if 'rho' in row and row['rho'] else 10000
                best_params[instance] = {'alpha': alpha, 'rho': rho}

    file_map = {}
    for root, _, files in os.walk(INPUTS_DIR):
        for file in files:
            if file.endswith('.vrp'):
                file_map[file.replace('.vrp', '')] = os.path.join(root, file)

    for target in TARGET_INSTANCES:
        base_name = os.path.basename(target).replace('.vrp', '')
        
        if base_name not in file_map:
            print(f"Warning: {base_name} not found in {INPUTS_DIR}. Skipping.")
            continue
            
        input_path = file_map[base_name]
        
        alpha = best_params.get(base_name, {}).get('alpha', 15.0) 
        rho = best_params.get(base_name, {}).get('rho', 10000)

        print(f"Generating metrics for {base_name} (Alpha: {alpha}, Rho: {rho})")
        
        cmd = [
            EXECUTABLE, 
            f"--alpha={alpha}", 
            f"--rho={rho}", 
            f"--input={input_path}", 
            "--output=temp_bucket_out.txt"
        ]
        
        try:
            subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            
            if os.path.exists("bucket_metrics.csv"):
                dest = os.path.join(OUTPUT_DIR, f"{base_name}.csv")
                
                if os.path.exists(dest):
                    os.remove(dest)
                    
                os.rename("bucket_metrics.csv", dest)
                print(f"   ✔ Successfully renamed and saved to {dest}")
            else:
                print(f"   ✖ Error: bucket_metrics.csv was not generated for {base_name}")
                
        except Exception as e:
            print(f"   ✖ Execution failed for {base_name}: {e}")
            
    if os.path.exists("temp_bucket_out.txt"):
        os.remove("temp_bucket_out.txt")

# ==============================================================================
# STEP 7: BFS Benchmarking
# ==============================================================================
def step7_bfs_benchmarking():
    print("\n" + "="*60)
    print(">>> EXECUTING STEP 7: BFS Benchmarking (from Old_Outputs.csv)")
    print("="*60)

    OLD_CSV = "Old_Outputs.csv"
    OUTPUT_DIR = "Outputs_BFS"
    NEW_CSV = os.path.join(OUTPUT_DIR, "BFS_Outputs.csv")
    INPUTS_DIR = "Inputs-all"
    EXECUTABLE = "./Bin/bucket-partitioned-MDS-buckets-bfs"
    NUM_EXECUTIONS = 5

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if not os.path.exists(OLD_CSV):
        print(f"Error: '{OLD_CSV}' not found! Skipping BFS Benchmarking.")
        return

    tasks = []
    with open(OLD_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = [h.strip() for h in reader.fieldnames]
        reader.fieldnames = headers
        for row in reader:
            input_name = row['input'].strip()
            if not input_name.endswith('.vrp'):
                input_name += '.vrp'
            alpha = float(row['alpha'])
            rho = int(float(row['rho'])) if 'rho' in row else 5000
            size = row['size'] if 'size' in row else 'UNKNOWN'
            tasks.append({'file': input_name, 'alpha': alpha, 'rho': rho, 'size': size})

    file_map = {}
    for root, _, files in os.walk(INPUTS_DIR):
        for file in files:
            if file.endswith('.vrp'):
                file_map[file] = os.path.join(root, file)

    with open(NEW_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["size", "input", "alpha", "rho", "time(sec)", "max_memory_diff(MB)", "cost"])
        
        for task in tasks:
            file_name = task['file']
            if file_name not in file_map:
                continue
            
            input_path = file_map[file_name]
            alpha = task['alpha']
            rho = task['rho']
            base_name = file_name.replace('.vrp', '')
            
            print(f"BFS Benchmarking: {base_name} (Alpha: {alpha}, Rho: {rho})")
            
            sum_time = 0.0
            sum_mem = 0.0
            sum_cost = 0.0
            success_runs = 0
            
            for _ in range(NUM_EXECUTIONS):
                temp_output = os.path.join(OUTPUT_DIR, "local_bfs_output.txt")
                cmd = [
                    EXECUTABLE, 
                    f"--alpha={alpha}", 
                    f"--rho={rho}", 
                    f"--input={input_path}", 
                    f"--output={temp_output}"
                ]
                
                try:
                    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
                    with open(temp_output, 'r') as tf:
                        content = tf.read()
                        ex_time = float(next((l.split()[-1] for l in content.split('\n') if "Execution time" in l), 0))
                        memory = float(next((l.split()[-1] for l in content.split('\n') if "Maximum memory" in l), 0))
                        cost = float(next((l.split()[-1] for l in content.split('\n') if "Cost:" in l), 0))
                        
                        sum_time += ex_time
                        sum_mem += memory
                        sum_cost += cost
                        success_runs += 1
                except Exception:
                    pass
            
            if success_runs == NUM_EXECUTIONS:
                avg_time = sum_time / NUM_EXECUTIONS
                avg_mem = sum_mem / NUM_EXECUTIONS
                avg_cost = sum_cost / NUM_EXECUTIONS
                writer.writerow([task['size'], base_name, alpha, rho, f"{avg_time:.6f}", f"{avg_mem:.6f}", f"{avg_cost:.6f}"])
            else:
                writer.writerow([task['size'], base_name, alpha, rho, "ERROR", "ERROR", "ERROR"])
            f.flush()
            
    if os.path.exists(os.path.join(OUTPUT_DIR, "local_bfs_output.txt")):
        os.remove(os.path.join(OUTPUT_DIR, "local_bfs_output.txt"))
        
    print(f"\nBFS Benchmarking complete! Metrics saved to '{NEW_CSV}'")

# ==============================================================================
# STEP 8: Generate BFS vs DFS Gaps (BFS_Gaps.csv)
# ==============================================================================
def step8_generate_bfs_gaps():
    print("\n" + "="*60)
    print(">>> EXECUTING STEP 8: Generating BFS_Gaps.csv")
    print("="*60)

    DFS_CSV = "Outputs/Outputs.csv"          # Standard DFS outputs
    BFS_CSV = "Outputs_BFS/BFS_Outputs.csv"  # Generated in Step 7
    OUT_CSV = "BFS_Gaps.csv"
    
    # Target instances and their Best Known Solutions (BKS)
    BKS_DICT = {
        'Antwerp1': 477277.00,
        'Antwerp2': 291350.00,
        'Brussels1': 501719.00,
        'Brussels2': 345468.00,
        'CMT4': 1028.42,
        'CMT5': 1291.289,
        'Flanders1': 7240118.00,
        'Flanders2': 4373244.00,
        'Leuven1': 192848.00,
        'Leuven2': 111395.00
    }

    if not os.path.exists(DFS_CSV) or not os.path.exists(BFS_CSV):
        print(f"Error: Required CSVs not found. Ensure {DFS_CSV} and {BFS_CSV} exist.")
        return

    # 1. Load standard DFS costs
    dfs_costs = {}
    with open(DFS_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            instance = row['input'].strip()
            if instance in BKS_DICT:
                dfs_costs[instance] = float(row['cost'])

    # 2. Process BFS outputs, merge with DFS, and calculate gaps
    results = []
    with open(BFS_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            instance = row['input'].strip()
            if instance in BKS_DICT:
                bks = BKS_DICT[instance]
                bfs_cost = float(row['cost'])
                
                # Calculate BFS Gap
                gap_bfs = ((bfs_cost - bks) / bks) * 100
                
                # Calculate DFS Gap 
                dfs_cost = dfs_costs.get(instance, bfs_cost) # Fallback to bfs cost if missing
                gap_dfs = ((dfs_cost - bks) / bks) * 100
                
                # Append row structure expected by the plotting script
                results.append({
                    'size': row.get('size', 'UNKNOWN'),
                    'input': instance,
                    'alpha': row.get('alpha', ''),
                    'rho': row.get('rho', ''),
                    'time(sec)': row.get('time(sec)', ''),
                    'max_memory_diff(MB)': row.get('max_memory_diff(MB)', ''),
                    'cost': bfs_cost,
                    'bks': bks,
                    'Gap_BFS(%)': gap_bfs,
                    'Gap_DFS(%)': gap_dfs
                })

    if not results:
        print("No matching target instances found in your BFS outputs. Exiting.")
        return

    # 3. Write final data to BFS_Gaps.csv
    fieldnames = ['size', 'input', 'alpha', 'rho', 'time(sec)', 'max_memory_diff(MB)', 
                  'cost', 'bks', 'Gap_BFS(%)', 'Gap_DFS(%)']
    
    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        # Sort alphabetically by instance name for a clean CSV
        results.sort(key=lambda x: x['input'])
        
        for row in results:
            row['cost'] = f"{row['cost']:.5f}"
            row['Gap_BFS(%)'] = f"{row['Gap_BFS(%)']:.6f}"
            row['Gap_DFS(%)'] = f"{row['Gap_DFS(%)']:.6f}"
            writer.writerow(row)

    print(f"✔ Successfully generated '{OUT_CSV}' with {len(results)} target instances.")

# ==============================================================================
# PIPELINE EXECUTION BLOCK
# ==============================================================================
if __name__ == "__main__":
    print("Initializing BP_MDS Master Pipeline...")
    compile_binaries()
    step1_script()
    step2_take_min_cost()
    step4_benchmark()    
    step5_threads()      
    step3_rho_test() 
    step6_bucket_metrics()
    step7_bfs_benchmarking()
    step8_generate_bfs_gaps()