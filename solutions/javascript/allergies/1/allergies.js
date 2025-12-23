
const allergens = [
  'eggs',
  'peanuts',
  'shellfish',
  'strawberries',
  'tomatoes',
  'chocolate',
  'pollen',
  'cats',
];

var allergen_to_score = {};
var score_to_allergen = {};

for (let i in allergens){
  allergen_to_score[allergens[i]] = 2**i;
  score_to_allergen[2**i] = allergens[i];
}

export class Allergies {
  constructor(score) {
    this.score = score;
  }

  list() {
    var res = [];
    for (let x in score_to_allergen){
      if ((x & this.score) != 0){
        res.push(score_to_allergen[x]);
      }
    }
    return res;
  }

  allergicTo(allergen) {
    return (allergen_to_score[allergen] & this.score) != 0;
  }
}
