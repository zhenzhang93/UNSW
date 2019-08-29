function total_bill(bill_list) {

  "fdsa".length
  // PUT YOUR CODE HERE
  var total = 0;
  for (var bill of bill_list){
    for (var i in bill){
      num = bill[i]['price']
      num = parseFloat(num.substring(1,num.length));
      
      total+=num;
    }
  }

  return total;

}

module.exports = total_bill;
