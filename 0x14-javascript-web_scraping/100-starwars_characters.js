#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(response.body).characters;
    for (let i = 0; i < data.length; i++) {
      request.get(data[i], (err, response) => {
        if (err) {
          console.error(err);
        } else {
          console.log(JSON.parse(response.body).name);
        }
      });
    }
  }
});
