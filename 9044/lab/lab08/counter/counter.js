(function() {
   'use strict';
   // write your code here


	const mycounter = document.getElementById("output");
	var num = 0;
	setInterval(function(){
		mycounter.innerHTML = num;
		num++;
	},1000);

}());
