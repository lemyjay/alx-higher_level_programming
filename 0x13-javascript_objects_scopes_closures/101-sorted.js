#!/usr/bin/node

const { dict } = require('./101-data');

// Initialize an empty dictionary to store user ids by occurrence
const usersByOccurrence = {};

// Iterate over the initial dictionary to populate usersByOccurrence
for (const userId in dict) {
  const occurrences = dict[userId];
  if (!usersByOccurrence[occurrences]) {
    usersByOccurrence[occurrences] = [];
  }
  usersByOccurrence[occurrences].push(userId);
}

// Print the new dictionary
console.log(usersByOccurrence);
