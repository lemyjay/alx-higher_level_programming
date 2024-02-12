#!/usr/bin/node
// A script that searches for the second biggest integer in the list of arguments.
const count = process.argv.length;

if (count > 3) {
  const array = [];
  for (let i = 2; i < count; i++) {
    array.push(parseInt(process.argv[i]));
  }
  array.sort((a, b) => b - a);
  console.log(array[1]);
} else {
  console.log('0');
}
