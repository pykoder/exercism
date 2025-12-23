export class Forth {
  constructor() {
    this.count = 0;
    this.lexer = {'+':'+', '-':'-', '*':'*', '/':'/',
      'dup': ':dup:',
      'drop': ':drop:',
      'swap': ':swap:',
      'over': ':over:',
    };
    this.commands = {
      '+': { 
        'code': () => {
        if (this._stack.length < 2){
          throw Error("Stack empty");
        }
        let a = this._stack.pop();
        let b = this._stack.pop();
        this._stack.push(a+b);
        }        
      },
      '-': { 
        'code': () => {
          if (this._stack.length < 2){
            throw Error("Stack empty");
          }
          let a = this._stack.pop();
          let b = this._stack.pop();
          this._stack.push(b-a);
        }        
      },
      '*': { 
        'code': () => {
          if (this._stack.length < 2){
            throw Error("Stack empty");
          }
          let a = this._stack.pop();
          let b = this._stack.pop();
          this._stack.push(a*b);
        }        
      },
      '/': { 
        'code': () => {
          if (this._stack.length < 2){
            throw Error("Stack empty");
          }
          let a = this._stack.pop();
          let b = this._stack.pop();
          if (a == 0){
            throw Error("Division by zero");
          }
          let res = b / a;
          let round = (res >= 0)?Math.floor:Math.ceil;
          this._stack.push(round(res));
        }        
      },
      ':dup:': { 
          'code': () => {
          if (this._stack.length < 1){
            throw Error("Stack empty");
          }
          let a = this._stack.pop();
          this._stack.push(a);
          this._stack.push(a);
        }        
      },
      ':drop:': { 
          'code': () => {
          if (this._stack.length < 1){
            throw Error("Stack empty");
          }
          this._stack.pop();
        }        
      },
      ':swap:': { 
          'code': () => {
          if (this._stack.length < 2){
            throw Error("Stack empty");
          }
          let a = this._stack.pop();
          let b = this._stack.pop();
          this._stack.push(a);
          this._stack.push(b);
        }        
      },
      ':over:': { 
        'code': () => {
            if (this._stack.length < 2){
              throw Error("Stack empty");
            }
            let a = this._stack.pop();
            let b = this._stack.pop();
            this._stack.push(b);
            this._stack.push(a);
            this._stack.push(b);
        }        
      },
    };
    this._stack = [];
  }

  execute(compiled) {
    compiled.forEach(
      (item) => {
        if (typeof item === 'number'){
          this._stack.push(item);
        }
        else if ('code' in item){
          item['code']();
        }
        else if ('custom' in item) {
          this.execute(item['custom']);
        }
      }
    );
  }

  compile(lexems){
    return lexems.map(
      (item) => {
        if (/[-+]?[0-9]+/.test(item)){
          return parseInt(item);
        }
        else if (item.toLowerCase() in this.lexer){
          let code = this.lexer[item.toLowerCase()];
          return this.commands[code];
        }
        else {
          throw Error("Unknown command");
        }
      }
    );
  }

  definition(input){
    let user_command = input.split(' ');
    let custom = `:${this.count}:`;
    this.count += 1;
    this.commands[custom] = { 
      'custom': this.compile(user_command.slice(2,-1)) 
    }
    this.lexer[user_command[1].toLowerCase()] = custom;
  }

  evaluate(input) {
    if (/^:\s[-+]?[0-9]+(\s\S+)+\s;$/.test(input)){
      throw Error("Invalid definition");
    }
    else if (/^:(\s\S+)+\s;$/.test(input)){
      this.definition(input);
    }
    else {
      let compiled = this.compile(input.split(' '));
      this.execute(compiled);
    }
  }

  get stack() {
    return this._stack;
  }
}
