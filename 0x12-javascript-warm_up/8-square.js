#!/usr/bin/node
const Size = process.argv[2];
if (Number(Size)) {
  for (let i = 0; i < Size; i++) {
    let square = '';
    for (let i = 0; i < Size; i++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
