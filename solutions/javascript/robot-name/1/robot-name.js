
export var allnames = new Set([]);

function genname(){
    var l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    var res = l.charAt(Math.floor(Math.random()*l.length));
    res += l.charAt(Math.floor(Math.random()*l.length));
    var d = '0123456789';
    res += d.charAt(Math.floor(Math.random()*d.length));
    res += d.charAt(Math.floor(Math.random()*d.length));
    res += d.charAt(Math.floor(Math.random()*d.length));
    return res;
}

export class Robot {

    constructor() {
        this.reset();
    }

    get name(){
        return this._name;
    }

    reset(){
        do {
            this._name = genname();
        }
        while (allnames.has(this._name));
        allnames.add(this._name);
    }
}

Robot.releaseNames = () => { allnames = new Set([]); };
