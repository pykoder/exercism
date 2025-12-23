export class Clock {
  constructor(hour, minute) {
    if (minute === undefined){
      minute = 0;
    }
    this.hour = hour;
    this.minute = minute;
    this.canonicalize();
  }

  canonicalize() {
    // modulo of negative numbers is negative in JS ? Really ?
    var newminute = (this.minute<0)?((this.minute%60+60)%60):(this.minute%60);
    this.hour += (this.minute-newminute)/60;
  this.minute = newminute;
    this.hour = (this.hour<0)?((this.hour%24+24)%24):(this.hour%24);
  }

  formatxx(n) {
    return String(((n-n%10)/10))+n%10;
  }

  toString() {
    return this.formatxx(this.hour)+":"+this.formatxx(this.minute);
  }

  plus(minute) {
    this.minute += minute;
    this.canonicalize();
    return this;
  }

  minus(minute) {
    this.minute -= minute;
    this.canonicalize();
    return this;
  }

  equals(other) {
    return (this.hour == other.hour) && (this.minute == other.minute);
  }
}
