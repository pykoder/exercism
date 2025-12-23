
export const COLORS = [
  'black',
  'brown',
  'red',
  'orange',
  'yellow',
  'green',
  'blue',
  'violet',
  'grey',
  'white',
];

export const decodedValue = (colors) => {
  return colors.slice(0,2).map((c) => COLORS.indexOf(c)).reduce((a,b) => a*10 + b, 0);
};
