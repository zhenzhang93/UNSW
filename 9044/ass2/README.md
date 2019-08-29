<!--
    DO NOT CHANGE THIS FILE - IT MAY BE UPDATED DURING THE ASSIGNMENT
-->
## Seddit - Introduction

JavaScript is used increasingly to provide a native-like application experience in the web. One
major avenue of this has been in the use of Single Page Applications or SPAs. SPAs
are generated, rendered, and updated using JavaScript. Because SPAs don't require a user
to navigate away from a page to do anything, they retain a degree of user and application state.

There are millions of websites that utilise SPAs in part of, or all of their web applications.

The assignment intends to teach students to build a simple SPA which can fetch dynamic data from a HTTP/S API.
Your task will be to provide an implemention of a SPA that can provide a number of key features.

Some of the skills/concepts this assignment aims to test (and build upon):

* Simple event handling (buttons)
* Advanced Mouse Events (Swipe)
* Fetching data from an API
* Infinite scroll
* CSS Animations
* Web Workers / Service Workers
* Push Notifications (Polling)
* Offline Support
* Routing (URL fragment based routing)

## API

The backend server will be where you'll be getting your data. Don't touch the code in the backend; although we've provided the source, 
it's meant to be a black box. Final testing will be done with our own backend so don't _assume_ any single piece of data will be there. Use the instructions provided in the backend/README.md
to get it started.

For the full docs on the API, start the backend server and navigate to the root (very likely to be `localhost:5000`, the exact url will be printed when you run the backend, see backend/README.md for more info). You'll see all the endpoints, descriptions and expected responses.

## A Working Product
Your application should be compatible with 'modern' Chrome, Safari, and Mozilla browsers.
We will assume your browser has JavaScript enabled, and supports ES6 syntax.

### Writing HTML - Restrictions

You are not permitted to edit the HTML provided in  *frontend/index.html* except you may change the `<head></head>` section to add your own styles and scripts.

You are not permitted to add HTML files.

You must create the HTML entirely via your JavaScript scripts.  Your task is to manipulate and control your application _entirely_ dynamically!

Also please use `.innerHTML` sparingly.  Using `.innerHTML` amounts to the same thing as hardcoding your HTML.  You'll be penalised if you rely on this method.  Ask in the forum if you require more information.

You are not permitted to use Javascript written by other people.

You are not permitted to use NPM to install packages.

You are not permitted to use frameworks (React, Angular, Vue ...)

You are permitted to use small snippets of general purpose code from external sources such as Stack Overflow with proper attribution.

## Getting Started
Clone the repository provided. It has a whole bunch of code, documentation, and a whole working server you'll need for
developing your frontend applicaiton.

Please read the relevant docs for setup in the folders `/backend` and `/frontend` of the provided repository.
Each folder outlines basic steps to get started. There are also some comments provided in the frontend source code.

## Milestones
Level 0 focuses on the basic user interface and interaction with of the site.
There is no need to implement any integration with the backend for this level.
When demonstrating the functionality included in level 0, you are not required to prevent access 
to login-protected pages - all pages may be accessible by changing the URL.

### Level 0

**Login**
```html
<!-- 
    Before seeing the login form, a 'Log In' button
    should exist on the page. The button _must_
    have the following data attribute.
    This is important for autotests.
-->
<button data-id-login>Log In</button>
```
The site presents a login form where a user can present their credentials. Since we do not need to 
interact with the backend for level 0, all attempts to log in would fail. Thus, you should allow 
the site to inform the user that authentication has failed.

**Registration**

```html
<!-- 
    Before seeing the form, a 'Sign Up' button
    should exist on the page. The button _must_
    have the following data attribute.
    This is important for autotests.
-->
<button data-id-signup>Sign Up</button>
```
An option to register for "Seddit" should be presented on the home page. This option will allow 
the user to create an account by entering a set of credentials (username and password) which they 
can then use to sign up to "Seddit". Again, since we are not required to interact with the backend 
for level 0, all attempts to create a new account will fail. You must perform basic input 
validation (think about the format of the user input you may receive) and handle cases where the 
input credentials should be rejected in the case of user error or (eventual) server rejection due 
to conflicting credential details.

**Feed Interface** 
```html
<!-- 
    The 'feed' _must_
    have the following id attribute.
    This is important for autotests.
-->
<ul id="feed">...</ul>
```
The application should present a "feed" of user content on the home page derived from the sample feed.json provided.
The posts should be displayed in reverse chronological order (most recent posts first). You can hardcode how this works for
this milestone.

Although this is not a graphic design exercise you should produce pages with a common and somewhat distinctive look-and-feel. You may find CSS useful for this.

```html
<!-- 
    Each 'post'  _must_
    have the following data attribute.
    This is important for autotests.
-->
<li data-id-post>...</li>
```
Each post must include:
1. who the post was made by (must include `data-id-author`)
2. when it was posted
3. The image itself, if there is one present
4. How many upvotes it has (or none) (must include `data-id-upvotes`)
5. The post title (must include `data-id-title`)
6. The post description text
7. How many comments the post has
8. What suseddit this was posted to i,e `/s/meme`

While completing these tasks for level 0, consider the future inclusion of HTTP requests when 
designing your code - this will be helpful for future levels.

## Level 1
Level 1 focuses on fetching data from the API.

**Login**
The login form now communicates with the backend (`POST /login`) after input validation to verify 
whether the provided credentials are valid for an existing user. Once the user has logged in, they 
should see their own news feed (the home page).

NB. This is slightly different to what they will see as a
non-logged in user. A non-logged in user should still see posts from `GET /post/public`.

**Registration**
The option to register for "Seddit" (implemented in level 0) should now accept a set of 
credentials (a username / password pair). This user information is then POSTed to the backend to 
create the user in the database (`POST /signup`). 

**Feed Interface**
The content shown in the user's feed is sourced from the backend (`GET /user/feed`). Contrary to 
the existing popular system which "Seddit" is based off, there is only one location where all posts 
are to appear at this level of functionality. In the actual system called reddit posts are organised into similar groups called "sub-reddits" so all posts about plants are grouped under `r/plants` allowing plant lovers to only see those posts. seddit copies this by letting users specify the subseddit of a post when creating it so people can make posts under `s/plants` but the feed we are asking you to implement aggregates **all** posts regardless of which subseddit they were posted to.

In level 4 you will implement multiple subseddits where posts are organised into groups much like reddit.

## Level 2
Level 2 focuses on a richer UX and will require some further backend interaction.

**Show Upvotes**
Allow an option for a logged in user to see a list of all users who have upvoted a post.
Possibly a [modal](https://www.webopedia.com/TERM/M/modal_window.html) but the design is up to you.

**Show Comments**
Allow an option for a logged in user to see all the comments on a post. Same as above.

**Upvote user generated content**
A logged in user can upvote a post on their feed and trigger a api request (`PUT /post/vote`)
For now it's ok if the upvote doesn't show up until the page is refreshed.

In addition the user can also retract their upvote, you can do this via `DELETE /post/vote`

**Post new content**
Logged in users can upload and post new content from a [modal](https://www.webopedia.com/TERM/M/modal_window.html) or seperate page via (`POST /post`). The uploaded content can either be text or text and an image.

**Pagination**
Logged in users can page between sets of results in the feed using the position token with (`GET /user/feed`).
Note users can ignore this if they properly implement Level 3's Infinite Scroll.

**Profile**
Logged in users can see their own profile information such as username, number of posts, 
number of upvotes across all posts. Get this information from (`GET /user`)

## Level 3
Level 3 focuses on more advanced features that will take time to implement and will
involve a more rigourously designed app to execute.

**Infinite Scroll**
Instead of pagination, users an infinitely scroll through the "subseddit" they are viewing. 
For infinite scroll to be properly implemented you need to progressively load posts as you scroll. 

**Comments**
Logged in users can write comments on "posts" via (`PUT /post/comment`)

**Live Update**
If a logged in user upvotes a post or comments on a post, the posts upvotes and comments should
update without requiring a page reload/refresh.

**Update Profile**
Users can update their personal profile via (`PUT /user`) E.g:
* Update email address
* Update password
* etc.

**User Pages**
Let a logged in user click on a user's name/picture from a post and see a page with the users name and other info.
The user should also see on this page all posts made by that person across all "subseddits".
The user should be able to see their own page as well.

This can be done as a [modal](https://www.webopedia.com/TERM/M/modal_window.html) or as a separate page (url fragmentation can be implemented if wished.)

**Follow**
Let a logged in user follow/unfollow another user too add/remove their posts to their feed via (`PUT user/follow`)
Add a list of everyone a user follows in their profile page.
Add just the count of followers / follows to everyones public user page

**Delete/Update Post**
Let a logged in user update a post they made or delete it via (`DELETE /post`) or (`PUT /post`)

**Search functionality**
Let a logged in user search for a post made by any user that they follow. You'll have to 
potentially combine a few different endpoint responses to allow this. 

## Level 4
This set of tasks is an extension beyond the previous levels and should only be attempted once the previous levels have been completed.

**Multiple Subseddits**
As mentioned earlier, a subseddit is denoted by a "s/" in front of the subseddit name. Users should be able to make a post to a specific subseddit (which may or may not have been posted to before). A logged in user should also be able to view the posts made to a specific subseddit. You may choose to show this in the URL as `/s/:subseddit_name` if you wish. The original news feed - which presented the `s/all` subseddit - must still remain as the home page and must also show all posts made across all subseddits. Any post that is not posted to a specific subseddit must appear on `s/all`.

**Slick UI**
The user interface looks good, is performant, makes logical sense, and is usable. 

**Push Notifications**
Users can receive push notifications when a user they follow posts an image. There is no endpoint or websocket provided, we expect you to figure out how to do this given the existing endpoints. Notice that since we do not give you a websocket (nor teach it in the course) we are happy for you to use polling ot achieve this, i.e check if there is anything to notify the user of every 5 or so seconds.

The delay is up to you, but remember you want it to look semi live without 
overwhelming the event queue.

**Offline Access**
Users can access the "Seddit" at all times by using Service Workers to cache the page (and previous content) locally.
d
**Fragment based URL routing**
Users can access different pages using URL fragments:

```
/#profile=1
/#feed
/#profile=420
```

# FAQ

1. I get a 403 (invalid auth token) on all my api requests?

Make sure you are authorized, remember you need to set your header with the token the login endpoing returned to you. 

```js
const options = {
    headers: {
        'Authorization' : `Token ${myToken}`
    }
} 
fetch("/user", options)
```

Just for playing around you can use the `/dummy` endpoints which let you skip this step but do note you need working auth for most of the levels.

2. How do i know what a endpoint takes in and what it returns?

Run the backend server and navigate to the root, usualy 127.0.0.1:5000 or similar. There is a full set of docs which outlines every url you can hit, what method to use, a description, the paramaters it needs and the structure of the response it gives. It also outlines every possible error code it returns.

3. I'm getting a '500' error

That means that the server is crashing, this might mean your doing something really weird the backend wasn't ready to handle, in general check the forum in this case. We may have just made a oopsie.
