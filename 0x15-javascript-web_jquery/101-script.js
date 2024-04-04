// Wait for the document to be fully loaded
$(document).ready(function () {
  // Add item to the list
  $('#add_item').click(function () {
    $('<li>Item</li>').appendTo('.my_list');
  });

  // Remove last item from the list
  $('#remove_item').click(function () {
    $('.my_list li:last-child').remove();
  });

  // Clear all items from the list
  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});
