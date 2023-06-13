#!/usr/bin/node
const Args = process.argv.length;
console.log(Args === 3 ? `${process.argv[2]}` : 'No argument');
