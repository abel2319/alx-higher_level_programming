#!/usr/bin/node
/* script that prints the title of a Star Wars movie where the episode number matches a given integer. */

const request = require('request');
const fs = require('fs');

const url = process.argv[2];

request(url, (err, data, body) => {
  if (err) console.error('error:', err);
  fs.writeFile(process.argv[3], body, 'utf-8', (error, data) => {
    if (error) console.log(error);
  });
});
