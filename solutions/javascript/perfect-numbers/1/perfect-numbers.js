
export const classify = (number) => {
  if (!Number(number) || number <= 0){
    throw new Error('Classification is only possible for natural numbers.');
  }
  let n = 0;
  for (let x = 1 ; x < number ; x++){
    if (number%x == 0){
      n += x;
    }
  }
  return (number == n)?"perfect"
        :(n > number) ?"abundant"
        :"deficient";
};
