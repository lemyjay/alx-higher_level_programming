#!/usr/bin/node
/*
A script that prints the title of a Star Wars movie where
the episode number matches given integer.
*/

const request = require('request');
const _url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(_url, (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  const final = JSON.parse(response.body);
  console.log(final.title);
});
