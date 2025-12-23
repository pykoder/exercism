export class GradeSchool {

  constructor(){
    this.register = {};
  }

  roster() {
    var result = {};
    Object.entries(this.register).forEach(
      (item) => {
        if (!result.hasOwnProperty(item[1])) {
          result[item[1]] = [];
        }
        result[item[1]].push(item[0]);
      });
    Object.keys(result).forEach(
      (grade) => {
        result[grade].sort();
      }
    );
    return result;
  }

  add(name, grade) {
    this.register[name] = grade;
  }

  grade(grade) {
    var result = [];
    Object.entries(this.register)
    .filter((item) => { return item[1] == grade; })
    .forEach(
      (item) => {
        result.push(item[0]);
      });
    return result.sort();
  }
}
