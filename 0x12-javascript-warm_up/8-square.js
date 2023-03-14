#!/usr/bin/node

const args = process.argv;
const intArg = parseInt(args[2]);

if (isNaN(intArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < intArg; i++) {
    console.log('X'.repeat(intArg));
  }
}
