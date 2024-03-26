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
  } else {
    const filmsData = JSON.parse(response.body).results;
    const moviesWithWedge = filmsData.filter((film) =>
      film.characters.includes(
        `https://swapi-api.alx-tools.com/api/people/${characterId}/`
      )
    );
    console.log(moviesWithWedge.length);
  }
});
