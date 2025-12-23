export const compute = (one, two) => {
  if ((one.length == 0) && (two.length == 0)){
    return 0;
  }
  if (one.length == 0){
    throw new Error('left strand must not be empty');
  }
  if (two.length == 0){
    throw new Error('right strand must not be empty');
  }
  if (one.length != two.length){
    throw new Error('left and right strands must be of equal length');
  }
  var count = 0;
  for (let i in one){
    if (one[i] != two[i]) count++;
  }
  return count;
};
