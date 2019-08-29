(function() {
   'use strict';
   // code here

	
	const player = document.getElementById("player");

	

	var speed = 10;
	var count = 0;
	var image = undefined;
	var startofball = undefined;
	
	if(!player.style.left){
		player.style.left = 0;
	}
	document.onkeydown = function(event){
		var position = parseInt(player.style.left);
		
		if(event.key ==='z'){

			if(speed === 10){
				speed = 50;
			}
			else{
				speed = 10;
			}
		}

		else if(event.key === 'x'){
			if (count === 0){
			
			
				image = document.createElement("img");
			
				image.src = "imgs/fireball.png";
				
				image.style.width = 60 + "px";
				image.style.height = 60 + "px"; 
				image.style.bottom = 118 + "px";	 
				image.style.position = "absolute";
				image.style.left = position + 75 + "px";
				startofball = parseInt(image.style.left);
				document.body.appendChild(image);
				console.log(image.style.bottom);
				count++;

				
				var interval = setInterval(function(){	
						if(image){
							image.style.left = parseInt(image.style.left)+ 10 + "px";
							if( parseInt(image.style.left) - startofball  > 400){
								document.body.removeChild(image);
								clearInterval(interval);
								count--;
							} 
						}
			
				},100);

			}


		} 
		//left
		else if(event.keyCode == 37){
			if( parseInt(player.style.left) <= -20 ){
				player.style.left = -20;
			}
			else{
				if( parseInt(player.style.left) - speed <= -20){
					
					player.style.left = "-20px";
				}
				else{
					player.style.left = parseInt(player.style.left) - speed + "px";
				}
			}
			console.log(player.style.left);
			

		}
		//right
		else if (event.keyCode ==39 ){
			player.style.left = parseInt(player.style.left) + speed + "px";
			console.log(player.style.left);

		}

	};

	
	

	


}());
