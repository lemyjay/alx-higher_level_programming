#!/usr/bin/node
// A function that executes x times a function.
function callMeMoby (x, theFunction) {
  if (x > 0) {
    theFunction();
    callMeMoby(x - 1, theFunction);
  }
}

module.exports = { callMeMoby };
