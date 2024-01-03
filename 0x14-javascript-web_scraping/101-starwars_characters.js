#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

function printCharacter (data, index) {
  if (index < data.length) {
    request.get(data[index], (err, response) => {
      if (err) {
        console.error(err);
      } else {
        console.log(JSON.parse(response.body).name);
        printCharacter(data, index + 1);
      }
    });
  }
}

request.get(url, async (err, response) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(response.body).characters;
    printCharacter(data, 0);
  }
}
);
