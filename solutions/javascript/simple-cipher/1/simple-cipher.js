
function l2n(x) {
  return x.charCodeAt() - 'a'.charCodeAt();
}

function n2l(x) {
  return String.fromCharCode('a'.charCodeAt() + (26 + x)%26);
}


export class Cipher {
  constructor(key) {
    if (!key){
      key = '';
      var characters = 'abcdefghijklmnopqrstuvwxy';
      for (var x = 0 ; x < 100 ; x++){
        key += characters.charAt(Math.floor(Math.random() * 
 characters.length));
      }
    }
    this._key = key;
  }

  encode(message) {
    var res = '';
    for (var idx in message){
      res += n2l(l2n(message[idx]) + l2n(this._key[idx%this._key.length]));
    }
    return res;
  }

  decode(message) {
    var res = '';
    for (var idx in message){
      res += n2l(l2n(message[idx]) - l2n(this._key[idx%this._key.length]));
    }
    return res;
  }

  get key() {
    return this._key;
  }
}
