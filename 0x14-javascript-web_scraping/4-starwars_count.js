#!/usr/bin/node
/*
A script that prints the number of movies where the
character “Wedge Antilles” is present.
*/

const request = require('request');
const characterId = 18;

request(process.argv[2], (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  const final = (JSON.parse(response.body)).results;
  let count = 0;
  for (let i = 0; i < final.length; i++) {
    if (final[i].characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      count++;
    }
  }
  console.log(count);
});
