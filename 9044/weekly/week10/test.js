const total_bill = require('./total_bill')
const json = process.argv[2];
if (json === undefined) {
  throw new Error(`input not supplied`);
}
const bill_list = require(`./${json}`);
console.log(total_bill(bill_list).toFixed(2));
