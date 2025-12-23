export const hey = (message) => {  

  const yelled = /^[^a-z]+$/.test(message) && /[A-Z]+/.test(message);
  const question = /[?]\s*$/.test(message);

  if (yelled && question){
    return "Calm down, I know what I'm doing!";
  }
  if (question){ 
    return "Sure.";
  }
  if (yelled){
    return "Whoa, chill out!";
  }
  if (/^\s*$/.test(message)){
    return "Fine. Be that way!";
  }
  return "Whatever."
};
