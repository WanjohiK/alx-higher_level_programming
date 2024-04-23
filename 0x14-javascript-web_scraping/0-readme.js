#!/usr/bin/node
/* script that Reads and Prints the contents of a file */

/* Import the 'fs' (file system) module to work with files. */
const fs = require('fs');
/* Get the third command-line argument file name */
const filename = process.argv[2];
/* read the contents using the readline method */
fs.readFile(filename, 'utf8', (err, data) => {
  if (err) console.log(err);
  /* print error */
  else console.log(data.toString());
  /* print contents of file */
});
