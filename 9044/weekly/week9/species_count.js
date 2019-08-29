function species_count(target_species, whale_list) {

  // PUT YOUR CODE HERE
  var res = 0;
  for(var i of whale_list){
    if(i.species === target_species){
      res += i.how_many;
    }
  }

  return res;

}

module.exports = species_count;
