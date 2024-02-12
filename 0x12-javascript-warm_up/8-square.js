#!/usr/bin/node
// A script that  prints a square
const arg1 = parseInt(process.argv[2]);

if (arg1) {
  for (let i = 0; i < arg1; i++) {
    let line = '';
    for (let j = 0; j < arg1; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
