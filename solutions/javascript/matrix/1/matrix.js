export class Matrix {
  constructor(matrix) {
    this.matrix = matrix.split('\n').map(
      (line) => {
        return line.split(' ').map((item) => parseInt(item));}
    );
  }

  get rows() {
    return this.matrix.slice();
  }

  get columns() {
    var transposed = [];
    for (let j = 0; j < this.matrix[0].length; j++) {
      transposed.push([])
    }
    for (let i = 0; i < this.matrix.length; i++) {
      for (let j = 0; j < this.matrix[i].length; j++) {
        transposed[j].push(this.matrix[i][j]);
      }
    } 
    return transposed;
  }
}
