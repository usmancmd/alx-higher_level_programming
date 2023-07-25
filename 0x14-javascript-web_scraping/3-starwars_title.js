#!/usr/bin/node

const request = require('request');
const args = process.argv;

const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url + `${args[2]}`, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
