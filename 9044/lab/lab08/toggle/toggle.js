(function() {
   'use strict';
   // write your js here.

	const output = document.getElementById("output");

	setInterval(function(){

		
		//output.classList.toggle("hide");
		if(output.classList.contains("hide")){
			output.classList.remove("hide");
		}
		else{
			output.classList.add("hide");
		}
		
		
	},2000);


}());
