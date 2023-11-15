#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
if (isNaN(num1)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num1; i++) {
    console.log('C is fun');
  }
}
