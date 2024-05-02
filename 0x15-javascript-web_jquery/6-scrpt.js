// Wait for the document to be fully loaded and ready
$(function () {
  // Add a click event listener to the DIV#add_item element
  $('DIV#add_item').click(function () {
    // update header to New header
    $('header').text('New Header!!!');
  });
});
