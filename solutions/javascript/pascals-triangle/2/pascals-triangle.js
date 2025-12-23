
export const rows = (n) => {
  var res = [[1]];
  for (let i = 0 ; i < n-1 ; i++){
     var next = [...res[i],0];
     next = next.map(function(e, idx){
               return e + ((idx==0)?0:next[idx-1]);});
     res.push(next);
  }
  return (n==0)?[]:res;
}
