#include "Command_Line_Args.h"
#include <iomanip>
#include <omp.h>

void initialize(const Command_Line_Args& args)
{
    args.output() << std::fixed << std::setprecision(4);
    // Nested teams: buckets outer, rho trials inner.
    omp_set_nested(1);
    omp_set_max_active_levels(2);
}
