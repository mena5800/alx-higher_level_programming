#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(response.body);
    const result = {};
    let userId = -1;
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed === true) {
        userId = data[i].userId;
        if (result[userId]) {
          result[userId] += 1;
        } else {
          result[userId] = 1;
        }
      }
    }
    console.log(result);
  }
});
