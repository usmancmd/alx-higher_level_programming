#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return (
    list.reduce((count, number) => {
      if (number === searchElement) {
        count += 1;
      }
      return (count);
    }, 0)
  );
};
