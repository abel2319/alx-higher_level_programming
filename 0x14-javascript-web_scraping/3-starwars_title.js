#!/usr/bin/node
/* script that prints the title of a Star Wars movie where the episode number matches a given integer. */

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, data, body) => {
  if (err) console.error('error:', err);
  console.log(JSON.parse(body).title);
});
