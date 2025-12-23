// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Determines whether or not you need a licence to operate a certain kind of vehicle.
 *
 * @param {string} kind
 * @returns {boolean} whether a license is required
 */
export function needsLicense(kind) {
    return ["car", "truck"].indexOf(kind) > -1;
}

/**
 * Helps choosing between two options by recommending the one that
 * comes first in dictionary order.
 *
 * @param {string} option1
 * @param {string} option2
 * @returns {string} a sentence of advice which option to choose
 */
export function chooseVehicle(...options) {
  options.sort();
  return `${options[0]} is clearly the better choice.`;
}

/**
 * Calculates an estimate for the price of a used vehicle in the dealership
 * based on the original price and the age of the vehicle.
 *
 * @param {number} originalPrice
 * @param {number} age
 * @returns expected resell price in the dealership
 */
export function calculateResellPrice(originalPrice, age) {
  var i = 0;
  if (age>10){i=3;}else if (age>=3){i=2;}else if(age>0){i=1}
  var rebate = [1.0, 0.8, 0.7, 0.5];
  // or (nice and shorter but no condition):
  // var i = (age > 0)+(age >= 3)+(age > 10);
  return originalPrice * rebate[i];
}
