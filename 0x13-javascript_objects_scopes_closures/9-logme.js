#!/usr/bin/node

let cnt = 0;

exports.logMe = function (item) {
  if (item !== undefined) {
    console.log(`${cnt}: ${item}`);
    cnt += 1;
  }
};
