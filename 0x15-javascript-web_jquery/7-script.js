// Wait for the document to be ready
$(document).ready(function () {
  // Make a GET request to fetch character data
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function (response) {
      // Extract the character name from the response
      const characterName = response.name;

      // Display the character name in the <div> with ID 'character'
      $('#character').text(characterName);
    },
    error: function (error) {
      console.error('Error fetching character data:', error);
    }
  });
});
