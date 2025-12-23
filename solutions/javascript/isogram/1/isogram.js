export const isIsogram = (word) => {
  if (word.length == 0) return true;
  var h = {};
  var isogram = true;
  [...word.toLowerCase()].filter((x) => /[a-z]/.test(x)).forEach(
    (x) => {
      if (h[x]){ isogram = false; }
      h[x] = true;
    });
  return isogram;
};
