#!/usr/bin/node
const importedDict = require('./101-data').dict;
const newDict = {};
for (const item in importedDict) {
  if (newDict[importedDict[item]] === undefined) {
    newDict[importedDict[item]] = [item];
  } else {
    newDict[importedDict[item]].push(item);
  }
}
console.log(newDict);
