CXX = g++
# Using 'native' since compilation happens directly on the compute node
OMPFLAGS = -O3 -march=native -flto -std=c++17 -fopenmp -IInclude -static-libstdc++

# All common source files EXCEPT the Solvers
COMMON_SRC = Src/Main.cpp \
             Lib/Bucket_Partitioned_MDS/CVRP.cpp \
             Lib/Bucket_Partitioned_MDS/Solution.cpp \
             Lib/Command_Line_Args.cpp \
             Lib/Initializer.cpp \
             $(shell find Lib/Utils -name '*.cpp')

# Define the 3 target executables
TARGET_NORMAL = Bin/bucket-partitioned-MDS
TARGET_SET    = Bin/bucket-partitioned-MDS-set
TARGET_DFS    = Bin/bucket-partitioned-MDS-dfs

# Build all 3 by default
all: $(TARGET_NORMAL) $(TARGET_SET) $(TARGET_DFS)

# Compile Rule: Custom MinHeap + Lazy DFS (Original)
$(TARGET_NORMAL): $(COMMON_SRC) Lib/Bucket_Partitioned_MDS/Solver.cpp
	@mkdir -p Bin
	$(CXX) $(OMPFLAGS) $^ -o $@
	@echo "Build successful: $@"

# Compile Rule: CPP Set (From new directory)
$(TARGET_SET): $(COMMON_SRC) Benchmarking_Code/Solver_cpp_set.cpp
	@mkdir -p Bin
	$(CXX) $(OMPFLAGS) $^ -o $@
	@echo "Build successful: $@"

# Compile Rule: Non-Lazy DFS (From new directory)
$(TARGET_DFS): $(COMMON_SRC) Benchmarking_Code/Solver_Non_Lazy_DFS.cpp
	@mkdir -p Bin
	$(CXX) $(OMPFLAGS) $^ -o $@
	@echo "Build successful: $@"

clean:
	rm -f $(TARGET_NORMAL) $(TARGET_SET) $(TARGET_DFS)
	@echo "Cleaned build artifacts."
