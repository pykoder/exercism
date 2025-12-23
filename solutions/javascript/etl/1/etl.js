
export const transform = (old) => {
  var transformed = {};
  for (let value in old){
    old[value].forEach( (letter) => {
      transformed[letter.toLowerCase()] = Number(value);
    }
    ); 
  }
  return transformed;
};
