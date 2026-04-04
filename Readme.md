- C++17 is needed as some features of c++17 is used in codebase

| Name | Number of Customers |
|:-----|:---|
| XS | 1 - 100 |
| S | 101 - 1,000 |
| M | 1,001 - 10,000 |
| L | 10,001 - 50,000 |
| XL | 50,001 - 100,000 |
| XXL | 100,001 - 1,000,000 |
| XXXL | 1,000,001 - 10,000,000 |

## test_pipeline.py:
The test_pipeline.py script is the main automation tool used to compile, test, and benchmark the BP_MDS routing algorithm. It automatically runs the C++ code across different input files, tests various parameters, and saves the results into neat CSV files so they can be plotted later.

Because High-Performance Computing (HPC) system performance can fluctuate, the script is configured to run every single test 5 times (NUM_EXECUTIONS = 5) and averages the execution time and memory usage to ensure the final results are highly accurate and reliable.

Pipeline Steps in testing script Explained:
The script is divided into distinct modular steps. By default, running the script executes the entire pipeline sequentially.

## compile_binaries()
* **What it does:** It cleans out any old, compiled code (make clean) and compiles the C++ codebase natively on the current compute node (make).

* **Outputs:** It generates three specific executable files inside the ./Bin/ folder, each testing a different implementation: 
    1. ./Bin/bucket-partitioned-MDS: The main, fully optimized algorithm (uses the Custom MinHeap + Lazy DFS).
    2. ./Bin/bucket-partitioned-MDS-set: A modified version that uses the standard C++ std::set to construct the MST (used to prove why our Custom MinHeap is faster).
    3. ./Bin/bucket-partitioned-MDS-dfs: A modified version that uses a "Non-Lazy" DFS traversal (used to test memory behavior when pre-copying the graph).

## step1_script() (The Alpha Parameter Search)
* **What it does:** This step tests how the "angle" parameter ($\alpha$) affects the algorithm. It takes the main executable and runs it on the .vrp input files in INPUTS directory. For every input, it tests a wide range of $\alpha$ angles (depending on the size category from XS-XXXL). It runs each angle 5 times and averages the performance.
* **Outputs:** Generates individual CSV files for each input graph. These are stored in categorized sub-directories based on their size and class (for example: Outputs/L/Flanders/Flanders1.csv).

## step2_take_min_cost() (Finding the Best Alpha)
* **What it does:** Because Step 1 tests dozens of angles for the exact same input graph, we need to find out which angle actually gave the best delivery route. This step scans all the individual CSV files generated in Step 1. For each input graph, it extracts the single row that produced the lowest total routing cost.
* **Outputs:** It combines these "best" rows into one master dataset and saves it as Outputs/Outputs.csv. This master file contains the best $\alpha$, execution time, and memory usage for every input in Inputs directory.


## step4_benchmark() (Comparing Code Implementations)
* **What it does:** This step tests the benfits of our custome code modifications. It takes all inputs in the Inputs directory and runs them through all three executables generated in the compile step. It compares our Custom MinHeap against the C++ std::set, and our Lazy DFS against the Non-Lazy DFS. Each implementation is run 5 times and averaged.
* **Outputs:** Generates two distinct files in the root directory:
benchmark_execution_times.csv and benchmark_memory_usage.csv detailing the execution times and peak memory usage details recorded for each input across the 3 executables.

## step5_threads() (Testing Multiple CPU Cores)
* **What it does:** This step tests how well the algorithm speeds up when we give it more CPU cores to work with (Strong Scaling). It runs the main program using an increasing number of OpenMP threads: 1, 2, 4, 8, 16, 32, and 40. It runs each configuration 5 times and averages the results.
To ensure the scaling measurements are mathematically accurate, this step explicitly exports 'OMP_PLACES'='cores'and 'OMP_PROC_BIND'='close' before running the executable. (In massive clusters, the Linux operating system can often move threads from one physical core to another during execution to balance heat or power. However, moving a thread destroys its L1/L2 CPU cache, causing massive, artificial drops in speed. By setting these variables, we **pin** every OpenMP thread to a specific, unmoving physical core. This guarantees maximum cache locality and proves the algorithm's true parallel efficiency.)
* **Outputs:** Creates individual CSV files for each tested input inside the Scaling_Outputs/ directory (e.g., Scaling_Outputs/Flanders2.csv). (Note: If a file already exists here, the script safely skips it so we dont test the same inputs again and again).

## step3_rho_test() (Testing Exploration Iterations)
* **What it does:** The parameter $\rho$ controls how many random DFS iterations the algorithm tries before giving up. First, this step parses the master Outputs/Outputs.csv (generated in Step 2) to look up the optimal "best $\alpha$" for a specific input. Then, locking in that exact $\alpha$, it runs the program while drastically increasing $\rho$: [1, 10, 100, 1000, 10^4, 10^5, 10^6]. It runs each of these 5 times and averages the results.
* **Outputs:** Generates individual CSV files detailing the cost-to-time trade-off, saved inside the Outputs_rho/ directory.

## Utility Function: `step0_fast_track()`

Because finding the "best $\alpha$" for massive 2-million node graphs in Step 1 can take many hours, we created `step0_fast_track()` to save time when moving between different computing clusters.

* **What it does:** If you already ran the full pipeline on one machine (e.g., the P100 cluster) and found all the optimal $\alpha$ values, you don't need to do a full parameter search on the new machine (e.g., the Aqua cluster). 
* **How it works:** 1. You rename the completed `Outputs/Outputs.csv` from your old machine to `Old_Outputs.csv` and place it in the root directory.
  2. The Fast Track utility parses `Old_Outputs.csv` row by row. 
  3. It extracts the input filename, the "best $\alpha$", and the "best $\rho$" that were already discovered.
  4. It immediately runs the executable on the new machine using *only* those optimal parameters.
* **Outputs:** It saves the new machine's Execution Time and Peak Memory directly into a new master file named **`New_Outputs.csv`**. This completely bypasses Step 1 and Step 2, allowing you to instantly recalibrate performance metrics for a new hardware architecture.

## Running the Entire Pipeline:
To run all the tests from start to finish, simply run the test_pipeline.py script after cloning this repo.
    
    $ python3 test_pipeline.py

## How to Customize the Run (Skipping Steps)
If you already generated some data and only want to run one specific step, you can easily disable the other steps.

Open test_pipeline.py and scroll to the very bottom of the file to the __main__ block.
Add a # symbol in front of the steps you want to skip.


    if __name__ == "__main__":
        print("Initializing BP_MDS Master Pipeline...")
    
        # Always leave the compile step on so your binaries are up to date
        compile_binaries()
        
        # --- Pipeline Execution Block ---
        # step0_fast_track()            # SKIPPED
        
        # step1_script()              # SKIPPED
        # step2_take_min_cost()       # SKIPPED
        step4_benchmark()           # Will run
        step5_threads()             # Will run
        # step3_rho_test()            # SKIPPED
    
