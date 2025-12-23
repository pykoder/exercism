//
// This is only a SKELETON file for the 'Secret Handshake' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const commands = (x) => {
  var res = [];
  if (x & 1) res.push("wink");
  if (x & 0b10) res.push("double blink");
  if (x & 0b100) res.push("close your eyes");
  if (x & 0b1000) res.push("jump");
  if (x & 0b10000) res.reverse();
  return res;
};
