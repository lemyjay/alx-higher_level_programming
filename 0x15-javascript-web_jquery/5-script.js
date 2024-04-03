// Wait for the document to be ready
$(document).ready(function () {
  // Add a click event listener to the div with ID 'add_item'
  $('#add_item').click(function () {
    // Create a new <li> element with text "Item"
    const newItem = $('<li>Item</li>');

    // Append the new <li> element to the UL with class 'my_list'
    $('ul.my_list').append(newItem);
  });
});
