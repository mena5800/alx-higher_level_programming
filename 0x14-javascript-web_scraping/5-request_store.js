#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    const data = response.body;
    // Read the content of the file in utf-8
    fs.writeFile(filePath, data, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
