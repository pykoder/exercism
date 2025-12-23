//
// This is only a SKELETON file for the 'Bank Account' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class BankAccount {
  constructor() {
    this.active = false;
  }

  open() {
    if (this.active){
      throw new ValueError('This account is already open');
    }
    this.credit = 0;
    this.active = true;
  }

  close() {
    if (!this.active){
      throw new ValueError('This account is closed');
    }
    this.active = false;
  }

  deposit(amount) {
    if (!this.active){
      throw new ValueError('This account is closed');
    }
    if (amount <= 0){
      throw new ValueError('Cannot deposit negative amount, use withdraw instead');
    }
    this.credit += amount;
  }

  withdraw(amount) {
    if (!this.active){
      throw new ValueError('This account is closed');
    }
    if (amount <= 0){
      throw new ValueError('Cannot withdraw negative amount');
    }
    if (amount > this.credit){
      throw new ValueError('Cannot withdraw more than current credit');
    }
    this.credit -= amount;
  }

  get balance() {
    if (!this.active){
      throw new ValueError('This account is closed');
    }
    return this.credit;
  }
}

export class ValueError extends Error {
  constructor() {
    super('Bank account error');
  }
}
