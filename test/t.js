
/*
const a = process.argv[2];
if(parseInt(a)% 2 !== 0){

	console.log(parseInt(a));
}
else{
	console.log(parseInt(a)* 2 );
}
*/


//function myadd(start,...argument){
//	return argument.reduce( (pre,cur)=>pre+cur,start);
//}

//console.log(process.argv.slice(2).map(x=>parseInt(x)).reduce( (pre,cur)=> pre + cur));

const readline = require('readline');
const r1=readline.createInterface({
	input:process.stdin,
	output:process.stdout
});
r1.on('line',(line)=>{
	console.log(line,"fdsaf");
	process.stdout.write(line+'\n');
});
