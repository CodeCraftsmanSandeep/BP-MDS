# Compiler (override on macOS: make CXX=g++-15)
CXX = g++

# Build flags:
#   -O3              speed optimizations
#   -march=native    use this machine's CPU features
#   -flto            link-time optimization
#   -std=c++17       C++17
#   -fopenmp         OpenMP parallelism
#   -IInclude        look for headers in Include/
#   -static-libstdc++  static-link libstdc++ (Linux clusters)
OMPFLAGS = -O3 -march=native -flto -std=c++17 -fopenmp -IInclude -static-libstdc++

# Sources: entry point + every .cpp under Lib/ (main solver only)
SRC = Src/Main.cpp \
      $(shell find Lib -name '*.cpp')

# Output binary
TARGET = Bin/bucket-partitioned-MDS

# Default: build the solver
all: $(TARGET)

# Compile & link all SRC into TARGET ($^ = sources, $@ = output)
$(TARGET): $(SRC)
	@mkdir -p Bin
	$(CXX) $(OMPFLAGS) $^ -o $@
	@echo "Build successful: $@"

# Remove the binary
clean:
	rm -f $(TARGET)
	@echo "Cleaned build artifacts."
