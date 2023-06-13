#!/usr/bin/node
const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

function add (a, b) {
  return (Number(a) + Number(b));
}

console.log(add(num1, num2));
