// Wait for the document to be fully loaded
$(document).ready(function () {
  // Function to fetch translation
  function fetchTranslation () {
    // Get the language code entered by the user
    const languageCode = $('#language_code').val();

    // Check if language code is empty or invalid
    if (!languageCode) {
      $('#hello').text('Please enter a valid language code');
      return;
    }

    // Make GET request to fetch translation
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      // Check if translation data is valid
      if (data && data.hello) {
        // Update the content of the div with the fetched translation
        $('#hello').text(data.hello);
      } else {
        $('#hello').text('Translation not found');
      }
    }).fail(function () {
      // Handle failed request
      $('#hello').text('Error fetching translation');
    });
  }

  // Handle click event on btn_translate
  $('#btn_translate').click(fetchTranslation);

  // Handle keypress event on language_code input (ENTER key)
  $('#language_code').keypress(function (event) {
    // Check if ENTER key is pressed (key code 13)
    if (event.keyCode === 13) {
      fetchTranslation(); // Fetch translation
    }
  });
});
