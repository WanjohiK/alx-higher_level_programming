#!/usr/bin/node
/* script that prints the number of movies where the character “Wedge Antilles” is present. */

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) console.log(err);
  else {
    let count = 0;
    /* parse the JSON response to results array */
    const results = JSON.parse(body).results;
    /* lops to get the char array */
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      /* loops through char array to get movie id */
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
