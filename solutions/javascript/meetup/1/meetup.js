
export const meetup = (year, month, dayword, strdow) => {
  const dow = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"].indexOf(strdow);
  var maybelast;
  var count = 0;
  const isleap = ((year&3)==0 && ((year%100) != 0 || (year%400) == 0));
  const nbdaybymonth = [31,isleap?29:28,31,30,31,30,31,31,30,31,30,31][month-1];
  const daycode = ["first","second","third","fourth","teenth","last"].indexOf(dayword);
  for (var d = 1 ; d <= nbdaybymonth ; d++ ){
    var tested_date = new Date(year,month-1,d);
    if (tested_date.getDay() == dow){
     switch (daycode) {
        case 4: 
        if ((d >= 13) && (d<=19)) {
          return tested_date;
        }
        break;
        case 5:
          maybelast = tested_date;
          break;
        default:
          if (count == daycode){
            return tested_date;
          }
          break;
      }
      count++;
    }
  }
  return maybelast;
};
