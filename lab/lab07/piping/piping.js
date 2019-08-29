// function buildPipe(...funcs) {
	
// 	return function(val){
// 		return funcs.reduce(function(pre,cur){
// 			return cur(pre);
// 		},val);
// 	}
// }

function buildPipe(...funcs) {
	
	return val => funcs.reduce((pre,cur)=>cur(pre),val);
	
}


// This is how we can export functions in node
// in the same way we can use the "export" keyword in browser 
// side JS

module.exports = buildPipe;

