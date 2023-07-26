#!/usr/bin/node

const request = require('request');
const args = process.argv;

let count = 0;

request.get(args[2], (error, response, body) => {
    if (error) {
        console.log(error);
    }
    const content = JSON.parse(body);
    contents.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes("18")) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
