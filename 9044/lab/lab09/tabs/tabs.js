export default function runApp() {
    /** your code goes here */

    const mytab = [...document.getElementsByClassName("nav-link")];
    const information = document.getElementById("information");
    //Array.from(mytab).forEach
    console.log(mytab);
    mytab.forEach(tab=>{
        tab.onclick = function(){
            mytab.forEach(e =>{
                e.classList.remove("active");
            })

            tab.className +=" active";
            fetch("planets.json")
            .then(r=>r.json())
            .then(function(r){
                
                for(var i of r){
                    if(i['name'] === tab.innerHTML){
                        deletecontent();
                        const myul = document.createElement("ul");
            
                        const myh2 = document.createElement("h2");
                        myh2.appendChild(document.createTextNode(`${i['name']}`));
            
                        information.appendChild(myh2);
            
            
                        information.appendChild(document.createElement("hr"));
            
            
                        const myp = document.createElement("p");
                        myp.appendChild(document.createTextNode(`${i['details']}`));
                        information.appendChild(myp);
            
                        Object.keys(i.summary).forEach(key =>{
                            
                            const myli = document.createElement("li");
                            const myb = document.createElement('b');
                            myb.appendChild(document.createTextNode(`${key}`))
                            myli.appendChild(myb);
                            myli.appendChild(document.createTextNode(`${i.summary[key]}`));
            
                            myul.appendChild(myli);
                            
                        });
                        information.appendChild(myul);
                    }
        
                }
            });
        }
    });

    function deletecontent(){
    
        while(information.firstChild){
            information.removeChild(information.firstChild);
        }
    }

}