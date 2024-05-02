// Wait for the document to be fully loaded and ready
$(function () {
  // Define the API URL
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

  // Make a GET request to the API using $.get()
  $.get(apiUrl, function (data) {
    // Access the movie titles from the API response
    const titles = data.results;

    // Iterate through the list of movie titles
    for (let i = 0; i < titles.length; i++) {
      // Append each movie title as a list item to the UL#list_movies element
      $('UL#list_movies').append('<li>' + titles[i].title + '</li>');
    }
  });
});
