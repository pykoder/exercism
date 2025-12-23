
export const gigasecond = (date) => {
  // getTime() returns milliseconds
  // hence we will be adding one gigasecond in ms
  return new Date(date.getTime()+1E12);
};
