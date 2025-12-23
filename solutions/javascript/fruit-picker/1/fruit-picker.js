/// <reference path="./global.d.ts" />
//
// @ts-check
//

import { checkStatus, checkInventory } from './grocer';

var status = false;

function callbackStatus(notification)
{
   switch (notification){
     case 'ONLINE':
       status = true;
       break;
     case 'OFFLINE':
       status = false;
       break;
   }
}


/**
 * Returns the service status as a boolean value
 * @return {boolean}
 */
export function isServiceOnline() {
  checkStatus(callbackStatus);
  return status;
}

/**
 * Pick a fruit using the checkInventory API
 *
 * @param {string} variety
 * @param {number} quantity
 * @param {InventoryCallback} action
 * @return {AvailabilityAction} the result from checkInventory
 */
export function pickFruit(variety, quantity, action) {
  const query = {
    variety: variety,
    quantity: quantity,
  };
  return checkInventory(query, action);
}

/**
 * This is a callback function to be passed to the checkInventory API
 * handles the next step once the inventory is known
 * @param {string | null} err
 * @param {boolean} isAvailable
 * @return {AvailabilityAction} whether the fruit was purchased 'PURCHASE' or 'NOOP'
 */
export function purchaseInventoryIfAvailable(err, isAvailable) {
  if (err) {
    throw new Error('Availability Error');
  }
  if (isAvailable) {
    return "PURCHASE";
  };
  return "NOOP";
}

/**
 * Pick a fruit, and if it is available, purchase it
 *
 * @param {string} variety
 * @param {number} quantity
 * @return {AvailabilityAction} whether the fruit was purchased 'PURCHASE' or 'NOOP'
 */
export function pickAndPurchaseFruit(variety, quantity) {
  return pickFruit(variety, quantity, purchaseInventoryIfAvailable);
}
