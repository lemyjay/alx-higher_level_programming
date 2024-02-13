#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 & h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let line = '';

    for (let j = 0; j < this.width; j++) {
      line += 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
