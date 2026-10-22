#include "Utils.h"
#include <iostream>
#include <cmath>

distance_t Unit_Vector_2D::get_norm(
    const cord_t x,
    const cord_t y) const
{
    return sqrt(x * x + y * y);
}

angle_t Unit_Vector_2D::degree_to_radian(
    const angle_t theta_deg) const
{
    return theta_deg * PI / 180.0;
}

Unit_Vector_2D::Unit_Vector_2D(
    cord_t _x,
    cord_t _y)
{
    auto norm_val = get_norm(_x, _y);
    this->x = _x / norm_val;
    this->y = _y / norm_val;

    return;
}

Unit_Vector_2D::Unit_Vector_2D(
    const Point& point1,
    const Point& point2)
{
    auto _x = point2.x - point1.x;
    auto _y = point2.y - point1.y;
    auto norm_val = get_norm(_x, _y);
    this->x = _x / norm_val;
    this->y = _y / norm_val;

    return;
}

Unit_Vector_2D::Unit_Vector_2D(
    const Unit_Vector_2D& v,
    const angle_t theta_deg)
{
    auto theta_rad = this->degree_to_radian(theta_deg);
    this->x = v.x * std::cos(theta_rad) - v.y * std::sin(theta_rad);
    this->y = v.x * std::sin(theta_rad) + v.y * std::cos(theta_rad);

    return;
}

bool Unit_Vector_2D::operator==(
    const Unit_Vector_2D& other) const
{
    return (std::fabs(this->x - other.x) < EPS) && (std::fabs(this->y - other.y) < EPS);
}


bool Unit_Vector_2D::is_in_between(
    const Unit_Vector_2D& vec1,
    const Unit_Vector_2D& vec2) const
{
    // Half-open angular sector [vec1, vec2) sweeping CCW.
    if (vec1 == vec2)
    {
        HANDLE_ERROR("The angle between starting & ending vectors of a partition cannot be zero!", true);
    }

    if (vec1 == *this)
    {
        return true;
    }

    if (vec2 == *this)
    {
        return false;
    }

    cord_t cross12 = vec1.x * vec2.y - vec1.y * vec2.x;
    cord_t cross1p = vec1.x * this->y - vec1.y * this->x;
    cord_t crossp2 = this->x * vec2.y - this->y * vec2.x;

    if(cross12 >= 0)
    {
        return cross1p >= 0 && crossp2 >= 0;
    }
    else
    {
        return !(cross1p < 0 && crossp2 < 0);
    }
}

void Unit_Vector_2D::print(
    std::ostream& output) const
{
    output << "Unit Vector: (" << this->x << ", " << this->y << ")" << "\n";

    return;
}
