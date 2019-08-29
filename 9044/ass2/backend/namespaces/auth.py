from app import api,db
from util.globals import *
from util.models import *
from flask_restplus import Resource, abort, reqparse, fields
from flask import request
auth = api.namespace('auth', description='Authentication Services')

@auth.route('/login', strict_slashes=False)
class Login(Resource):
    @auth.response(200, 'Success',token_details)
    @auth.response(400, 'Missing Username/Password')
    @auth.response(403, 'Invalid Username/Password')
    @auth.expect(login_details)
    @auth.doc(description='''
        This is used to authenticate a verified account created through signup.
        Returns a auth token which should be passed in subsequent calls to the api
        to verify the user.
    ''')
    def post(self):
        if not request.json:
            abort(400,'Malformed Request')
        (un,ps) = unpack(request.json,'username','password')
        if not db.exists('USER').where(username=un,password=ps):
            abort(403,'Invalid Username/Password')
        t = gen_token()
        db_r = db.update('USER').set(curr_token=t).where(username=un)
        db_r.execute()
        return {
            'token': t
        }

@auth.route('/signup', strict_slashes=False)
class Signup(Resource):
    @auth.response(200, 'Success',token_details)
    @auth.response(400, 'Malformed Request')
    @auth.response(409, 'Username Taken')
    @api.expect(signup_details)
    @auth.doc(description='''
        Use this endpoint to create a new account,
        username must be unique and password must be non empty
        After creation api retuns a auth token, same as /login would
    ''')
    def post(self):
        if not request.json:
            abort(400,'Malformed Request')
        (un,ps,em,n) = unpack(request.json,'username','password','email','name')

        if ps == '' or un == '':
            abort(400, 'Malformed Request')

        if db.exists('USER').where(username=un):
            abort(409, 'Username Taken')

        t = gen_token()
        db_r = db.insert('USER').with_values(
            curr_token=t,
            username=un,
            password=ps,
            email=em,
            name=n
        )
        db_r.execute()
        return {
            'token': t
        }
