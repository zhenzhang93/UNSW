const species_count = require('./species_count')
const target_species = process.argv[2];
const json = process.argv[3];
if (json === undefined) {
  throw new Error(`input not supplied`);
}
const whale_list = require(`./${json}`);
console.log(species_count(target_species, whale_list));
