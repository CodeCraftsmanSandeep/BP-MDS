#ifndef BUCKET_PARTITIONED_MDS_H
#define BUCKET_PARTITIONED_MDS_H

#include "Utils.h"
#include <vector>
#include <string>
#include <cfloat>
#include <cmath>
#include <iostream>

namespace Bucket_Partitioned_MDS
{
    class CVRP
    {
    private:
        capacity_t _capacity;
        int _size;
        std::vector <Point> node;
        std::string type;
        const node_t _depot = 0;

    public:
        CVRP(
            std::istream&);
        distance_t distance(
            const node_t,
            const node_t) const;

        // No bounds checks; caller must pass valid indices.
        distance_t distance_fast(
            const node_t u,
            const node_t v) const
        {
            if (u == v)
            {
                return 0.0;
            }
            const double dx = node[u].x - node[v].x;
            const double dy = node[u].y - node[v].y;
            return std::sqrt(dx * dx + dy * dy);
        }

        const Point& operator[](
            const node_t) const;
        void print(
            std::ostream&) const;
        capacity_t capacity() const;
        int size() const;
        node_t depot() const;
    };

    class Solution
    {
    private:
        double time_for_solving;
        double maxMB_difference;
        double cost;
        std::vector <std::vector <node_t>> routes;

        distance_t get_total_cost_of_routes(
            const CVRP& cvrp);
    public:
        Solution(
            const double,
            const double,
            const double,
            const std::vector <std::vector <node_t>>&);
        bool verify(
            const CVRP&) const;
        void print(
            std::ostream&) const;
    };

    class Solver
    {
    private:
        const double alpha;
        const int rho;

        void get_bucket(
            const CVRP&,
            const double,
            const double,
            std::vector <node_t>&) const;

        void construct_mst(
            const CVRP&,
            const std::vector <node_t>&,
            std::vector <std::vector <node_t>>&) const;

        distance_t get_route_distance(
            const CVRP&,
            const std::vector <node_t>&) const;

        void tsp_approx(
            const CVRP&,
            std::vector <node_t>&,
            std::vector <node_t>&,
            node_t) const;

        std::vector<std::vector<node_t>> process_tsp_approx(
            const CVRP&,
            const std::vector<std::vector<node_t>>&) const;

        void tsp_2OPT(
            const CVRP&,
            std::vector <node_t>&,
            std::vector <node_t>&,
            int) const;

        std::vector<std::vector<node_t>> process_2OPT(
            const CVRP&,
            const std::vector<std::vector<node_t>>&) const;

        void process_routes(
            const CVRP&,
            std::vector <std::vector<int>>&,
            distance_t&) const;

        void get_routes(
            const CVRP&,
            const std::vector <std::vector <node_t>>&,
            const std::vector <node_t>&,
            std::vector <std::vector <node_t>>&,
            distance_t&,
            distance_t cost_bound,
            unsigned seed) const;

    public:
        Solver(
            const double,
            const int);

        Solution solve(
            const CVRP&) const;

        void create_buckets(
            const CVRP&,
            std::vector <std::vector <node_t>>&) const;
    };
}

#endif
