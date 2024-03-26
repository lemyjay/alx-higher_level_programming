#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.
const fs = require('fs');
const request = require('request');
const _url = process.argv[2];
const fName = process.argv[3];

request(_url, (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  const content = response.body;
  fs.writeFile(fName, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
