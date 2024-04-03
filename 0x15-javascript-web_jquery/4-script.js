// Wait for the document to be ready
$(document).ready(function () {
  // Add a click event listener to the div with ID 'toggle_header'
  $('#toggle_header').click(function () {
    // Toggle the class 'red' on the <header> element
    $('header').toggleClass('red green');
  });
});
