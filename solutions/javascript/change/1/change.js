
export class Change {

  calculate(coinArray, target) {
      if (target < 0) {
        const message = 'Negative totals are not allowed.';
        throw new Error(message);
      }
      try {
        //console.log("==================================");
        this.best = null;
        coinArray.reverse();
        this.change(coinArray, target, []);
        this.best.reverse();
        return this.best;
      }
      catch (error) {
        const message = `The total ${target} cannot be represented in the given currency.`;
        throw new Error(message);
      }
  }

  change(ca, x, res) {
    //console.log(ca, x, res, "=", this.best);
    if (this.best && res.length >= this.best.length){
      return;
    }
    if (x == 0) {
      this.best = [...res];
      //console.log("Got result:", ca, x, res, "=", this.best);
      return;
    }
    if (ca.length == 0) {
      throw new Error();
    }
    var [h, ...rest] = ca;
    if (x >= h) {
      try {
        res.push(h);
        this.change(ca, x-h, res);
      }
      catch (error) {
      }
      res.pop();
    }
    try {
      return this.change(rest, x, res);
    }
    catch (error) {
    }
    if (this.best == null) {
      throw new Error();
    }
} 

}
