'use strict'; // Enable strict mode

$(() => { // Execute when the document is ready
  // Function to translate and display the "hello" message
  const translateHello = () => {
    const BASE_URL = 'https://fourtonfish.com';
    const code = $('INPUT#language_code').val();

    // Make a GET request to the API to fetch translation data
    $.get(`${BASE_URL}/hellosalut/?lang=${code}`, (data, status) => {
      // Set the translated "hello" message in the HTML tag DIV#hello
      $('DIV#hello').html(data.hello);
    });
  };

  // Add a click event listener to the translate button
  $('INPUT#btn_translate').click(translateHello);

  // Add a keydown event listener to the language code input field
  $('INPUT#language_code').keydown((ev) => {
    // Check if the "Enter" key was pressed
    if (ev.key === 'Enter') {
      // Call the translateHello function when "Enter" key is pressed
      translateHello();
    }
  });
});
