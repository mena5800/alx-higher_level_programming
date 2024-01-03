#!/usr/bin/node
const fs = require('fs');

// Get the file path from command-line arguments
const filePath = process.argv[2];
const txtToWrite = process.argv[3];

// Read the content of the file in utf-8
fs.writeFile(filePath, txtToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
