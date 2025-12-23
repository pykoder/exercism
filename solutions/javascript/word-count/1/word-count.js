
export const countWords = (message) => {
  var h = {};
  do {
    const i = message.search(/[^\w\d']|$/);
    //console.log(i);
    if (i){
      let word = message.substring(0,i).toLowerCase();
      if (/^['].*[']$/.test(word)){
        word = word.substring(1,word.length-1);
      }
      // console.log(word);
      if (!(word in h)){
        h[word] = 0;
      }
      h[word] = h[word] + 1;
    }
    message = message.substring(i+1, message.length);
  } while (message.length > 0);
  return h;
};
