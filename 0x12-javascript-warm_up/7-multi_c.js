#!/usr/bin/node
// A script that  prints x times “C is fun”
const arg1 = parseInt(process.argv[2]);

if (arg1) {
  for (let i = 0; i < arg1; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
