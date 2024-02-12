//#!/usr/bin/node
// A script that prints the first argument passed to it.
const argument = process.argv[2];

if (argument) {
  console.log(argument);
} else {
  console.log('No argument');
}
