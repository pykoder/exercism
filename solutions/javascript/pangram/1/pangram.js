export const isPangram = (sentence) => {
  let letters = {};
  let count = 0;
  [...sentence].filter((c) => /[A-Za-z]/.test(c))
    .map((c) => c.toLowerCase())
    .forEach(
      (c) => {
        if (!(c in letters)) {
          count += 1;
          letters[c] = true;
        }
      });
  return count == 26;
};
