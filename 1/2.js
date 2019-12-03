var fs = require('fs');
var lines = fs.readFileSync('1/in.txt', 'utf-8').split('\n').map(Number)

let cost = function(amt) {
  let needed = Math.floor(amt / 3) - 2
  if(needed <= 0) {
    return 0
  } else {
    return needed + cost(needed)
  }
}

console.log(lines.map(cost).reduce((a, b) => a + b))
