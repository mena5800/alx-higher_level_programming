#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const id = 18;

request.get(url, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    const results = JSON.parse(response.body).results;
    let counter = 0;
    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i].characters.length; j++) {
        if (results[i].characters[j].includes(id)) {
          counter += 1;
        }
      }
    }
    console.log(counter);
  }
});
