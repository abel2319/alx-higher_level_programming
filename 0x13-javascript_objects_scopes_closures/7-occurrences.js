#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  if (list !== undefined && searchElement !== undefined) {
    for (let i = 0; i < list.length; i++) {
      if (list[i] === searchElement) { cnt += 1; }
    }
  }
  return (cnt);
};
