#!/usr/bin/node
const argv = process.argv;
const len = argv.length;
if (len === 2) {
  console.log(0);
} else if (len === 3) {
  console.log(0);
} else {
  const numbers = argv.slice(2, len);
  const intNumbers = numbers.map(num => parseInt(num));
  const sortedNumbers = intNumbers.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}
