export class Bowling {

  constructor(n = 10) {
    this.n = n;
    this.turn = 0;
    this.first = true;
    this.strike = false;
    this.spear = false;
    this.rolls = [];
  }

  roll(pins) {
    if (pins < 0) {
      throw Error("Negative roll is invalid");
    }
    if (pins > 10) {
      throw Error("Pin count exceeds pins on the lane");
    }
    if (this.turn < this.n) {
      if (this.first) {
        this.rolls.push(pins);
        this.spear = false;
        if (pins == 10){
          this.turn += 1;
          this.strike = true;
        }
        else {
          this.strike = false;
          this.first = false;
        }
      }
      else {
        this.strike = false;
        let turn_pins = this.rolls.slice(-1)[0]+pins;
        if (turn_pins > 10){
          throw Error("Pin count exceeds pins on the lane");
        }
        this.spear = turn_pins == 10;
        this.rolls.push(pins);
        this.turn += 1;
        this.first = true;
      }
    }
    // Maybe bonus rolls after a spear or strike on last throw
    else {
      if (this.turn == this.n) {
        if (this.strike){
          if (this.first){
            this.first = false;
            this.rolls.push(pins);
          }
          else {
            if (this.rolls.slice(-1)[0] < 10 && this.rolls.slice(-1)[0]+pins > 10){
              throw Error("Pin count exceeds pins on the lane");
            }
            this.rolls.push(pins);
            this.strike = false;
          }
        }
        else if (this.spear){
          this.rolls.push(pins);
          this.spear = false;
        }
        else {
          throw Error("Cannot roll after game is over");
        }
      }
      else {
        throw Error("Cannot roll after game is over");
      }
    }
  }

  score() {
    if (this.turn < this.n || this.strike || this.spear){
      throw Error("Score cannot be taken until the end of the game");
    }
    let score = 0;
    let start = 0;
    for (let turn = 0; turn < this.n; turn++) {
      // strike
      if (this.rolls[start+0] == 10){
        score += this.rolls[start+0] + this.rolls[start+1] + this.rolls[start+2];
        start += 1;
      }
      // spare
      else if (this.rolls[start+0] + this.rolls[start+1] == 10) {
        score += this.rolls[start+0] + this.rolls[start+1] + this.rolls[start+2];
        start += 2;
      }
      else {
        score += this.rolls[start+0] + this.rolls[start+1];
        start += 2;
      }
    }
    return score;
  }
}
