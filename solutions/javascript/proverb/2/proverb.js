export const proverb = (...args) => {
  if (args.length == 0){
    return "";
  }
  var qualifier = "";
  if (typeof args.slice(-1)[0] == "object"){
    let x = args.pop();
    qualifier = x.qualifier+" ";
  }

  var text = "";
  for (let i = 0 ; i < args.length-1 ; i++){
    const one = args[i];
    const two = args[i+1];
    text += `For want of a ${one} the ${two} was lost.\n`
  }
  text += `And all for the want of a ${qualifier}${args[0]}.`
  return text;
};
