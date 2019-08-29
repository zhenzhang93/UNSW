function sum(list) {
  var res = 0;
  for(var i of list){
    
    res = res + parseInt(i);
  }
  return res;

}

module.exports = sum;
