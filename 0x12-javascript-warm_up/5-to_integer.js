#!/usr/bin/node
const Arg = Math.floor(process.argv[2]);
if (Number(Arg)) {
  console.log(`My number: ${Arg}`);
} else {
  console.log('Not a number');
}
