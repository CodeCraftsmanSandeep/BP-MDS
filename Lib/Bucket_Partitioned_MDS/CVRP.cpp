#include "Bucket_Partitioned_MDS.h"
#include "Utils.h"

#include <stdexcept>
#include <iomanip>
#include <cmath>

namespace Bucket_Partitioned_MDS
{
    CVRP::CVRP(
        std::istream& input)
    {
        std::string line;

        for (int i = 0; i < 3; ++i)
        {
            getline(input, line);
        }

        // stoi: stof loses integers above ~2^24
        getline(input, line);
        _size = stoi(line.substr(line.find(":") + 2));

        getline(input, line);
        type = line.substr(line.find(":") + 2);

        getline(input, line);
        _capacity = stoi(line.substr(line.find(":") + 2));

        getline(input, line);

        node.resize(_size);

        for (int i = 0; i < _size; ++i) {
            getline(input, line);

            std::stringstream iss(line);
            int id;
            std::string xStr, yStr;

            iss >> id >> xStr >> yStr;
            node[i].x = stof(xStr);
            node[i].y = stof(yStr);
        }

        getline(input, line);

        for (int i = 0; i < _size; ++i) {
            getline(input, line);
            std::stringstream iss(line);

            int id;
            std::string dStr;
            iss >> id >> dStr;

            node[i].demand = stof(dStr);
        }
    }

    distance_t CVRP::distance(
        const node_t u,
        const node_t v) const
    {
        if (u < 0 || u >= _size)
        {
            HANDLE_ERROR("Index out of bounds: " + std::to_string(u) + " must be >= 0 and < " + std::to_string(_size), true);
        }

        if (v < 0 || v >= _size)
        {
            HANDLE_ERROR("Index out of bounds: " + std::to_string(v) + " must be >= 0 and < " + std::to_string(_size), true);
        }

        if (u == v)
        {
            return 0.0;
        }

        return std::sqrt((node[u].x - node[v].x) * (node[u].x - node[v].x) +
            (node[u].y - node[v].y) * (node[u].y - node[v].y));
    }

    const Point& CVRP::operator[](
        const node_t index) const
    {
        if (index < 0 || index >= _size)
        {
            HANDLE_ERROR("Index out of bounds: " + std::to_string(index) + " must be >= 0 and < " + std::to_string(_size), true);
        }
        return this->node[index];
    }

    void CVRP::print (
        std::ostream& output) const
    {
        output << "SIZE: " << _size << "\n";
        output << "Capacity: " << _capacity << "\n";
        output << std::setw(6) << "NODE"
                << std::setw(10) << "X"
                << std::setw(10) << "Y"
                << std::setw(10) << "DEMAND" << "\n";

        for (int i = 0; i < _size; ++i)
        {
            output << std::setw(6) << i
                    << std::setw(10) << node[i].x
                    << std::setw(10) << node[i].y
                    << std::setw(10) << node[i].demand
                    << "\n";
        }

        return;
    }

    capacity_t CVRP::capacity() const
    {
        return _capacity;
    }

    int CVRP::size() const
    {
        return _size;
    }

    node_t CVRP::depot() const
    {
        return _depot;
    }
}
