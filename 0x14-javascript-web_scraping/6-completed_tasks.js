#!/usr/bin/node
/* script that prints the title of a Star Wars movie where the episode number matches a given integer. */

const request = require('request');

const url = process.argv[2];

request(url, (err, data, body) => {
  if (err) console.error('error:', err);

  const bod = JSON.parse(body);
  const output = {};

  bod.map(dict => {
    if (dict.completed && output[dict.userId] === undefined) {
      output[dict.userId] = 1;
    } else if (dict.completed) {
      output[dict.userId] += 1;
    }
    return (1);
  });
  console.log(output);
});
