#!/usr/bin/node
// A script that tries to convert the first argument to an integer and then prints it
const arg1 = parseInt(process.argv[2]);

if (arg1) {
  console.log('My number:', arg1);
} else {
  console.log('Not a number');
}
