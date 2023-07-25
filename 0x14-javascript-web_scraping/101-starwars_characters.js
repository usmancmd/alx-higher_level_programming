#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];
request(url, function (error, response, body) {
  if (body) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, i) {
  request(characters[i], function (error, response, body) {
    if (body) {
      console.log(JSON.parse(body).name);
      if (i + 1 < characters.length) {
        printCharacters(characters, i + 1);
      }
    }
  });
}
