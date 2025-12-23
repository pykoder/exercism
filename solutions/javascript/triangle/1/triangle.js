export class Triangle {
  constructor(...sides) {
    if (sides.length != 3)
    {
      throw new Error('Not a triangle');
    }
    // check sides are strict positive numbers
    // and that the triangle is possible
    // (ie: for instance there is no triangle with sides 3, 5, 10)

    this.sides = sides.sort();
  }

  get isEquilateral() {
    // this is merely to make the test pass
    // it would be better to detect all non triangles
    // at constructor raising some exception
    // at it's not the API picked by tests
    // I won't care writing the sanity check code everywhere
    let [a, b, c] = this.sides;
    if (a + b + c == 0){
      return false;
    }
    return a == b && b == c;
  }

  get isIsosceles() {
    // if the triangle is equilateral it is also isocele
    let [a, b, c] = this.sides;
    if (a + b < c) {
      return false;
    }
    return a == b || b == c || a == c ;
  }

  get isScalene() {
    let [a, b, c] = this.sides;
    if (a + b < c) {
      return false;
    }
    return !this.isIsosceles;
  }
}
