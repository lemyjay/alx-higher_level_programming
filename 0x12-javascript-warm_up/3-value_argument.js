#!/usr/bin/node
// A script that prints a message depending on the number of arguments passed.
const argument = process.argv[2];

if (argument) {
  console.log(argument);
} else {
  console.log('No argument');
}
