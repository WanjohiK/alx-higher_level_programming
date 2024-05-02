// Wait for the document to be fully loaded and ready
$(function () {
  // Define the API URL
  const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  // Make a GET request to the API using $.get()
  $.get(apiUrl, function (data, status) {
    // When the request is successful, set the character name in the HTML tag DIV#character
    $('DIV#character').text(data.name);
  });
});
