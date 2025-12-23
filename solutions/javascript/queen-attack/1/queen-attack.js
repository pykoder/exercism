
export class QueenAttack {
  constructor(board)
  {
    var black = [0, 3];
    if (board && "black" in board){
      black = board["black"];
      if (black[0] < 0 || black[0] > 7||black[1] < 0 || black[1] > 7){
          throw new Error('Queen must be placed on the board');
      }
    }
    this.black = black;

    var white = [7, 3];
    if (board && "white" in board){
      white = board["white"];
      if (white[0] < 0 || white[0] > 7||white[1] < 0 || white[1] > 7){
          throw new Error('Queen must be placed on the board');
      }
    }
    if ((white[0] == black[0]) && (white[1] == black[1])){
      throw new Error('Queens cannot share the same space');
    }

    this.white = white;
  }

  toString() {
    var res = [];
    var [y0, x0] = this.black;
    var [y1, x1] = this.white;
    for (let y = 0 ; y < 8 ; y++){
      var line = [];
      for (let x = 0 ; x < 8 ; x++){
        var c = '_';
        if ((x == x0) && (y==y0)){ c = 'B'; }
        if ((x == x1) && (y==y1)){ c = 'W'; }
        line.push(c);
      }
      res.push(line.join(' '));
    }
    return res.join('\n');
  }

  get canAttack() {
    var [x0, y0] = this.black;
    var [x1, y1] = this.white;
    if ((x0 == x1)||(y0 == y1)||(x0-x1==y0-y1)||(x0-x1==y1-y0)){
      return true
    }
    return false;
  }
}
