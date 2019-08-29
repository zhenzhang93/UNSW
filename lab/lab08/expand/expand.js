(function() {
  'use strict';
	window.onload = function(){
		const uparrows = document.getElementsByClassName("material-icons");
	
		for(let i = 0; i<uparrows.length;i++){
			
			if(!uparrows[i].id) continue;
			const arrow = document.getElementById(uparrows[i].id);
		
			
			arrow.onclick = function(){
			
				var string = uparrows[i].id+"-content";
				
				const content = document.getElementById(string);


				if(content.style.display === 'block'){
					content.style.display ='none';
					arrow.innerHTML = "expand_more";
				}
				else{
					content.style.display = 'block';	
					arrow.innerHTML = "expand_less";	
				} 

			};

		}
	}

}());
