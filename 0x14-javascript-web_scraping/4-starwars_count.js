#!/usr/bin/node
/*script that prints the number of movies where the character “Wedge Antilles” is present.*/

const request = require('request');

request(process.argv[2], (err, data, body) => {
  if (err) console.error('error:', err);
  console.log(JSON.parse(body));
});
