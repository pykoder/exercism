
export const isLeap = (year) => {
  // This is the Naive version, working fine
  // return ((year&3)==0 && ((year%100) != 0 || (year%400) == 0));

  // But version below is slightly faster on my system
  // (because it avoids one division, and divisions are realy expensive)
  if ((year&3)!=0) {
    return false;
  }
  var siecle = Math.floor(year / 100);
  if (siecle*100 != year){
    return true;
  }
  return (siecle&3)==0;


};
