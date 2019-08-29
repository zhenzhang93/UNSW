//export default function runApp() {
    /** your code goes here */
    // const output = document.getElementById("output");

    // fetch("https://jsonplaceholder.typicode.com/users")
    // .then(r=>r.json())
    // .then(function(r){
    //     for(var i of r){
            
    //         console.log(i['name'],"==",i['company']['catchPhrase']);
    //         var child = document.createElement("div");
    //         child.className = "user";
    //         var h2 = document.createElement("h2");
    //         h2.appendChild(document.createTextNode(`${i['name']}`));
    //         var p = document.createElement('p');
    //         p.appendChild(document.createTextNode(`${i['company']['catchPhrase']}`));
    //         child.appendChild(h2);
    //         child.appendChild(p);
    //         output.appendChild(child);
    //     }
    // })
    // .catch(e=>alert(e));
    let output;

    function createUserDiv(user) {
    const div = document.createElement('div');
    div.className = 'user';

    const h2 = document.createElement('h2');
    h2.innerText = user.name;

    const p = document.createElement('p');
    p.innerText = user.company.catchPhrase;

    div.appendChild(h2);
    div.appendChild(p);

    output.appendChild(div);
    
    //return div;
    }

    function append(element) {
    output.appendChild(element);
    }

    export default function runApp() {
    output = document.getElementById('output');

    fetch('https://jsonplaceholder.typicode.com/users')
        .then(res => res.json())
        .then(data => data.map(createUserDiv));
        //.then(elements => elements.map(append));
    }
//}