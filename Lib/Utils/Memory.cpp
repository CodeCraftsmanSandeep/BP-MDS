#include <sys/resource.h>
#include <fstream>
#include <string>
#include <cstring>

#include "Utils.h"


double get_curr_rss_mb() {
    char line[256];
    FILE *status_file = fopen("/proc/self/status", "r");

    if (!status_file) {
        perror("Error opening /proc/self/status");
        return -1.0;
    }

    while (fgets(line, sizeof(line), status_file)) {
        if (strncmp(line, "VmRSS:", 6) == 0) {
            long kb_value = 0;
            sscanf(line, "VmRSS:%ld", &kb_value);
            fclose(status_file);
            return kb_value / 1024.0;
        }
    }

    fclose(status_file);
    return -1.0;
}

double get_peak_rss_mb()
{
    struct rusage u;
    getrusage(RUSAGE_SELF, &u);
    return u.ru_maxrss / 1024.0;
}
