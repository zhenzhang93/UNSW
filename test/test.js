// const readline = require('readline');
// const r1 = readline.createInterface({

// 	input:process.stdin,
// 	output:process.stdout

// });

// var maxnum = 0;
// var myname;
// var dic={};
// r1.on('line',function(r){
// 	var myarr = r.split(/ +/);
// 	if(!dic.hasOwnProperty(myarr[0])) {
// 		dic[myarr[0]] = parseInt(myarr[1]);
// 	}
// 	else {

// 		dic[myarr[0]] += parseInt(myarr[1]);
// 	}
// });


// r1.on('pause',function(r){
// 	var res = Object.keys(dic).sort((a,b)=> dic[b] -dic[a])[0];
// 	console.log(`expel ${res} total ${dic[res]}`); 
// 	process.stdout.write("fsaf");
// });


const cart = [
  {
    name: 'Apple',
    cost: 2.30
  },
  {
    name: 'Orange',
    cost: 4.50
  },
  {
    name: 'Apple',
    cost: 2.30
  },
  {
    name: 'Strawberry',
    cost: 6.70
  },
  {
    name: 'Orange',
    cost: 4.50
  }
];


/*
var dic={};

for (var i of process.argv.slice(2)){
	
	dic[i] = dic[i]? dic[i] +1 : 1;
}
for (const key of Object.keys(dic).sort()){
	console.log(`${key} +++ ${dic[key]}`);

} 

*/

//console.log(cart.map(item=>item.cost).reduce((a,b)=>a+b,10));




let r = /(\d+)/g;
let res = r.exec(process.argv[2]);
console.log(res)
while((res = r.exec(process.argv[2]))!==null){
	console.log(res);
}
//let [a,b] = res.slice(1);
//console.log(res);
//console.log(a,b);



//week7 q26
// function extractTime(s) {
//   let r = /(\d+)\s+([ms])/g;
//   r = r.exec(s);
// 	console.log(r)
//   let [num,unit] = r;
//   if (unit === "m") num *= 60;
//   return num;
// }

// console.log(extractTime("set timer for 5 minutes"), 300);
// console.log(extractTime("set a timer for 10m"), 600);
// console.log(extractTime("timer 8minutes"), 480);
// console.log(extractTime("new timer 60seconds"), 60);
// console.log(extractTime("timer for 60s"), 60); 

//let mylist = [1,3,5,7,undefined,8]
//let res = mylist.filter(r=> r);
//console.log(res); 























