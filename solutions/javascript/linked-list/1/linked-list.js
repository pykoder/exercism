class Node {
}


export class LinkedList {
 
  constructor() {
    this.top = new Node();
    this.bottom = new Node();
    this.top.next = this.bottom;
    this.top.prev = this.top;
    this.bottom.prev = this.top;
    this.bottom.next = this.bottom;
    this._count = 0;
  }

  push(value) {
    var n = new Node();
    n.value = value;
    n.prev = this.top;
    n.next = this.top.next;
    this.top.next.prev = n;
    this.top.next = n;
    this._count++;
  }

  pop() {
    var n = this.top.next;
    this.top.next = n.next;
    n.next.prev = this.top;
    delete n.next;
    delete n.prev;
    this._count--;
    return n.value;
  }

  unshift(value) {
    var n = new Node();
    n.value = value;
    this.bottom.prev.next = n;
    n.next = this.bottom;
    n.prev = this.bottom.prev;
    this.bottom.prev = n;
    this._count++;
  }

  shift() {
    var n = this.bottom.prev;
    this.bottom.prev = n.prev;
    n.prev.next = this.bottom;
    delete n.next;
    delete n.prev;
    this._count--;
    return n.value;
  }

  delete(value) {
    var n = this.top.next;
    while (n != this.bottom){
      if (n.value == value) {
        var prev = n.prev;
        prev.next = n.next;
        var next = n.next;
        next.prev = n.prev;
        delete n.next;
        delete n.prev;
        this._count--;
        return;
      }
      n = n.next;
    }
  }

  count() {
    return this._count;
  }
}
