#!/usr/bin/node
exports.addMeMaybe = (a, b) => {
  let num = a;
  num++;
  return b(num);
};
