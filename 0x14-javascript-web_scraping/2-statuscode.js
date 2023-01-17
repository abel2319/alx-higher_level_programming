#!/usr/bin/node

const request = require('request');
request(process.argv[1], function (error, response, body) {
  if (error) console.error('error:', error);
  console.log('code:', response && response.statusCode);
});
