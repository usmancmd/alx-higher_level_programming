#!/usr/bin/node
exports.callMeMoby = (a, b) => {
  for (let i = 0; i < a; i++) {
    b();
  }
};
