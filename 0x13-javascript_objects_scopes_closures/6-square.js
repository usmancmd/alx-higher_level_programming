#!/usr/bin/node

const square = require('./5-square.js');

module.exports = class Square extends square {
  charPrint (c) {
    super.print(c);
  }
};
