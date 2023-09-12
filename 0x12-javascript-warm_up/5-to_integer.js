#!/usr/bin/node
const argv = process.argv;
const num1 = parseInt(argv[2]);
if (isNaN(num1)) {
  console.log('Not a number');
} else {
  console.log('My number:', num1);
}
