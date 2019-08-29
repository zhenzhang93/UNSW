<!--
    DO NOT CHANGE THIS FILE - IT MAY BE UPDATED DURING THE ASSIGNMENT
-->
## Seddit - Frontend

## Recommended Steps for tackling the assignment
1. Get something basic working with the data provided in `frontend/data`
2. Once you've got something basic working, start hitting the `/dummy/` API, which doesn't require authentication. See docs.
3. Finally, once you've got that working, transition over to use the real API.

## Quickstart

To start up the frontend server which simply servers everything under the frontend folder:

```
python3 frontend_server.py
```

This will print out a username, password and launch up a static server at localhost:8080, if something else on your network is using 8080 it will start it on some other port.

```
Live at http://localhost:8080
use username 'user' and password '8tv1oz'
```

Use control-c to shut this server down.

When you visit the link you will be prompted for a username and password, use the ones printed to the console. This is to prevent other students on the same network as you being able to see your code.

In addition we've provided a basic project scaffold for you to build from.
You can use everything we've given you, although there's no requirement to use anything.
```bash
# scaffold
data
  - feed.json  # A sample feed data object
  - users.json # A sample list of user/profile objects
  - post.json  # A sample post object

src
  - main.js   # The main entrypoint for your app
  - api.js    # Some example code for your api logic

styles
  - post.css
  - provided.css  # some sample css we've provided (add more stylesheets as you please)
```

To make sure everything is working correctly we strongly suggest you read the instructions in both backend and frontend,
and try to start both servers (frontend and backend).
