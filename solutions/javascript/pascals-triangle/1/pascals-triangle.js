export const rows = (n) => {
  var res = [];
  var pre = [1];
  console.log("=========="+n)
  for (let height = 0 ; height < n ; height++){
    console.log("+++height="+height, "pre="+pre, "n="+n);
    res.push(pre);
    var next = [1];
    for (let i = 0 ; i < height ; i++){
      console.log("---",height, i, pre[i-1], pre[i]);
      next.push(pre[i]+pre[i+1]);
    }
    next.push(1);
    pre = next;
  }
  console.log(res);
  return res;
};
