#!/usr/bin/node
function fact (a) {
  if (a === 1) {
    return 1;
  }
  return a * fact(a - 1);
}

const argv = process.argv;
const num = parseInt(argv[2]);

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(fact(num));
}
