#!/usr/bin/node
const filesys = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (
  filesys.existsSync(fileA) &&
filesys.statSync(fileA).isFile &&
filesys.existsSync(fileB) &&
filesys.statSync(fileB).isFile &&
fileC !== undefined
) {
  const fileAContent = filesys.readFileSync(fileA);
  const fileBContent = filesys.readFileSync(fileB);
  const stream = filesys.createWriteStream(fileC);

  stream.write(fileAContent);
  stream.write(fileBContent);
  stream.end();
}
