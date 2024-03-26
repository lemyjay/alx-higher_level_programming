#!/usr/bin/node
// A script that that prints all characters of a Star Wars movie.
const request = require('request');
const _url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(_url, (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  // Getting a list of characters
  const final = (JSON.parse(response.body)).characters;

  // Iterating the list, is a list of links and performing requests on each
  for (let i = 0; i < final.length; i++) {
    request(final[i], (errorInner, responseInner) => {
      if (errorInner) {
        console.error(errorInner);
        return;
      }
      // Getting and print the name of character for each link in the list
      const name = (JSON.parse(responseInner.body)).name;
      console.log(name);
    });
  }
});
