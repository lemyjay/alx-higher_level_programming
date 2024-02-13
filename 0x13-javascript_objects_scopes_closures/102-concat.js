#!/usr/bin/node
const fs = require('fs');

// Get file paths from command line arguments
const [, , fileA, fileB, fileC] = process.argv;

// Read the contents of fileA and fileB
const contentA = fs.readFileSync(fileA, 'utf8');
const contentB = fs.readFileSync(fileB, 'utf8');

// Concatenate the contents of fileA and fileB
const concatenatedContent = contentA + contentB;

// Write the concatenated content to fileC
fs.writeFileSync(fileC, concatenatedContent);
