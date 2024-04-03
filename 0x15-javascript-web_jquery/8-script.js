// Wait for the document to be ready
$(document).ready(function () {
  // Make a GET request to fetch movie data
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (response) {
      // Get the list of movies from the response
      const movies = response.results;

      // Iterate through each movie and add its title to the list
      movies.forEach(function (movie) {
        const title = movie.title;
        $('#list_movies').append('<li>' + title + '</li>');
      });
    },
    error: function (error) {
      console.error('Error fetching movie data:', error);
    }
  });
});
