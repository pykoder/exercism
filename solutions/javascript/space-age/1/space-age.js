const factor = {
  'mercury': 1.0 / (315576 * 0.2408467),
  'venus': 1.0 / (315576 * 0.61519726),
  'earth': 1.0 / 315576,
  'mars': 1.0 / (315576 * 1.8808158),
  'jupiter': 1.0 / (315576 * 11.862615),
  'saturn': 1.0 / (315576 * 29.447498),
  'uranus': 1.0 / (315576 * 84.016846),
  'neptune': 1.0 / (315576 * 164.79132),
}

export const age = (planet, age_in_seconds) => {
  return Math.round(age_in_seconds*factor[planet])/100;
};
