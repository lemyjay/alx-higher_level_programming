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
  const characters = (JSON.parse(response.body)).characters;
  // Call the function to print characters, starting from index 0
  printCharacters(characters, 0);
});

// Function to recursively print characters
function printCharacters (characters, index) {
  // Make a request to fetch information about the character at the given index
  request(characters[index], function (error, response, body) {
    // Check for errors in the request
    if (!error) {
      // Print the name of the character
      console.log(JSON.parse(body).name);

      // Check if there are more characters to print
      if (index + 1 < characters.length) {
        // Recursively call the function for the next character
        printCharacters(characters, index + 1);
      }
    }
  });
}
