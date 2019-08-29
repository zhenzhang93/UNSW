import os
from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from util.DB_Interface import DB

app = Flask(__name__)
CORS(app)

@app.route('/soft-reset', strict_slashes=False)
def reset():
    db.raw("DELETE FROM USERS WHERE USERNAME LIKE \"TESTERELLA%\"")
    db.raw("DELETE FROM POSTS WHERE AUTHOR LIKE \"TESTERELLA%\"")
    db.raw("DELETE FROM COMMENTS WHERE AUTHOR LIKE \"TESTERELLA%\"")
    db.raw("DELETE FROM POSTS WHERE AUTHOR = \"Anon\"")
    db.raw("DELETE FROM COMMENTS WHERE AUTHOR = \"Anon\"")
    db.raw('DELETE FROM USERS WHERE USERNAME = "Anon"')
    db.raw('INSERT INTO USERS VALUES(1,"Anon","Anon","password","Anon@unsw.edu.au","","",0)')
    return ':)'

api = Api(app)
db = DB()

if 'HOST' in os.environ:
    print()
    print('***')
    print('*** cd to the frontend directory (probably cd ../frontend')
    print('*** then run the frontend server telling it the URL FOR the backend server like this:')
    print('*** python3 frontend_server.py http://{}:{}'.format(os.environ['HOST'], os.environ['PORT']))
    print('***')
    print()
