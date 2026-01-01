#pragma once

namespace space_age {

struct space_age {
    space_age(long seconds) : seconds_(seconds) {}
    long seconds_;
    long seconds() const;
    double on_earth() const;
    double on_mercury() const;
    double on_venus() const;
    double on_mars() const;
    double on_jupiter() const;
    double on_saturn() const;
    double on_uranus() const;
    double on_neptune() const;
};


}  // namespace space_age
