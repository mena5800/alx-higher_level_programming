#!/usr/bin/node
const importedList = require('./100-data').list;
console.log(importedList);
console.log(importedList.map((x, index) => x * index));
