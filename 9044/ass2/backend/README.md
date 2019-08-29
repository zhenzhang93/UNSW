<!--
    DO NOT CHANGE THIS FILE - IT MAY BE UPDATED DURING THE ASSIGNMENT
-->
## Seddit Backend

You are given a backend server for seddit written in Python.

Do not change any file in the backend directory.

You only submit the seddit frontend.

Any changes you make to the backend will be lost.

If you depend on changes you make to the backend your code will break.

## Running the Backend @ CSE

Running the backend on a CSE machine is simple:
  
```bash
$ 2041 ass2_backend
```

Visit the url it prints (e.g. http://127.0.0.1:5000/) to see the backend docs!

Note if other students are running a sever on the same machine you will give a different URL (port).

The backend server will print out a message telling you how to run the frontend server.

This command ensures correct URL for the backend server is passed to your frontend Javascript.

## Running the Backend on your Own Machine

You can use virtual env [recommended].

```bash
cd backend
# create a sandbox for the backend 
virtualenv -p /usr/local/bin/python3 env

# enter sandbox
source env/bin/activate
# set up sandbox
pip install -r requirements.txt
# run backend! Will print out a bunch of info including a line like this:
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# visit the url on this line (e.g. http://127.0.0.1:5000/) to see the backend docs!
python backend_server.py
```

Once you are done working on the assignment run the following
command to exit the sandbox

```bash
deactivate
```

This method creates a space in which the backend can run without
clashing with any other python packages and issues on your local account. If you don't care you can run the backend in the global space as such.

```bash
cd backend
# on your local system this may just be pip and python not pip3 and python3
pip3 install -r requirements.txt
python3 app.py
```

# User Data

in `backend/db/users.csv` there is a list of all users within the provided database, you can login as any of these users for testing or create your own account. Note that in the case that you put the database in a undesirable state such as accidently making too many accounts or comments on a post etc. simply delete the file `backend/db/test.sqlite3` and restart the backend server. The server will automatically detect the missing file and download a fresh copy.
