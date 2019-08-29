from app import api,db
from util.globals import *
from util.models import *
from flask_restplus import Resource, abort, reqparse, fields
from flask import request

user = api.namespace('user', description='User Information Services')

@user.route('/', strict_slashes=False)
class User(Resource):
    @user.response(200, 'Success', user_details)
    @user.response(403, 'Invalid Auth Token')
    @user.response(400, 'Malformed Request')
    @user.expect(auth_details)
    @user.param('id','Id of user to get information for (defaults to logged in user)')
    @user.param('username','username of user to get information for (defaults to logged in user)')
    @user.doc(description='''
        Gets the information for the supplied user, if neither id nor username is specified the
        user corresponding to the supplied auth token's information is returned.
        If both are supplied the id is used first and on failure the username is used.
        If either supplied form of identification is invalid the request is considered malformed and may be rejected.
        The response object contains a list of user_ids of the user following
        the target user and the total number of people who follow the target user.
        These are contained in the variables following and followed_num respectively.
        The response also contains the list of posts by the target user referenced
        by their post id. use the GET /post to retrive the entire post
    ''')
    def get(self):
        u = authorize(request)
        u_id = request.args.get('id', None)
        username = request.args.get('username', None)

        # extract information from paramtaters
        if u_id or username:
            try:
                if u_id and db.exists("USER").where(id=u_id):
                    u_id = int(u_id)
                elif username and db.exists("USER").where(username=username):
                    u_id = int(db.select("USER").where(username=username).execute()[0])
                else:
                    abort(400, 'Malformed Request')
            except:
                abort(400, 'Malformed Request')
        else:
            u_id = int(u[0])

        # get information
        u = db.select('USER').where(id=u_id).execute()
        u_username = u[1]

        follow_list = text_list_to_set(u[4])
        posts_raw = db.select_all('POST').where(author=u_username).execute()
        posts = [post[0] for post in posts_raw]
        return {
            'username': u[1],
            'name': u[2],
            'id'  : int(u[0]),
            'email': u[3],
            'following': [int(x) for x in follow_list],
            'followed_num': u[5],
            'posts': posts
        }

    @user.response(403, 'Invalid Authorization Token')
    @user.response(200, 'Success')
    @user.response(400, 'Malformed user object')
    @user.expect(auth_details,user_update_details)
    @user.doc(description='''
        Updates the user referenced by the supplied auth token
        to match the given object.
        The given object can update name, email or password.
        At least one of above must be supplied or the request is
        considered malformed.
        Again password must be at least 1 character. Come on guys.
    ''')
    def put(self):
        u = authorize(request)
        u_id = int(u[0])
        if not request.json:
            abort(400, 'Malformed request')

        allowed_keys=['password','name','email']
        safe = {}
        valid_keys = [k for k in request.json.keys() if k in allowed_keys]
        if len(valid_keys) < 1:
            abort(400, 'Malformed request')
        if "password" in valid_keys and request.json["password"] == "":
            abort(400, 'Malformed request')
        for k in valid_keys:
            safe[k] = request.json[k]
        db.update('USER').set(**safe).where(id=u_id).execute()
        return {
            "msg": "success"
        }

@user.route('/feed', strict_slashes=False)
class Feed(Resource):
    @user.response(403, 'Invalid Auth Token')
    @user.response(200, 'Success', post_list_details)
    @user.expect(auth_details)
    @user.param('n','Number of posts to fetch, 10 by default')
    @user.param('p','What post to start at, 0 by default')
    @user.doc(description='''
        Returns a array of posts for the user pointed to by
        the given auth token. These posts are sorted in reverse
        chronological order (newest first) and are a combination
        of everyone the user pointed to by the auth token follows.
        The users own posts do not show up here.
        The paramater p specifies where to begin reading and n specified the
        length of the read.
        N must be greater then 0 and p must be equal to or greater then 0, providing
        p and n otherwise will give you a 400.
        If you wanted to get 2 pages worth of posts you would do (p=0,n=10) to
        get the first 10 posts and (p=10,n=10) to get the next 10. The first one
        would return posts 0,1,2,3,4,5,6,7,8,9 etc.
    ''')
    def get(self):
        u = authorize(request)
        try:
            n = int(request.args.get('n',10))
            p = int(request.args.get('p',0))
        except:
            abort(400, 'Malformed Request')
        if n <= 0 or p < 0:
            abort(400, 'Malformed Request')
        following = text_list_to_set(u[4],process_f=lambda x:int(x))
        following = [db.select('USER').where(id=int(id)).execute()[1] for id in following]
        wildcards = ','.join(['?']*len(following))
        q = 'SELECT * FROM POSTS WHERE author in ({})'.format(wildcards)

        all_posts = db.raw(q,following)
        all_posts = [format_post(row) for row in all_posts]
        all_posts.sort(reverse=True,key=lambda x: int(float(x["meta"]["published"])))

        return {
            'posts': all_posts[p:p+n]
        }

@user.route('/follow', strict_slashes=False)
class Follow(Resource):
    @user.response(200, 'Success')
    @user.response(403, 'Invalid Auth Token')
    @user.response(400, 'Malformed Request')
    @user.expect(auth_details)
    @user.param('username','username of person to follow')
    @user.doc(description='''
        Allows the current user pointed to by the auth token to follow
        a specified user. If they are already following the user nothing is done.
        username must be supplied and must be a valid username.
    ''')
    def put(self):
        u = authorize(request)
        u_id = int(u[0])
        follow_list = text_list_to_set(u[4], process_f=lambda x: int(x))
        to_follow = request.args.get('username',None)
        if to_follow == None or not db.exists('USER').where(username=to_follow):
            abort(400,'Malformed Request')
        if to_follow == u[1]:
            abort(400,'Malformed Request')
        to_follow = db.select('USER').where(username=to_follow).execute()[0]

        if to_follow not in follow_list:
            db.raw('UPDATE USERS SET FOLLOWED_NUM = FOLLOWED_NUM + 1 WHERE ID = ?',[to_follow])
        follow_list.add(to_follow)
        db.update('USER').set(following=set_to_text_list(follow_list)).where(id=u_id).execute()
        return {
            'message': 'success'
        }

@user.route('/unfollow', strict_slashes=False)
class UnFollow(Resource):
    @user.response(200, 'Success')
    @user.response(403, 'Invalid Auth Token')
    @user.response(400, 'Malformed Request')
    @user.expect(auth_details)
    @user.param('username','username of person to follow')
    @user.doc(description='''
        Allows the current user pointed to by the auth token to unfollow
        a specified user. If they are not following the user nothing is done.
        Username must be supplied and must be a valid username.
    ''')
    def put(self):
        u = authorize(request)
        u_id = int(u[0])
        follow_list = text_list_to_set(u[4], process_f=lambda x: int(x))
        to_follow = request.args.get('username',None)
        if to_follow == u[1]:
            abort(400,'Malformed Request')
        if to_follow == None or not db.exists('USER').where(username=to_follow):
            abort(400,'Malformed Request Or Unknown username')
        to_follow = db.select('USER').where(username=to_follow).execute()[0]
        if to_follow in follow_list:
            db.raw('UPDATE USERS SET FOLLOWED_NUM = FOLLOWED_NUM - 1 WHERE ID = ?',[to_follow])
        follow_list.discard(to_follow)
        db.update('USER').set(following=set_to_text_list(follow_list)).where(id=u_id).execute()

        return {
            'message': 'success'
        }
