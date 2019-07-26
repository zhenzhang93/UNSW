function countStats(data) {
	var matches = 0;
	var tries = 0;
	
	for (var i in data){
		matches += Number(data[i].matches);
		tries += Number(data[i].tries);
	}
    return {matches,tries};
}

const json = process.argv[2];
if (json === undefined) {
    throw new Error(`input not supplied`);
}
// include the json file via node's module system,
// this parses the json file into a JS object
// NOTE: this only works via node and will not work in the browser
const stats = require(`./${json}`);

console.log(countStats(stats.results));
