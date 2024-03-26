#!/usr/bin/node
// A script that that prints all characters of a Star Wars movie.
const request = require('request');
const _url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(_url, (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  const final = (JSON.parse(response.body)).characters;
  for (let i = 0; i < final.length; i++) {
    request(final[i], (errorInner, responseInner) => {
      if (errorInner) {
        console.error(errorInner);
        return;
      }
      const name = (JSON.parse(responseInner.body)).name;
      console.log(name);
    });
  }
});
