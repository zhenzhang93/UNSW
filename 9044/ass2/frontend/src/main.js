/**
 * Written by A. Hinds with Z. Afzal 2018 for UNSW CSE.
 * 
 * Updated 2019.
 */

// import your own scripts here.

// your app must take an apiUrl as an argument --
// this will allow us to verify your apps behaviour with 
// different datasets.
function initApp(apiUrl) {


    
    //the root and nav html
    const root = document.createElement("div");
    root.setAttribute("id","root");
    document.body.appendChild(root);
    
    const nav = document.createElement("header");
    nav.className = "banner";
    nav.setAttribute("id","nav");
    
    root.appendChild(nav);
    
    const logo = document.createElement("h1");
    logo.setAttribute("id","logo");
    logo.appendChild(document.createTextNode("Seddit"));
    logo.className="flex-center";
    
    nav.appendChild(logo);
    
    const ul = document.createElement("ul");
    ul.className = "nav";
    nav.appendChild(ul);
    
    var li1 = document.createElement("li");
    var li2 = document.createElement("li");
    var li3 = document.createElement("li");
    li1.className = "nav-item";
    li2.className = "nav-item";
    li3.className = "nav-item";
    
    ul.appendChild(li3);
    ul.appendChild(li1);
    ul.appendChild(li2);
    
    
    
    //login button
    var login_button = document.createElement("button");
    login_button.setAttribute("data-id-login","");
    login_button.setAttribute("id","my_login_button");
    login_button.appendChild(document.createTextNode("Log In"));
    login_button.className="button button-primary";
    
    
    //registration button
    var register_button = document.createElement("button");
    register_button.setAttribute("data-id-signup","");
    register_button.setAttribute("id","my_register_button");
    register_button.appendChild(document.createTextNode("Sign Up"));
    register_button.className="button button-secondary";
    
    
    //search input
    var search = document.createElement("input");
    search.setAttribute("id","search");
    search.setAttribute("placeholder","Search Seddit");
    search.setAttribute("data-id-search","");
    search.setAttribute("type","search");
    
    li1.appendChild(login_button);
    li2.appendChild(register_button);
    li3.appendChild(search);


    //feed interface

    const feed = document.createElement("main");
    feed.setAttribute("role","main");
    root.appendChild(feed);
    const feedul = document.createElement("ul");
    feed.appendChild(feedul);
    feedul.setAttribute("id","feed");
    feedul.setAttribute("data-id-feed","");
    feed.appendChild(feedul);
    var feed_div = document.createElement("div");
    feed_div.className="feed-header";
    feedul.appendChild(feed_div);
    var Popular_post = document.createElement("h3");
    Popular_post.className="feed-title alt-text";
    Popular_post.appendChild(document.createTextNode("Popular posts"));
    feed_div.append(Popular_post);
    const post_button = document.createElement("button");
    post_button.className = "button button-secondary";
    post_button.appendChild(document.createTextNode("Post"));
    feed_div.appendChild(post_button);







    //add feed to main page or the feed of some user
    var path = `${apiUrl}/user`
    fetch(path,{
        method: "GET",
        headers:{
           'accept':"application/json",
            'Content-Type':"application/json",
            'Authorization':'Token: ' + getLocalStorage('logintoken')
        }
    })
    .then(function(r){
        //if is is logged in
        if(r.status === 200){

            addShowMyPost();
            getUserFeed('logintoken');
            addUserProfile();
            UpdateUser();
            addUserLogOut();
          
        }

        //read local posts
        else{
            // fetch("../data/feed.json")
            // .then(r=>r.json())
            // .then(function(r){
            //     for(var i of r.posts){
            //         createFeed(i);
            //     }
            // });

            //fetch the data from post/public
            var path = `${apiUrl}/post/public`;

            fetch(path,{
                method: 'GET',
                headers: {'accept':"application/json",
                           'Content-Type':"application/json"}
            })
            .then(r=>r.json())
            .then(function(r){
                
                if(r.posts.length!==0){
                    
                    for(var i of r.posts.sort(sortTheTime)){
                        createFeed(i);
                    }
                }

            })
            

        }
    })


    //modal
    const myModal = createElement("div","",{
        "class":"modal",
        "id":"myModal"
    })
    document.body.appendChild(myModal);
    const modalcontent = createElement("div","",{
        'class':"modal-content",
        "id":"myModalcontent"
    })
    myModal.appendChild(modalcontent);
    const closespan = createElement("span",'x',{
        'class':"close"
    })
    modalcontent.appendChild(closespan);


    //another modal for the follow list
    const myListModal = createElement("div","",{
        "class":"modal",
        "id":"myListModal"
    })
    document.body.appendChild(myListModal);
    const listmodalcontent = createElement("div","",{
        "id":"listmodalcontent"
    })
    myListModal.appendChild(listmodalcontent);

    const listclosespan = createElement("span",'x',{
        'class':"close",
        id:"mylistclose"
    })
    listmodalcontent.appendChild(listclosespan);



    //login button
    const login = document.getElementById("my_login_button");
    login.onclick=function(){
        if(! document.getElementById("login_input_div")){     
            var input_box = document.createElement("div");
            input_box.className = "button";
            input_box.setAttribute("id","login_input_div");
            input_box.style["background-color"]="#FFFF99";
            nav.appendChild(input_box);
            var inputname = document.createElement('input');
            var inputpw = document.createElement('input');
            var login_submit = document.createElement("li");
            login_submit.appendChild(document.createTextNode("Login"));
            login_submit.setAttribute("id","login_submit_button");
            login_submit.className = "nav-item";
            inputname.setAttribute("id","lname");
            inputpw.setAttribute("id","lpassword");
            inputname.setAttribute("placeholder","Enter your username");
            inputname.setAttribute("type","text");
            inputpw.setAttribute("placeholder","Enter your password");
            inputpw.setAttribute("type","password");
            input_box.appendChild(inputname);
            input_box.appendChild(inputpw);
            input_box.appendChild(login_submit);


            //add cancel to the login button
            var login_cancel = createElement("li","cancel",{
                id:"login_cancel_button",
                class:"nav-item"
            });
            input_box.appendChild(login_cancel);
            login_cancel.onclick = function(){
                var mybutton = document.getElementById("login_input_div");

                mybutton.parentNode.removeChild(mybutton);
            }
        }
        
        tologin();
        //after click login, delete these node;
    }

    //register button
    const register = document.getElementById("my_register_button");
    register.onclick=function(){
        if(! document.getElementById("register_input_div")){     
            var input_box = document.createElement("div");
            input_box.className = "button";
            input_box.setAttribute("id","register_input_div");
            input_box.style["background-color"]="#FFFF99";
            nav.appendChild(input_box);
            var inputusername = document.createElement('input');
            var inputpw = document.createElement('input');
            var inputname = document.createElement('input');
            var inputemail = document.createElement('input');
            var login_submit = document.createElement("li");
            login_submit.appendChild(document.createTextNode("Register"));
            login_submit.setAttribute("id","register_submit_button");
            login_submit.className = "nav-item";
            inputusername.setAttribute("id","rusername");
            inputusername.setAttribute("placeholder","Enter your username");
            inputusername.setAttribute("type","text");
            inputpw.setAttribute("id","rpassword");
            inputpw.setAttribute("placeholder","Enter your password");
            inputpw.setAttribute("type","password");
            inputemail.setAttribute("id","remail");
            inputemail.setAttribute("placeholder","Enter your email");
            inputemail.setAttribute("type","text");
            inputname.setAttribute("id","rname");
            inputname.setAttribute("placeholder","Enter your name");
            inputname.setAttribute("type","text");
        

            input_box.appendChild(inputusername);
            input_box.appendChild(inputpw);
            input_box.appendChild(inputemail);
            input_box.appendChild(inputname);
            input_box.appendChild(login_submit);

            //add cancel to the register button
            var register_cancel = createElement("li","cancel",{
                id:"register_cancel_button",
                class:"nav-item"
            });
            input_box.appendChild(register_cancel);
            register_cancel.onclick = function(){
                
                var mybutton = document.getElementById("register_input_div");

                mybutton.parentNode.removeChild(mybutton);
            }
        }
        
        toregister();
        //after click login, delete these node;
    }

    //to fetch 
    function tologin(){
        const submit_login = document.getElementById("login_submit_button");
        submit_login.onclick=function(){
    
            const login_username = document.getElementById("lname").value;
            const login_password = document.getElementById("lpassword").value;
    
            if(!login_username || !login_password){
                alert("Username or password can not be empty");
                return false;
            }
            
            var path = `${apiUrl}/auth/login`;
            var userinfo ={
                'username':login_username,
                'password':login_password
            }
            fetch(path,{
                method: 'POST',
                body: JSON.stringify(userinfo),
                headers: {'accept':"application/json",
                           'Content-Type':"application/json"}
            })
            .then(r => r.json())
            .then(function(res){
                //successful login
                if(res['token']){
                    //window.localStorage.setItem("logintoken",res['token']);
                    alert("login successful")
                    localStorage.setItem("logintoken",res['token']);
                    localStorage.setItem("currentusername",login_username);
                    location.reload();
                }
                else{
                    alert(res['message']);
                    
                }
            });
            //.catch(error=>alert(error));
        }
    }
    
    //to fetch 
    function toregister(){
        const submit_register = document.getElementById("register_submit_button");
        submit_register.onclick=function(){
    
            const register_username = document.getElementById("rusername").value;
            const register_password = document.getElementById("rpassword").value;
            const register_email = document.getElementById("remail").value;
            const register_name = document.getElementById("rname").value;
    
            if(!register_username ||!register_password||!register_email||!register_name){
                alert("All fields can not be empty");
                return false;
            }
    
            var userinfo = {
                'username':register_username,
                'password':register_password,
                'email':register_email,
                'name':register_name
            }
            var path = `${apiUrl}/auth/signup`;
            fetch(path,{
                method: 'POST',
                body: JSON.stringify(userinfo),
                headers: {'accept':"application/json",
                           'Content-Type':"application/json"}
            })
            .then(r => r.json())
            .then(r =>{
                //successful register
                if(r['token']){
                    //window.localStorage.setItem("registertoken",r['token']);
                    alert("register success");
                    window.location.reload();
                }
            });
        }
    
    }

    //add profile in the page,show the information of logged in user
    function addUserProfile(){
        var porfile = createElement("button","profile",{
            "data-id-profile":"",
            "id":"my-profile-button",
            "class":"button button-primary"
        });
        var profileli = createElement("li","",{
            "class":"nav-item"
        })
        profileli.appendChild(porfile);
        ul.appendChild(profileli);


        //profile button
        const profile = document.getElementById("my-profile-button");
        profile.onclick = function(){

            var modal = document.getElementById("myModal");

            var span = document.getElementsByClassName("close")[0];
            modal.style.display = "block";
    
    
            span.onclick = function() {
                modal.style.display = "none";
                deleteChildInmodal();
            }      
            window.onclick = function(event) {
                if (event.target == modal) {
                    modal.style.display = "none";
                    deleteChildInmodal();
                }
            }
            UserPages();

            showFollow();
        }
    }

    //get the userpages of some logged user
    //or others info
    function UserPages(username = ""){

        var path = `${apiUrl}/user?username=${username}`;
        fetch(path,{
            method: "GET",
            headers:{
               'accept':"application/json",
                'Content-Type':"application/json",
                'Authorization':'Token: ' + getLocalStorage('logintoken')
            }
        })
        .then(r=>r.json())
        .then(function(r){ 
            
            modalcontent.appendChild(createElement('p',`username: ${r['username']}`,{}));
           
            modalcontent.appendChild(createElement('p',`number of posts: ${r['posts'].length}`,{}));
           
            modalcontent.appendChild(createElement('p',`email: ${r['email']}`,{}));
            
            modalcontent.appendChild(createElement('p',`name: ${r['name']}`,{}));

            modalcontent.appendChild(createElement('p',`number of followed: ${r['followed_num']}`,{}));

            //add the total votes number;
           
            showupvotesNumber(r.posts)
            .then(function(r){
                
                modalcontent.appendChild(createElement('p',
                `number of votes: ${r}`,{}));
                
            })
        
        });
        //.catch(e => alert(e));

    }


    


    //add update in the page

    function UpdateUser(){
        var update = createElement("button","upddate",{
            "data-id-update":"",
            "id":"my-update-button",
            "class":"button button-primary"
        });
        var updateli = createElement("li","",{
            "class":"nav-item"
        })
        updateli.appendChild(update);
        ul.appendChild(updateli);


        //update form
        update.onclick = function(){

            var modal = document.getElementById("myModal");

            var span = document.getElementsByClassName("close")[0];
            modal.style.display = "block";
    
    
            span.onclick = function() {
                modal.style.display = "none";
                deleteChildInmodal();
            }
    
            window.onclick = function(event) {
                if (event.target == modal) {
                    modal.style.display = "none";
                    deleteChildInmodal();
                }
            }
            UserupdateButton("logintoken");


            
        }


    }



    //add onclick to the update button
    function UserupdateButton(token){
        var path = `${apiUrl}/user`;
                
        modalcontent.appendChild(createElement('label',"email:",{}));
        modalcontent.appendChild(createElement('input',"",{
            placeholder:"input your new email",
            id:"updateemail"
        }));
    
        modalcontent.appendChild(createElement('p',"",{}));
        modalcontent.appendChild(createElement('label',"password:",{}));
        modalcontent.appendChild(createElement('input',"",{
            placeholder:"input you new password",
            id:"updatepassword"
        }));
    
        modalcontent.appendChild(createElement('p',"",{}));
        modalcontent.appendChild(createElement('label',"name:",{}));
        modalcontent.appendChild(createElement('input',"",{
            placeholder:"input your new name",
            id:"updatename"
        }));
    
        modalcontent.appendChild(createElement('p',"",{}));
        modalcontent.appendChild(createElement('p',"",{}));
        modalcontent.appendChild(createElement('botton',"yes,update",{
            id:"myupdatebutton",
            class:"button button-primary"
        }));
    
    
    
        const myupdatebutton = document.getElementById("myupdatebutton");
        myupdatebutton.onclick = function(){
    
            const update_email = document.getElementById("updateemail").value;
            const update_password = document.getElementById("updatepassword").value;
            const update_name = document.getElementById("updatename").value;
            var userinfo = {
                'password':update_password,
                'email':update_email,
                'name':update_name
            }
            console.log(update_password);
            if(update_email==="" || update_password==="" || update_name===""){
                alert("Pleease update something");
            }
            else{
                fetch(path,{
                    method: "PUT",
                    headers:{
                    'accept':"application/json",
                        'Content-Type':"application/json",
                        'Authorization':'Token: ' + getLocalStorage(token)
                    },
                    body: JSON.stringify(userinfo)
                })
                .then(r=>r.json())
                .then(function(r){ 
                    console.log(r);
                    alert("update information successful");
                    location.reload();
                });
                
            }
        }
    
    }


    //add my post button to show my own post
    function addShowMyPost(){
        var mypost = createElement("button","my post",{
            "id":"my-mypost-button",
            "class":"button button-primary"
        });
        var mypostli = createElement("li","",{
            "class":"nav-item"
        })
        mypostli.appendChild(mypost);
        ul.appendChild(mypostli);


        //add logout function
        mypost.onclick =function(){
            //tansfer the main page to the my post   
            
            if(mypost.innerText === "MY POST"){
                window.onscroll = null;
                mypost.innerText = "FEED";
                showAllpost();
            }

            //tansfer the main page to feed;
            else{
                window.onscroll = ()=>myscroll();
                deleteFeed();
                mypage = 10;
                mypost.innerText = "MY POST";
                getUserFeed('logintoken');
                

            }  
        }
    }


    //add logout button to the logged user
    function addUserLogOut(){

        var logout = createElement("button","logout",{
            "id":"my-logout-button",
            "class":"button button-primary"
        });
        var logoutli = createElement("li","",{
            "class":"nav-item"
        })
        logoutli.appendChild(logout);
        ul.appendChild(logoutli);


        //add logout function
        logout.onclick =function(){
            localStorage.clear();
            location.reload();
        }
    }


    //give the name of the author and show their name
    function showInfoByname(username){


        if(getLocalStorage('logintoken') === null){
            return;
        }
        var modal = document.getElementById("myModal");

        var span = document.getElementsByClassName("close")[0];
        modal.style.display = "block";


        span.onclick = function() {
            modal.style.display = "none";
            deleteChildInmodal();
        }      
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
                deleteChildInmodal();
            }
        }

        UserPages(username);
        addFollowButton(username);
        showFollow(username);

    }


    


    //Add a list of everyone a user follows in their profile page
    function showFollow(username=""){


        modalcontent.appendChild(createElement('button',`show following`,{
            id:"show-follow",
            calss:"button button-primary"
        }));

        var myshowfollowbutton= document.getElementById("show-follow");
        myshowfollowbutton.onclick = function(){
            if(username){
                var path = `${apiUrl}/user/?username=${username}`;
            }
            else{
                var path = `${apiUrl}/user`;
            }
            fetch(path,{
                method: "GET",
                headers:{
                'accept':"application/json",
                    'Content-Type':"application/json",
                    'Authorization':'Token: ' + getLocalStorage('logintoken')
                }
            })
            .then(r=>r.json())
            .then(function(r){
                console.log(r);
                var modal = document.getElementById("myListModal");

                var span = document.getElementById("mylistclose");
                modal.style.display = "block";
        
        
                span.onclick = function() {
                    modal.style.display = "none";
                    deleteChildInListmodal();
                }      
               
                addFollowButtonToList(r.following);

            
            });

        }
    }


    //add onclick listener to each button
    async function addFollowButtonToList(ids){

        const idPromis = ids.map((id)=>
            fetch(`${apiUrl}/user/?id=${id}`,{
                method: "GET",
                headers:{
                    'accept':"application/json",
                    'Content-Type':"application/json",
                    'Authorization':'Token: ' + getLocalStorage('logintoken')
                }
            })
        )

        const responses = await Promise.all(idPromis);
        const jsons = await Promise.all(responses.map(response=>response.json()));
        
        
        for(var json of jsons){

            var mydiv = createElement("div","",{
                class:"listdiv"
            });
            var myp = createElement("p",`${json.name}`,{});
            listmodalcontent.appendChild(myp);

            var myfollowbutton = createElement("button","follow",{
                id:`list-follow-button-${json.id}`,
                //name:"${json.name}",
                class:"button"
            })
            var myunfollowbutton = createElement("button","unfollow",{
                id:`list-unfollow-button-${json.id}`,
                //name:"${json.name}",
                class:"button"
            })
            myp.appendChild(myfollowbutton);
            myp.appendChild(myunfollowbutton);

            (function(val){
               
                myfollowbutton.onclick=function(){
                    toFollowOrNot(val,true);
                }
                myunfollowbutton.onclick=function(){
                    toFollowOrNot(val,false);
                }

            })(json.name);

        }   
    }


    //show my post on the main page
    function showAllpost(){
        fetch(`${apiUrl}/user`,{
            method: "GET",
            headers:{
                'accept':"application/json",
                'Content-Type':"application/json",
                'Authorization':'Token: ' + getLocalStorage('logintoken')
            }
        })
        .then(r=>r.json())
        .then(function(r){

            const postpromises = r.posts.map((post)=>
                fetch(`${apiUrl}/post/?id=${post}`,{
                    method: "GET",
                    headers:{
                        'accept':"application/json",
                        'Content-Type':"application/json",
                        'Authorization':'Token: ' + getLocalStorage('logintoken')
                    }
                })
            );
        
            Promise.all(postpromises)
            .then((responses) => Promise.all(responses.map(res => res.json())))
            .then( (jsons)=>{
                //delete the feed first
                deleteFeed();
                for(var json of jsons.sort(sortTheTime)){

                    (function(val){            
                        createFeed(json);       
                    })(json);
                }

            });


        });

    }

    //delete the feed (for show my post,and feed)
    function deleteFeed(){
        var myfeed = document.getElementById("feed");
        for(var i = myfeed.children.length - 1; i>=1;i--){

            console.log(i);
            myfeed.removeChild(myfeed.children[i]);
        }
    }

    //add the button the my post
    function addDeleteAndChangeToPost(id){
        var deletebutton = document.getElementById(`${id}-deletebutton`);
        deletebutton.onclick = function(e){
            e.cancelBubble = true;
            if(window.confirm("Do you really want to delete?")){
                fetch(`${apiUrl}/post?id=${id}`,{
                    method: 'DELETE',
                    headers: {'accept':"application/json",
                            'Content-Type':"application/json",
                            'Authorization':'Token: ' + getLocalStorage('logintoken')}
                })
                .then(function(r){
                    if( r.status === 200){
                        console.log(r);
                        alert("delete post success");
                        location.reload();
                    }               
                });
                
            }
        }

        var updatebutton = document.getElementById(`${id}-updatebutton`);
        updatebutton.onclick = function(e){
            e.cancelBubble = true;

            //write something to update the post.
            //get the original content first

            fetch(`${apiUrl}/post/?id=${id}`,{
                method: `GET`,
                headers: {'accept':"application/json",
                            'Content-Type':"application/json",
                            'Authorization':'Token: ' + getLocalStorage('logintoken')
                        }
            })
            .then(r=>r.json())
            .then(function(r){


                var modal = document.getElementById("myModal");
    
                var span = document.getElementsByClassName("close")[0];
                modal.style.display = "block";
            
                span.onclick = function() {
                    modal.style.display = "none";
                    deleteChildInmodal();
                }
            
                window.onclick = function(event) {
                    if (event.target == modal) {
                        modal.style.display = "none";
                        deleteChildInmodal();
                    }
                }
                const texttitle = createElement("textarea",`${r.title}`,{
                    placeholder:"change your title",
                    id:"mytexttitle"
                })
                modalcontent.appendChild(texttitle);
                const textarea = createElement("textarea",`${r.text}`,{
                    placeholder:"change your content",
                    id:"mytextarea"
                });
                modalcontent.appendChild(textarea);    
                const testarea_button = createElement("button","yes,update",{
                    class:"button", 
                    id: "mytextarea_button"
                })
                modalcontent.appendChild(testarea_button);
                const uploadimg = createElement("input","",{
                    id:"myuploadimg",
                    class:"button-secondary",
                    type:"file"
                })
                modalcontent.appendChild(uploadimg);
                console.log(`${r.thumbnail}`);

                var imgUrl=`${r.thumbnail}`;
                if(imgUrl !== "null" && imgUrl!==""){
                    modalcontent.appendChild(createElement("img","",{
                        src:`data:image;base64,${r.thumbnail}`,
                        id:"myupdateimg"
                    }));
                }
                else{
                    modalcontent.appendChild(createElement("img","",{
                        id:"myupdateimg"
                    }));             
                }
                
                uploadimg.onchange =function(event){
                    //upload the image.
                    const myimg = event.target.files[0];
                    if(myimg.type === "image/jpeg" || myimg.type ==="image/png" || myimg.type ==="image/jpg"){
                        var reader = new FileReader();
                        reader.onload= function(e){
                            console.log(e);
                            imgUrl = e.target.result.split(',')[1];
                            console.log(imgUrl);
                            document.getElementById("myupdateimg").src = e.target.result;
                            
            
                        }
                        reader.readAsDataURL(myimg);
                    }
                    else{
                        alert("you need to choose an image");  
                    }
                }

                testarea_button.onclick=function(){
        
                    if(!textarea.value && !imgUrl && !texttitle.value){
                        alert("please change something");
                    }else{
                        if(imgUrl){
                            var mypost = {
                                title:`${texttitle.value}`,
                                text:`${textarea.value}`,
                                image:`${imgUrl}`
                            }
                        }
                        else{
                            var mypost = {
                                title:`${texttitle.value}`,
                                text:`${textarea.value}`               
                            }
                        }
                        console.log(mypost);
                        
                        var path = `${apiUrl}/post/?id=${id}`;
                
                        fetch(path,{
                            method: `PUT`,
                            body: JSON.stringify(mypost),
                            headers: {'accept':"application/json",
                                        'Content-Type':"application/json",
                                        'Authorization':'Token: ' + getLocalStorage('logintoken')
                                    }
                        })
                        .then(r =>{
                            if(r.status === 200){
                                alert("post success");
                                location.reload();
                            }
                            
                        })                                
                    }
            
                }
            });
            
      
        }

    }

    //sort the posts accordint to the time
    function sortTheTime(a,b){
        return (a.meta.published<b.meta.published)?1:-1;

    }

    //get the time of the post
    function getTime(timestring){
        var time = new Date(timestring * 1000);
        return time.toLocaleString("en-AU");

    }

    //function to follow or unfollow someone
    function addFollowButton(username){

        modalcontent.appendChild(createElement('button',`follow`,{
            id :`${username}-follow-button`,
            class:"button"
        }));
           
        modalcontent.appendChild(createElement('button',`unfollow`,{
            id :`${username}-unfollow-button`,
            class:"button"
        }));

        const followbutton = document.getElementById(`${username}-follow-button`);
        const unfollowbutton = document.getElementById(`${username}-unfollow-button`);
        followbutton.onclick = ()=>{
            toFollowOrNot(username,true);
        }
       
        unfollowbutton.onclick = ()=>{
            toFollowOrNot(username,false);
        }

    }





    //function to follow someone or unfollow someone
    function toFollowOrNot(username,follow = true){
        var followrornot;
        if (follow === true ){
            followrornot = "follow";
        }
        else{
            followrornot = "unfollow";
        }

        var path = `${apiUrl}/user/${followrornot}?username=${username}`;


        fetch(path,{
            method: "PUT",
            headers:{
               'accept':"application/json",
                'Content-Type':"application/json",
                'Authorization':'Token: ' + getLocalStorage('logintoken')
            },
        })
        .then(function(r){
            if(r.status ===400){
                alert("Can not follow/unfollow yourself");
            }
            else if(r.status === 200){
                alert(`${followrornot} user ${username} success`);
            }
        })

    }


    //create the post
    function createFeed(post){
        var li = document.createElement("li");
        li.className ="post";
        li.setAttribute("data-id-post","");
        li.setAttribute("id",post.id);
        feedul.appendChild(li);
        var votediv = document.createElement("div");
        li.appendChild(votediv);
        votediv.className ="vote";
        votediv.setAttribute("data-id-upvotes","");
        votediv.setAttribute("id",`${post.id}-votediv`);
        var contentdiv = document.createElement("div");
    
        li.appendChild(contentdiv);
        contentdiv.className = "content";
        var title = document.createElement("h4");
        contentdiv.appendChild(title);
    
        title.className = "post-title alt-text";
        title.setAttribute("data-id-title","");
        title.appendChild(document.createTextNode(post.title));
        var author = document.createElement("p");
        contentdiv.appendChild(author);
        author.className = "post-author";
        author.setAttribute("data-id-author","");
        author.setAttribute("id",`${post.id}-author`)
        author.appendChild(document.createTextNode(`Posted by @${post.meta.author}`));


        //show the number of upvotes to these posts

        votediv.appendChild(document.createTextNode(`votes:${post.meta.upvotes.length}`));


        //add time to each post
        var mytime = createElement('h5',getTime(post.meta.published),{
            class:"post-time"
        });
        
        li.appendChild(mytime);

        //add onclick function to these name.
        author.onclick = function(e){
            e.cancelBubble = true;
            showInfoByname(post.meta.author);
        }



        //add vote button
        votediv.appendChild(createElement('button',"upvote",{
            calss:"votebutton",
            id:`${post.id}-votebutton`
        }));
        votediv.appendChild(createElement('button',"unvote",{
            calss:"votebutton",
            id:`${post.id}-unvotebutton`
        }));
        votediv.appendChild(createElement('button',"comment",{
            calss:"votebutton",
            id:`${post.id}-commentbutton`
        }));

        //add click listener to those button

        addOnclikToAllpost(post.id);

        //show comment and upvotes to those posts
        showUpvotesAndComments(post.id,'logintoken');

        //check whether it is logged in
        //add the delete and change button to the my post 

        if(document.getElementById("my-mypost-button") && document.getElementById("my-mypost-button").innerText ==="FEED"){
            //ban the scroll function
          
            votediv.appendChild(createElement('button',"delete",{
                calss:"deletebutton",
                id:`${post.id}-deletebutton`
            }));
            votediv.appendChild(createElement('button',"update",{
                calss:"updatebutton",
                id:`${post.id}-updatebutton`
            }));

            //add click listener to my post 
            addDeleteAndChangeToPost(post.id);
        }


    }


    
    //live update the comment

    //bugs found here
    //fixed in 8/8/2019
    async function liveUpdate(id){
        var path = `${apiUrl}/user`;
        const promise = fetch(path,{
            method: 'GET',
            headers: {'accept':"application/json",
                    'Content-Type':"application/json",
                    'Authorization':'Token: ' + getLocalStorage('logintoken')}
        });
        const res = await promise;
        const json = await res.json();
        //console.log(json);

        var pathid = `${apiUrl}/post/?id=${id}`;
        const anotherpromise = fetch(pathid,{
            method: 'GET',
            headers: {'accept':"application/json",
                    'Content-Type':"application/json",
                    'Authorization':'Token: ' + getLocalStorage('logintoken')}
        });
        const anotherres = await anotherpromise;
        const anotherjson = await anotherres.json();
        //console.log(anotherjson)
        var hasupvoted = 0;
        for (var i of anotherjson.meta.upvotes){
            if( i == json.id){
                hasupvoted = 1;
            }        
        }

        return hasupvoted;
    }


    //add listener to these post
    function addOnclikToAllpost(id){
             
        var upvotebutton = document.getElementById(`${id}-votebutton`);
        var path = `${apiUrl}/post/vote?id=${id}`;


        liveUpdate(id).then(function(myr){
           
            //has been upvoted
            if (myr==1){
                localStorage.setItem(`${id}-canupvotes`,"false");
                localStorage.setItem(`${id}-canunvotes`,"true");
            }      
            else{
                localStorage.setItem(`${id}-canupvotes`,"true");
                localStorage.setItem(`${id}-canunvotes`,"false");
            }
        })
        
        upvotebutton.onclick = function(e){
            e.cancelBubble = true;
            if(!getLocalStorage('logintoken')){
                alert("you need to log in first");
                return;
            }
            //check this one has upvote it or not;

            if(getLocalStorage(`${id}-canupvotes`)==='true'){
                fetch(path,{
                    method: 'PUT',
                    headers: {'accept':"application/json",
                            'Content-Type':"application/json",
                            'Authorization':'Token: ' + getLocalStorage('logintoken')}
                })
                .then(function(r){
                    if( r.status === 200){
                        //check if has been voted
                        
                        //change the content without reload the website;
                        
                        var mydiv = document.getElementById(`${id}-votediv`);
                        var number =mydiv.firstChild.nodeValue.split(':')[1];
                        mydiv.firstChild.nodeValue = `votes:${parseInt(number) + 1}`;
                        localStorage.setItem(`${id}-canupvotes`,"false");
                        localStorage.setItem(`${id}-canunvotes`,"true");
                        
                        alert("vote success");
                        
                    }
                    else{
                        alert("can not upvote before login");
                    }                
                });
            }
        }

        var unvotebutton = document.getElementById(`${id}-unvotebutton`);

        unvotebutton.onclick = function(e){            
            e.cancelBubble = true;

            if(!getLocalStorage('logintoken')){
                alert("you need to log in first");
                return;
            }

            if(getLocalStorage(`${id}-canunvotes`)==='true'){
                fetch(path,{
                    method: 'PUT',
                    headers: {'accept':"application/json",
                            'Content-Type':"application/json",
                            'Authorization':'Token: ' + getLocalStorage('logintoken')}
                })
                .then(function(r){
                    if( r.status === 200){
                        
                        var mydiv = document.getElementById(`${id}-votediv`);
                        var number =mydiv.firstChild.nodeValue.split(':')[1];
                        mydiv.firstChild.nodeValue = `votes:${parseInt(number) - 1}`;
                        localStorage.setItem(`${id}-canupvotes`,"true");
                        localStorage.setItem(`${id}-canunvotes`,"false");
                        alert("remove upvote success");
                    
                    }
                    else alert("can not remove upvote before login");                     
                });
            }
            
        }

        //add function to comment button
        var commentbutton = document.getElementById(`${id}-commentbutton`);
        commentbutton.onclick = function(e){
            e.cancelBubble = true;
            if(!getLocalStorage('logintoken')){
                alert("you need to log in first");
                return;
            }
            var modal = document.getElementById("myModal");

            var span = document.getElementsByClassName("close")[0];
            modal.style.display = "block";


            span.onclick = function() {
                modal.style.display = "none";
                deleteChildInmodal();
            }

            window.onclick = function(event) {
                if (event.target == modal) {
                    modal.style.display = "none";
                    deleteChildInmodal();
                }
            }

            const textarea = createElement("textarea","",{
                id:"mytextarea"
            });
            modalcontent.appendChild(textarea);    
            const testarea_button = createElement("button","yes,comment",{
                class:"button", 
                id: "mytextarea_button"
            })
            modalcontent.appendChild(testarea_button);

            testarea_button.onclick= function(){
                
                if(textarea.value === ""){
                    alert("comment can not be empty");
                }
                var commentinfo = {
                    "comment":textarea.value
                }
                var path = `${apiUrl}/post/comment?id=${id}`;
                fetch(path,{
                    method: 'PUT',
                    body: JSON.stringify(commentinfo),
                    headers: {'accept':"application/json",
                            'Content-Type':"application/json",
                            'Authorization':'Token: ' + getLocalStorage('logintoken')}
                })
                .then(r=>r.json())
                .then(function(r){
                    alert("comment success");
                    modal.style.display = "none";
                    deleteChildInmodal();
                    localStorage.setItem(`postcomment-${id}`,id);
                    
                    localStorage.setItem(`comment-content-${id}`,textarea.value);
                });
                //.catch(e=>alert(e));
            }
        }
        
    }





    //add post 
    //or update the post for level 3
    function addPost(token){

        var modal = document.getElementById("myModal");
    
        var span = document.getElementsByClassName("close")[0];
        modal.style.display = "block";
    
        span.onclick = function() {
            modal.style.display = "none";
            deleteChildInmodal();
        }
    
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
                deleteChildInmodal();
            }
        }
        const texttitle = createElement("textarea","",{
            placeholder:"enter your title",
            id:"mytexttitle"
        })
        modalcontent.appendChild(texttitle);
        const textsubseddit = createElement("textarea","",{
            placeholder:"enter your subseddit",
            id:"mytextsubseddit"
        })
        modalcontent.appendChild(textsubseddit);
        const textarea = createElement("textarea","",{
            placeholder:"enter your content",
            id:"mytextarea"
        });
        modalcontent.appendChild(textarea);    
        const testarea_button = createElement("button","yes,post",{
            class:"button", 
            id: "mytextarea_button"
        })
        modalcontent.appendChild(testarea_button);
        const uploadimg = createElement("input","",{
            id:"myuploadimg",
            class:"button-secondary",
            type:"file"
        })
        modalcontent.appendChild(uploadimg);
    

        var imgUrl="";
        uploadimg.onchange =function(event){
            //upload the image.
            const myimg = event.target.files[0];
            if(myimg.type === "image/jpeg" || myimg.type ==="image/png" || myimg.type ==="image/jpg"){
                var reader = new FileReader();
                reader.onload= function(e){
                    imgUrl = e.target.result.split(',')[1];
                    //console.log(imgUrl)

                    //show the img
                    modalcontent.appendChild(createElement("img","",{
                        src:`${e.target.result}`
                    }))
    
                }
                reader.readAsDataURL(myimg);
            }
            else{
                alert("you need to choose an image");  
            }
        }

    
        testarea_button.onclick=function(){
    
            if(textarea.value == ""){
                alert("please input something");
            }else{
                if(imgUrl === null){
                    imgUrl = "";
                }
                const mypost = {
                    title:`${texttitle.value}`,
                    text:`${textarea.value}`,
                    subseddit:`${textsubseddit.value}`,
                    image:`${imgUrl}`
                }
                console.log(mypost);
                
                var path = `${apiUrl}/post`;
                
      
                //if login,then can post.
                if(token){
    
                    fetch(path,{
                        method: `POST`,
                        body: JSON.stringify(mypost),
                        headers: {'accept':"application/json",
                                   'Content-Type':"application/json",
                                   'Authorization':'Token: ' + getLocalStorage(token)
                                }
                    })
                    .then(r => r.json())
                    .then(r =>{
                        alert("post success");
                        location.reload();
                        
                    });
                    //.catch(error=>alert(error));
    
                }
    
            }
    
        }
        
    
    }
    //add lisener to the add post putton
    post_button.onclick= function(){
        var token = getLocalStorage("logintoken");
        if(token){
    
            addPost("logintoken");
        }
        else{
            alert("you need to log in first");
        }
    
    }

    //to show the votes number,level 2 profile
    async function showupvotesNumber(posts){
        var numberofvote = 0;
        const postpromises = posts.map((post)=>
            fetch(`${apiUrl}/post/?id=${post}`,{
                method: "GET",
                headers:{
                    'accept':"application/json",
                    'Content-Type':"application/json",
                    'Authorization':'Token: ' + getLocalStorage('logintoken')
                }
            })
        );
    
        const responses = await Promise.all(postpromises)
        const jsons = await Promise.all(responses.map(res => res.json()));
        
        for(var json of jsons){            
        
            numberofvote += json.meta.upvotes.length;
        }
        
        return numberofvote;        
    }


    //function for search
    function searchThePost(){
        var mysearch = document.getElementById("search");
        mysearch.onkeydown = function(e){
            if(e.which === 13){
                //search the post when press enter
                fetch(`${apiUrl}/user`,{
                    method: "GET",
                    headers:{
                        'accept':"application/json",
                        'Content-Type':"application/json",
                        'Authorization':'Token: ' + getLocalStorage('logintoken')
                    }
                })
                .then(r=>r.json())
                .then(function(r){
                    if(mysearch.value === ""){
                        deleteFeed();
                        getUserFeed('logintoken');
                    }
                    else
                        if(!getLocalStorage('logintoken')){
                            alert("you need to login before search");
                        }
                        getPostFromAllId(r.following,mysearch.value.toLowerCase());
                })
                
                
            }
        }
    }
    searchThePost();

    //get all posts from the follwing list
    async function getPostFromAllId(ids,searchcontent){
        const idPromis = ids.map((id)=>
            fetch(`${apiUrl}/user/?id=${id}`,{
                method: "GET",
                headers:{
                    'accept':"application/json",
                    'Content-Type':"application/json",
                    'Authorization':'Token: ' + getLocalStorage('logintoken')
                }
            })
        )

        const responses = await Promise.all(idPromis);
        //get all user info
        const jsons = await Promise.all(responses.map(response=>response.json()));
        var myarr = [];
        
        for(var json of jsons){
            //add all followint posts;
            myarr = myarr.concat(json.posts);
        }
        //console.log(myarr);

        const postPromis = myarr.map((post)=>
            fetch(`${apiUrl}/post/?id=${post}`,{
                method: "GET",
                headers:{
                    'accept':"application/json",
                    'Content-Type':"application/json",
                    'Authorization':'Token: ' + getLocalStorage('logintoken')
                }
            })
        )
        const postresponses = await Promise.all(postPromis);
        const postjsons = await Promise.all(postresponses.map(res=>res.json()));
        //flag to record find or not
        var hasdelete = 0;
        var found = 0;
        for(var json of postjsons){
            if(json.text.toLowerCase().search(searchcontent)!=-1 || 
            json.title.toLowerCase().search(searchcontent)!=-1){
                //delete the original feed
                if(!hasdelete){
                    //delete the original feed
                    deleteFeed();
                    hasdelete = 1;
                }
                found = 1;
                createFeed(json);
            }
        }
        if(!found){
            alert(`No posts contains ${searchcontent}`);
        }

    }






    

    //show the upvote and comment of certain post
    function showUpvotesAndComments(id,token){

        if(getLocalStorage(token) === null){
            return;
        }
        
        const mypostdiv = document.getElementById(id);
        //console.log(document.getElementById(205));
        var path = `${apiUrl}/post/?id=${id}`;
        fetch(path,{
            method: "GET",
            headers:{
            'accept':"application/json",
                'Content-Type':"application/json",
                'Authorization':'Token: ' + getLocalStorage(token)
            }
        })
        .then(r=>r.json())
        .then(function(r){        
            //console.log(r);
            mypostdiv.onclick=function(){
                var modal = document.getElementById("myModal");

                var span = document.getElementsByClassName("close")[0];
                modal.style.display = "block";
        
        
                span.onclick = function() {
                    modal.style.display = "none";
                    deleteChildInmodal();
                    
                }
                window.onclick = function(event) {
                    if (event.target == modal) {
                        modal.style.display = "none";
                        deleteChildInmodal();
                    }
                }

                //add content to the modal
                
                var comments = r.comments;
                var upvotes = r.meta.upvotes;
                var mycomment = comments.length;
                var myflag = 1;
                if(getLocalStorage(`postcomment-${id}`)){
                    mycomment +=1;
                    myflag = 0;
                }

                //show the comment
                if(mycomment > 0){
                    modalcontent.appendChild(createElement('p',`comments:`,{}));
                    if(myflag === 0){
                        modalcontent.appendChild(createElement('div',`author:${getLocalStorage('currentusername')}
                        \xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\content:${getLocalStorage(`comment-content-${id}`)}`,{}));
                        // localStorage.removeItem(`postcomment-${id}`);
                        // localStorage.removeItem(`comment-content-${id}`);

                    }
        
                    for(var i of comments){
        
                        modalcontent.appendChild(createElement('div',`author:${i.author}\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\content:${i.comment}`,{}));
                    }
                }
                else{

                    modalcontent.appendChild(createElement('p',`No comments yet`,{}));
                }

                //show the upvote
                if(upvotes.length > 0){
                    
                    var myp = createElement('p',`upvotes:`,{});
                    
                    var mybutton = createElement("button","show upvotes",{
                        class:"button",
                        id:"post-showupvotes-button"
                    });

                    myp.appendChild(mybutton);
                    modalcontent.appendChild(myp);

                    mybutton.onclick = ()=>{
                        var modal = document.getElementById("myListModal");

                        var span = document.getElementById("mylistclose");
                        modal.style.display = "block";
                
                
                        span.onclick = function() {
                            modal.style.display = "none";
                            deleteChildInListmodal();
                        }      
                        addFollowButtonToList(upvotes);
                    }          
                }
                else{

                    modalcontent.appendChild(createElement('p',`No upvotes yet`,{}));
                }
                //show the text content

                
                var myp = createElement('p',`text:`,{});
                var mytextbutton = createElement("button","show text",{
                    class:"button",
                    id:"post-showtext-button"
                });

                
                myp.appendChild(mytextbutton);
                modalcontent.appendChild(myp);
                mytextbutton.onclick = function(){
                    //show the content and img
                    
                    var modal = document.getElementById("myListModal");

                    var span = document.getElementById("mylistclose");
                    modal.style.display = "block";


                    span.onclick = function() {
                        modal.style.display = "none";
                        deleteChildInListmodal();
                    }    

                    if(r.text && r.thumbnail){
                    
                        listmodalcontent.appendChild(createElement("p",`${r.text}`,{}));
                        console.log(`data:image,base64,${r.thumbnail}`);
                        listmodalcontent.appendChild(createElement("img","",{
                            src:`data:image;base64,${r.thumbnail}`
                        }))

                    }
                    else if(!r.thumbnail) {
                        listmodalcontent.appendChild(createElement("p",`${r.text}`,{}));
                    }
                    else{
                        alert("no text content in this post");
                    }
                }
        
            }
        });
        //.catch(e => alert(e));
        
    }

   
    // ginve the token key,get the feed of some token
    //the post belong to oneself does not show

    function getUserFeed(token,page = 0, number = 10){
        var path = `${apiUrl}/user/feed?p=${page}&n=${number}`;
        fetch(path,{
            method: "GET",
            headers:{
            'accept':"application/json",
                'Content-Type':"application/json",
                'Authorization':'Token: ' + getLocalStorage(token)
            }
        })
        .then(r=>r.json())   
        .then(function(r){
           
            if(r.posts.length > 0){
                for(var i of r.posts.sort(sortTheTime)){
                    createFeed(i);
                }
            }
        });
            
    }

    //function for infinite srcoll
    var mypage = 10;
    async function getUserFeedScroll(token,page = 0, number = 10){
        
        
        window.onscroll =null;
        var path = `${apiUrl}/user/feed?p=${page}&n=${number}`;
        const mypromise = fetch(path,{
            method: "GET",
            headers:{
            'accept':"application/json",
                'Content-Type':"application/json",
                'Authorization':'Token: ' + getLocalStorage(token)
            }
        });
        const res = await mypromise;
        const jsons = await res.json();

        mypage += jsons.posts.length;
        if(jsons.posts.length == 10){
            for(var i of jsons.posts){
                createFeed(i);
            }
            window.onscroll = ()=>myscroll();
        }
        else{
            for(var i of jsons.posts){
                createFeed(i);
            }
            window.onscroll = null;
        }     
        
    }

 


    //delete element in the modal
    function deleteChildInmodal(){
        const length = modalcontent.children.length;
        for(var i  = length - 1; i >= 1; i--){ 
            // console.log(modalcontent.children[i]);
            const parent = modalcontent.children[i].parentNode;
            parent.removeChild(modalcontent.children[i]);
        }
     
    }

    //same as above
    function deleteChildInListmodal(){
    
        const length = listmodalcontent.children.length;
        for(var i  = length - 1; i >= 1; i--){ 
            // console.log(modalcontent.children[i]);
            var parent = listmodalcontent.children[i].parentNode;
            parent.removeChild(listmodalcontent.children[i]);
        }
     
    }

    //create a new element, make it a function
    function createElement(element,textnode,attribute={}){
        const ele = document.createElement(element);
        ele.appendChild(document.createTextNode(textnode));
        for (let [key,value] of Object.entries(attribute)){
            ele.setAttribute(key,value);
        }
        return ele;
    }

    //get the local storage
    function getLocalStorage(key){
        if(window.localStorage){
            return window.localStorage.getItem(key);
        }
        else{
            return null;
        }
    }

    //scroll function 
    function myscroll(){   
        if(document.getElementById("my-mypost-button")){
            if(document.getElementById("my-mypost-button").innerText === 'MY POST'){  
                if(isEnd()){
                    getUserFeedScroll('logintoken',mypage);      
    
                }
            }
        }
    }

    //in the end of the window
    function isEnd(){
        var scrollHeight = document.documentElement.scrollTop;
        var viewheight = document.documentElement.offsetHeight;
        var documentheight = document.body.scrollHeight;
        console.log(scrollHeight,"scrollHeight");
        console.log(viewheight,"viewheight");
        console.log(documentheight,"documentheight");
        return documentheight - scrollHeight -viewheight < 20;
    }

    //add listener to scroll
    window.onscroll = ()=>myscroll();





}

export default initApp;

