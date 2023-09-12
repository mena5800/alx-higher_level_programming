#!/usr/bin/node
const argv = process.argv;
const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  let myStr = '';
  for (let i = 0; i < num; i++) {
    myStr += 'X';
  }
  console.log(myStr);
}
