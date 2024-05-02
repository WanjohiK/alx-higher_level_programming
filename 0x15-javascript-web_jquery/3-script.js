// Wait for the document to be fully loaded and ready
$(function () {
  // Add a click event listener to the <header> element
  $('header').click(function () {
    // When the <header> is clicked, select the <div> with id "red_header"
    // and change its text color to red (#FF0000)
    $('DIV#red_header').css('color', '#FF0000');
    // Add the class "red" to the <header> element
    $('header').addClass('red');
  });
});
