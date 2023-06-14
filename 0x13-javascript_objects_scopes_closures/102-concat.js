#!/usr/bin/node
const fileSystem = require('fs');
const a = fileSystem.readFileSync(process.argv[2], 'utf8');
const b = fileSystem.readFileSync(process.argv[3], 'utf8');
fileSystem.writeFileSync(process.argv[4], a + b);
