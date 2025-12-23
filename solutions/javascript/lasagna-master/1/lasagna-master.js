/// <reference path="./global.d.ts" />

import { nextTick } from "process";

// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

 export function cookingStatus(timer)
 {
    if (timer == undefined) return 'You forgot to set the timer.';
    if (timer == 0) return "Lasagna is done.";
    return 'Not done, please wait.';
 }
 
 
 export function preparationTime(layers, timeperlayer = 2)
 {
    return layers.length * timeperlayer;
 }

 export function quantities(layers)
 {
    var noodles = 0.0;
    var sauce = 0.0;
    layers.forEach((item) => {
        if (item === "noodles") {
            noodles += 50;
        }
        else if (item === "sauce") {
            sauce += 0.2;
        }
    });
    return {sauce: sauce, noodles: noodles};
 }

 export function addSecretIngredient(friendList, myList)
 {
    myList.push(friendList[friendList.length-1]);
 }

 export function scaleRecipe(recipe, people)
 {
     for (let x in recipe){
         recipe[x] *= people/2;
     }
     return recipe;
 }