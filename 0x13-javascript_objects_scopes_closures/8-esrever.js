#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight((list, num) => {
    list.push(num);
    return (list);
  }, []);
};
