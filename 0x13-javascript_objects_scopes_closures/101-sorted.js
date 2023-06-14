#!/usr/bin/node
const dict = require('./101-data.js').dict;
const NewDict = {};
for (const key in dict) {
  if (typeof NewDict[dict[key]] === 'undefined') {
    NewDict[dict[key]] = [key];
  } else {
    NewDict[dict[key]].push(key);
  }
}
console.log(NewDict);
