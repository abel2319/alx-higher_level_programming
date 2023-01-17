#!/usr/bin/node
/* script that gets the contents of a webpage and stores it in a file. */

const request = require('request');
const fs = require('fs');

const url = process.argv[2];

request(url, (err, data, body) => {
  if (err) console.error('error:', err);
  fs.writeFile(process.argv[3], body, 'utf-8', (error, data) => {
    if (error) console.log(error);
  });
});
