#!/usr/bin/node

const args = process.argv;
const intArg = parseInt(args[2]);
if (isNaN(intArg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < intArg; i++) {
    console.log('C is fun');
  }
}
