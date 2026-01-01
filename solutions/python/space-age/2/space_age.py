
"""
| Planet  | Orbital period in Earth Years |
| ------- | ----------------------------- |
| Mercury | 0.2408467                     |
| Venus   | 0.61519726                    |
| Earth   | 1.0                           |
| Mars    | 1.8808158                     |
| Jupiter | 11.862615                     |
| Saturn  | 29.447498                     |
| Uranus  | 84.016846                     |
| Neptune | 164.79132                     |
"""


from types import UnionType
from typing import Any


class SpaceAge:
    Planetary_ORBITAL_PERIODS = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }

    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_years = seconds / 31557600

    def __orbital_period(self, planet: str) -> float:
        return round(self.seconds / (31557600 * self.Planetary_ORBITAL_PERIODS[planet]), 2)

    def __getattribute__(self, name: str) -> Any:
        pass
        if name.startswith('on_'):
            planet = name[3:]
            if planet in self.Planetary_ORBITAL_PERIODS:
                return lambda: self.__orbital_period(planet)
        return super().__getattribute__(name)
