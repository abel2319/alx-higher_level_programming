#!/usr/bin/node
const a = parseInt(process.argv[2]);

function factorial (b) {
	if (b == 0 || isNaN(b))
		return (1);
	return (b * factorial(b - 1));
}
console.log(factorial(a));
