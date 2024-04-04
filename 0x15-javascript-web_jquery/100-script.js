// Wait for the document to be fully loaded
document.addEventListener('DOMContentLoaded', function () {
  // Select the <header> element using querySelector
  const headerElement = document.querySelector('header');

  // Check if the header element is found
  if (headerElement) {
    // Update the text color to red (#FF0000)
    headerElement.style.color = '#FF0000';
  } else {
    console.error('Header element not found');
  }
});
