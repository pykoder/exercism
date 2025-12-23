// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

const juices = {
    'Pure Strawberry Joy': 0.5,
    'Energizer': 1.5,
    'Green Garden': 1.5,
    'Tropical Island': 3.0,
    'All or Nothing': 5.0
};

/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */
export function timeToMixJuice(name) {
  return (name in juices)?juices[name]:2.5;
}

const lime_slices = {
  small: 6,
  medium: 8,
  large: 10
};

/**
 * Calculates the number of limes that need to be cut
 * to reach a certain supply.
 *
 * @param {number} wedgesNeeded
 * @param {string[]} limes
 * @returns {number} number of limes cut
 */
export function limesToCut(wedgesNeeded, limes) {
  var wedges = 0;
  var number = 0;
  for (const l of limes){
    if (wedges >= wedgesNeeded){
      break;
    }
    number++;
    wedges += lime_slices[l];
  }
  return number;
}

/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft
 * @param {string[]} orders
 * @returns {string[]} remaining orders after the time is up
 */
export function remainingOrders(timeLeft, orders) {
  while (timeLeft > 0){
    const juice = orders.shift();
    timeLeft -= timeToMixJuice(juice);
  }
  return orders;
}
