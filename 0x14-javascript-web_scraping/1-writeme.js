#!/usr/bin/node
/* script that prints the contents of a file */

/* Import the 'fs' (file system) module to work with files. */
const fs = require('fs');
/* Get the third command-line argument file name */
const filename = process.argv[2];
const text = process.argv[3];
/* writes the contents using the writeFile method */
fs.writeFile(filename, text, 'utf8', (err) => {
  if (err) console.log(err);/* print error */
});
