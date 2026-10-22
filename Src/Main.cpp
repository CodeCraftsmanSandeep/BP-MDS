#include "Command_Line_Args.h"
#include "Initializer.h" 
#include "Bucket_Partitioned_MDS.h"
#include <iostream>
#include <chrono>
 
int main(int argc, char* argv[]) 
{ 
    const Command_Line_Args args(argc, argv);
    initialize(args);

    std::cerr << "[bpmds] loading instance (alpha=" << args.get_alpha()
              << ", rho=" << args.get_rho() << ")...\n" << std::flush;

    auto t0 = std::chrono::high_resolution_clock::now();
    const Bucket_Partitioned_MDS::CVRP cvrp(args.input());
    auto t1 = std::chrono::high_resolution_clock::now();

    std::cerr << "[bpmds] loaded N=" << cvrp.size()
              << " customers+depot, Q=" << cvrp.capacity()
              << " (" << std::chrono::duration<double>(t1 - t0).count() << "s)\n"
              << std::flush;

    const Bucket_Partitioned_MDS::Solver solver(args.get_alpha(), args.get_rho());

    std::cerr << "[bpmds] solving...\n" << std::flush;
    Bucket_Partitioned_MDS::Solution cvrp_solution = solver.solve(cvrp);

    std::cerr << "[bpmds] verifying...\n" << std::flush;
    cvrp_solution.verify(cvrp);

    std::cerr << "[bpmds] writing solution...\n" << std::flush;
    cvrp_solution.print(args.output());

    std::cerr << "[bpmds] done.\n" << std::flush;
    return 0;
}
