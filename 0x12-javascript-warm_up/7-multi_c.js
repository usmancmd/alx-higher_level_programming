#!/usr/bin/node
const Arg = process.argv[2];
if (Number(Arg)) {
  for (let i = 0; i < Arg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
