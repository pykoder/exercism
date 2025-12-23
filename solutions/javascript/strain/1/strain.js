export const keep = (list, filter) => {
  // Of course actually using filter would be much master
  // return list.filter((x) => filter(x));
  
  var res = [];
  list.forEach((x) => {
    if (filter(x)){
      res.push(x);
    }
  });
  return res;
};

export const discard = (list, filter) => {
  return keep(list, (x) => !filter(x));
};
