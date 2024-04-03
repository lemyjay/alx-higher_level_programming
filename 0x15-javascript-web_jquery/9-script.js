// Make a GET request to fetch translation data
$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  method: 'GET',
  success: function (response) {
    // Display the translation in the <div> with ID 'hello'
    $('#hello').text(response.hello);
  },
  error: function (error) {
    console.error('Error fetching translation:', error);
  }
});
