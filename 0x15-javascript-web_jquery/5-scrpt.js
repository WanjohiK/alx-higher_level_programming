// Wait for the document to be fully loaded and ready
$(function () {
  // Add a click event listener to the DIV#add_item element
  $('DIV#add_item').click(function () {
    // Select the <ul> element with the class "my_list" and append a new <li> item
    $('UL.my_list').append('<li>Item</li>');
  });
});
