#!/usr/bin/node
const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c) {
    let line = '';

    if (!c) {
      c = 'X';
    }

    for (let j = 0; j < this.width; j++) {
      line += c;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
}

module.exports = Square;
