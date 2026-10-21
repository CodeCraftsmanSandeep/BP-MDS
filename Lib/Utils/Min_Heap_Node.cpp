#include "Utils.h"

Min_Heap_Node::Min_Heap_Node(
    node_t _u,
    node_t _v,
    distance_t _weight)
    : u(_u), v(_v), weight(_weight) {}

Min_Heap_Node::Min_Heap_Node()
    : u(0), v(0), weight(0) {}

void Min_Heap_Node::reset_node(
    node_t _u,
    node_t _v,
    distance_t _weight)
{
    this->u = _u;
    this->v = _v;
    this->weight = _weight;
}
