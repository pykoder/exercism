
export class Squares {
  constructor(n) {
    this.n = n;
  }

  get sumOfSquares() {
    let n = this.n;
    return n*(n+1)*(2*n+1)/6;
  }

  get squareOfSum() {
    let n = this.n;
    let v = n*(n+1)/2;
    return v * v;
  }

  get difference() {
    return this.squareOfSum - this.sumOfSquares;
  }
}
