#!/usr/bin/node
const Args = process.argv[2];
console.log(typeof Args === 'undefined' ? 'No argument' : `${process.argv[2]}`);
