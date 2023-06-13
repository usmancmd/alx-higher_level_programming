#!/usr/bin/node
const num = Number(process.argv[2]);

function Factorial (n) {
  return n === 0 || isNaN(n) ? 1 : n * Factorial(n - 1);
}

console.log(Factorial(num));
