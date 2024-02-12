#!/usr/bin/node
// A script that prints a message depending on the number of arguments passed.
const numArguments = process.argv.length - 2;

if (numArguments === 0) {
  console.log('No argument');
} else if (numArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
