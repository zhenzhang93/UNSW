export default function runApp() {
    /** your code goes here */



    const output = document.getElementById("output");
    const morebutton = document.getElementById("more");
    morebutton.onclick = function(){


        var date = new Date();

        var time =`${date.getHours()}:${date.getMinutes()}`;

        //remove the img
        var loading  = document.getElementById("loading");
        loading.style.display = null;
        if(output.children.length >=6){
            output.removeChild(output.children[1]);
            fetch("https://picsum.photos/200/300/?random")
            .then(function(r){

                const mydiv = document.createElement("div");
                mydiv.className = "img-post";

                const myimg = document.createElement("img");
                myimg.setAttribute("src",r.url);

                const mytime = document.createElement("p");
                mytime.appendChild(document.createTextNode(`Fetched at ${time}`));
                mydiv.appendChild(myimg);
                mydiv.appendChild(mytime);

                output.appendChild(mydiv);
            
                loading.style.display = "none";
            });
        }
        else{
            fetch("https://picsum.photos/200/300/?random")
            .then(function(r){

                const mydiv = document.createElement("div");
                mydiv.className = "img-post";

                const myimg = document.createElement("img");
                myimg.setAttribute("src",r.url);

                const mytime = document.createElement("p");
                mytime.appendChild(document.createTextNode(`Fetched at ${time}`));
                mydiv.appendChild(myimg);
                mydiv.appendChild(mytime);

                output.appendChild(mydiv);
            
                loading.style.display = "none";
                
            });
        }
    }
}