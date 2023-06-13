#!/usr/bin/node
const Args = process.argv.length;
console.log(Args === 2 ? 'No argument' : `${process.argv[2]}`);
