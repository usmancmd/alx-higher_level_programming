#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  list.forEach(count);
  function count (item) {
    if (item === searchElement) {
      i++;
    }
  }
  return i;
};
