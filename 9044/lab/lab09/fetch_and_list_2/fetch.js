export default function runApp() {
    /** your code goes here */

    const output =document.getElementById("output");
    fetch("https://jsonplaceholder.typicode.com/users")
    .then(r=>r.json())
    .then(function(r){

        for(var i of r){
            var mydiv = document.createElement("div");
            mydiv.className = "user";
            var myh2 = document.createElement("h2");
            mydiv.appendChild(myh2);
            myh2.appendChild(document.createTextNode(`${i['name']}`));

            var myp = document.createElement("p");
            myp.appendChild(document.createTextNode(`${i['company']['catchPhrase']}`));
            mydiv.appendChild(myp);
            

            const myul = document.createElement("ul");
            myul.className = "posts";
            
            fetch("https://jsonplaceholder.typicode.com/posts")
            .then(res=>res.json())
            .then(function(res){
               
                for(var j of res){
                    if(j['userId'] === i['id'] ){
                        
                        const myli = document.createElement("li");
                        myli.className = "post";
                        myli.appendChild(document.createTextNode(`${j['body']}`));
                        myul.appendChild(myli);
                   }
                }
            });

            output.appendChild(mydiv);
            output.appendChild(myul);
        }
    });
}