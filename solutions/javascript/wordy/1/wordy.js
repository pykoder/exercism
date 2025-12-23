export const answer = (message) => {
  var r = /^What is (-?[1-9][0.9]*)[?]$/.exec(message);
  if (r){
    return Number(r[1]);
  }
  r = /^What is ([-]?[1-9][0-9]*) plus ([-]?[1-9][0-9]*)[?]$/.exec(message);
  if (r){
      return Number(r[1])+Number(r[2]);
  }
  r = /^What is ([-]?[1-9][0-9]*) minus ([-]?[1-9][0-9]*)[?]$/.exec(message);
  if (r){
      return Number(r[1])-Number(r[2]);
  }
  r = /^What is ([-]?[1-9][0-9]*) multiplied by ([-]?[1-9][0-9]*)[?]$/.exec(message);
  if (r){
      return Number(r[1])*Number(r[2]);
  }
  r = /^What is ([-]?[1-9][0-9]*) divided by ([-]?[1-9][0-9]*)[?]$/.exec(message);
  if (r){
      return Number(r[1])/Number(r[2]);
  }
  r = /^What is ([-]?[1-9][0-9]*) plus ([-]?[1-9][0-9]*) plus ([-]?[1-9][0-9]*)[?]$/.exec(message);
  if (r){
      return Number(r[1])+Number(r[2])+Number(r[3]);
  }
  r = /^What is ([-]?[1-9][0-9]*) minus ([-]?[1-9][0-9]*) minus ([-]?[1-9][0-9]*)[?]$/.exec(message);
  if (r){
      return Number(r[1])-Number(r[2])-Number(r[3]);
  }
  r = /^What is ([-]?[1-9][0-9]*) plus ([-]?[1-9][0-9]*) minus ([-]?[1-9][0-9]*)[?]$/.exec(message);
  if (r){
      return Number(r[1])+Number(r[2])-Number(r[3]);
  }
  r = /^What is ([-]?[1-9][0-9]*) minus ([-]?[1-9][0-9]*) plus ([-]?[1-9][0-9]*)[?]$/.exec(message);
  if (r){
      return Number(r[1])-Number(r[2])+Number(r[3]);
  }
  r = /^What is ([-]?[1-9][0-9]*) multiplied by ([-]?[1-9][0-9]*) multiplied by ([-]?[1-9][0-9]*)[?]$/.exec(message);
  if (r){
      return Number(r[1])*Number(r[2])*Number(r[3]);
  }
  r = /^What is ([-]?[1-9][0-9]*) divided by ([-]?[1-9][0-9]*) divided by ([-]?[1-9][0-9]*)[?]$/.exec(message);
  if (r){
      return Number(r[1])/Number(r[2])/Number(r[3]);
  }
  r = /^What is ([-]?[1-9][0-9]*) plus ([-]?[1-9][0-9]*) multiplied by ([-]?[1-9][0-9]*)[?]$/.exec(message);
  if (r){
      return (Number(r[1])+Number(r[2]))*Number(r[3]);
  }
  r = /^What is ([-]?[1-9][0-9]*) multiplied by ([-]?[1-9][0-9]*) minus ([-]?[1-9][0-9]*)[?]$/.exec(message);
  if (r){
      return Number(r[1])-Number(r[2])+Number(r[3]);
  }
  r = /^What is ([-]?[1-9][0-9]*) (plus|minus|multiplied by|divided by)?$/.exec(message);
  if (r){
    throw new Error("Syntax error");
  }
  r = /^What is ([-]?[1-9][0-9]*) cubed[?]$/.exec(message);
  if (r){
    throw new Error("Unknown operation");
  }
  r = /^Who is /.exec(message);
  if (r){
    throw new Error("Unknown operation");
  }
  throw new Error("Syntax error");
};
