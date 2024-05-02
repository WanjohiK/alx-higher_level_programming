// Wait for the document to be fully loaded and ready
$(function () {
  // Define the API URL
  const apiUrl = 'https://stefanbohacek.com/hellosalut/?lang=fr';

  // Make a GET request to the API using $.get()
  $.get(apiUrl, function (data) {
    // Set the "hello" text from the API response in the HTML tag DIV#hello
    $('DIV#hello').text(data.hello);
  });
});
