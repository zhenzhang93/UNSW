const buildPipe = require('./piping');

let timesTwo = (a) => a*2;
let timesThree = (a) => a*3;
let minusTwo = (a) => a - 2;
let pipeline = buildPipe(timesTwo, timesThree, minusTwo);

console.log(pipeline(6));

pipeline = buildPipe(timesThree, minusTwo, timesTwo);
console.log(pipeline(6));
