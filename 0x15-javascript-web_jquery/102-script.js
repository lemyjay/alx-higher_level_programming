$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();

    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      type: 'GET',
      data: { lang: languageCode },
      success: function (response) {
        console.log(response); // Log the response for debugging
        $('#hello').text(response.hello);
      },
      error: function (xhr, status, error) {
        console.error('Error:', error); // Log the error for debugging
        $('#hello').text('Error fetching translation');
      }
    });
  });
});
