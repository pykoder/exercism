//
// This is only a SKELETON file for the 'Complex Numbers' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class ComplexNumber {
  constructor(r,i) {
    this.re = r;
    this.im = i;
  }

  get real() {
    return this.re;
  }

  get imag() {
    return this.im;
  }

  add(other) {
    this.re += other.real;
    this.im += other.imag;
    return this;
  }

  sub(other) {
    this.re -= other.real;
    this.im -= other.imag;
    return this;
  }

  inv() {
    if (this.re == 0 & this.im == 0) {
      throw new Error("Divide by zero");
    }
    let c2 = this.re*this.re;
    let d2 = this.im*this.im;
    let den = 1/(c2 + d2);
    let cd = this.re*this.im;
    this.re = other.real*den;
    this.im = -other.imag*den;
    return this;
  }

  div(other) {
    if (other.real == 0 && other.imag == 0) {
      throw new Error("Divide by zero");
    }
    let c2 = other.real*other.real;
    let d2 = other.imag*other.imag;
    let den = 1/(c2 + d2);
    let cd = other.real*other.imag;
    let re = (other.real*this.re + other.imag*this.im)*den;
    let im = (-other.imag*this.re + other.real*this.im)*den;
    this.re = re;
    this.im = im;
    return this
  }

  mul(other) {
    let re = this.re * other.real - this.im * other.imag;
    let im = this.re * other.imag + this.im * other.real;
    this.re = re;
    this.im = im;
    return this;
  }

  get abs() {
    return Math.sqrt(this.re*this.re+this.im*this.im);
  }

  get conj() {
    this.im = 0-this.im;
    return this;
  }

  get exp() {
    let ea = Math.exp(this.re);
    let re = ea * Math.cos(this.im);
    let im = ea * Math.sin(this.im);
    this.re = re;
    this.im = im;
    return this;
  }
}
