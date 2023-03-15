#!/usr/bin/node

const args = process.argv;
if (args <= 3) {
  console.log(0);
} else {
  args.map(Number)
    .slice(2, args.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
