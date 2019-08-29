from app import api,db
from util.globals import *
from util.models import *
from flask_restplus import Resource, abort, reqparse, fields
from PIL import Image
from io import BytesIO
import base64
import time
from flask import request

dummy = api.namespace('dummy', description='Dummy Endpoints for testing')

def shrink(src):
    size = (150,150)
    im = Image.open(BytesIO(base64.b64decode(src)))
    im.thumbnail(size, Image.ANTIALIAS)
    buffered = BytesIO()
    im.save(buffered, format='PNG')
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

@dummy.route('/post', strict_slashes=False)
class Dummy_Post(Resource):
    @dummy.response(200, 'Success', post_id_details)
    @dummy.response(400, 'Malformed Request / Image could not be processed')
    @dummy.expect(new_post_details)
    @dummy.doc(description='''
        Identical to POST /post but doesn't require any authentication
        Allows you to act as a "Anon" user.
    ''')
    def post(self):
        j = request.json
        u = get_dummy_user()
        u_username = u[1]
        if not j:
            abort(400, 'Malformed request')

        (desc, title, subseddit) = unpack(j, 'text', 'title', 'subseddit')
        src = j.get('image', None)
        if desc == "":
            abort(400, 'Malformed request')
        thumbnail = ''

        if src != None and src != "":
            try:
                thumbnail = shrink(src)
            except:
                abort(400,'Image Data Could Not Be Processed')
        post_id = db.insert('POST').with_values(
            author=u_username,
            description=desc,
            title=title,
            published=str(time.time()),
            likes='',
            thumbnail=thumbnail,
            src=src,
            tag=subseddit
        ).execute()
        return {
            'post_id': post_id
        }

    @dummy.response(200, 'Success')
    @dummy.response(400, 'Malformed Request')
    @dummy.param('id','the id of the post to update')
    @dummy.expect(new_post_details)
    @dummy.doc(description='''
        Identical to PUT /post but doesn't require any authentication
        Allows you to act as a "Anon" user.
    ''')
    def put(self):
        j = request.json
        id = request.args.get('id',None)
        u = get_dummy_user()
        u_username = u[1]
        if not j or not id:
            abort(400, 'Malformed request')
        id = int(id)
        if not db.exists('POST').where(id=id):
            abort(400, 'Malformed request')
        # check the logged in user made this post
        post_author = db.select('POST').where(id=id).execute()[1]
        if u[1] != post_author:
            # exposing what post id's are valid and unvalid
            # may be a security issue lol
            abort(403, 'You Are Unauthorized To Edit That Post')
        (title,desc,src) = unpack(j,'title','description_text','src',required=False)
        if desc == None and src == None:
            abort(400, 'Malformed Request')
        updated = {}
        if desc:
            updated['description'] = desc
        if src:
            updated['src'] = src
        if title:
            updated['title'] = title
        db.update('POST').set(**updated).where(id=id).execute()
        return {
            'message': 'success'
        }

    @dummy.response(200, 'Success')
    @dummy.response(400, 'Missing Username/Password')
    @dummy.param('id','the id of the post to delete')
    @dummy.doc(description='''
        Identical to DELETE /post but does not require any authentication
        Allows you to act as a "Anon" user.
    ''')
    def delete(self):
        u = get_dummy_user()
        id = request.args.get('id',None)
        if not id:
            abort(400,'Malformed Request')
        id = int(id)
        if not db.exists('POST').where(id=id):
            abort(400,'Malformed Request')
        p = db.select('POST').where(id=id).execute()
        if p[1] != u[1]:
            abort(403,'You Are Unauthorized To Make That Request')
        comment_list = text_list_to_set(p[7])
        [db.delete('COMMENT').where(id=c_id).execute() for c_id in comment_list]
        db.delete('POST').where(id=id).execute()
        return {
            'message': 'success'
        }
    @dummy.response(200, 'Success',post_details)
    @dummy.response(400, 'Missing Username/Password')
    @dummy.param('id','the id of the post to fetch')
    @dummy.doc(description='''
        Identical to GET /post but doesn't require any authentication
        Allows you to act as a "Anon" user.
    ''')
    def get(self):
        u = get_dummy_user()
        id = request.args.get('id',None)
        if not id:
            abort(400,'Malformed Request')
        id =int(id)
        p = db.select('POST').where(id=id).execute()
        if not p:
            abort(400,'Malformed Request')
        return format_post(p)

@dummy.route('/post/vote', strict_slashes=False)
class Vote(Resource):
    @dummy.response(200, 'Success')
    @dummy.response(400, 'Malformed Request')
    @dummy.param('id','the id of the post to upvote')
    @dummy.doc(description='''
        Identical to PUT /post/vote but doesn't require any authentication
        Allows you to act as a "Anon" user.
    ''')
    def put(self):
        u = get_dummy_user()
        id = request.args.get('id',None)
        if not id:
            abort(400, 'Malformed request')
        id = int(id)
        if not db.exists('POST').where(id=id):
            abort(400, 'Malformed request')

        p = db.select('POST').where(id=id).execute()
        votes = text_list_to_set(p[5],process_f=lambda x:int(x))
        votes.add(u[0])
        votes = set_to_text_list(votes)
        db.update('POST').set(likes=votes).where(id=id).execute()
        return {
            'message': 'success'
        }

    @dummy.response(200, 'Success')
    @dummy.response(400, 'Malformed Request')
    @dummy.param('id','the id of the post to remove an upvote from')
    @dummy.doc(description='''
        Identical to DELETE /post/vote but doesn't require any authentication
        Allows you to act as a "Anon" user.
    ''')
    def delete(self):
        u = get_dummy_user()
        id = request.args.get('id',None)
        if not id:
            abort(400, 'Malformed request')
        id = int(id)
        if not db.exists('POST').where(id=id):
            abort(400, 'Malformed request')
        p = db.select('POST').where(id=id).execute()
        votes = text_list_to_set(p[5],process_f=lambda x: int(x))
        if not u[0] in votes:
            abort(400, 'Malformed request')
        votes.discard(u[0])
        votes = set_to_text_list(votes)
        db.update('POST').set(likes=votes).where(id=id).execute()
        return {
            'message': 'success'
        }

@dummy.route('/post/comment', strict_slashes=False)
class Comment(Resource):
    @dummy.response(200, 'Success')
    @dummy.response(400, 'Malformed Request')
    @dummy.param('id','the id of the post to comment on')
    @dummy.expect(comment_details)
    @dummy.doc(description='''
        Identical to PUT /comment but doesn't require any authentication
        Allows you to act as a "Anon" user.
    ''')
    def put(self):
        u = get_dummy_user()
        j = request.json
        id = request.args.get('id',None)
        if not id or not j:
            abort(400, 'Malformed request')
        id = int(id)
        if not db.exists('POST').where(id=id):
            abort(400, 'Malformed request')
        (comment,) = unpack(j,'comment')
        if comment == "":
            abort(400, 'Malformed request')
        comment_id = db.insert('COMMENT').with_values(
            comment=comment,
            author=u[1],
            published=str(time.time())
        ).execute()
        p = db.select('POST').where(id=id).execute()
        comment_list = text_list_to_set(p[7],process_f=lambda x: int(x))
        comment_list.add(comment_id)
        comment_list = set_to_text_list(comment_list)
        db.update('POST').set(comments=comment_list).where(id=id).execute()
        return {
            'message': 'success'
        }


@dummy.route('/user', strict_slashes=False)
class User(Resource):
    @dummy.response(200, 'Success', user_details)
    @dummy.response(400, 'Malformed Request')
    @dummy.param('id','Id of user to get information for (defaults to logged in user)')
    @dummy.doc(description='''
        Identical to GET /user but doesn't require any authentication
        Allows you to act as a "Anon" user.
    ''')
    def get(self):
        u = get_dummy_user()
        u_id = int(request.args.get('id',u[0]))
        if not db.exists('USER').where(id=u_id):
            abort(400,'Malformed Request')
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

    @dummy.response(200, 'Success')
    @dummy.response(400, 'Malformed user object')
    @dummy.expect(user_update_details)
    @dummy.doc(description='''
        Identical to PUT /user but doesn't require any authentication
        Allows you to act as a "Anon" user.
    ''')
    def put(self):
        u = get_dummy_user()
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
            "message": "success"
        }
@dummy.route('/user/feed', strict_slashes=False)
class Feed(Resource):
    @dummy.response(200, 'Success', post_list_details)
    @dummy.param('n','Number of posts to fetch, 10 by default')
    @dummy.param('p','What post to start at, 0 by default')
    @dummy.doc(description='''
        Identical to GET /feed but doesn't require any authentication
        Allows you to act as a "Anon" user.
    ''')
    def get(self):
        u = get_dummy_user()
        n = request.args.get('n',10)
        p = request.args.get('p',0)
        following = text_list_to_set(u[4],process_f=lambda x:int(x))
        following = [db.select('USER').where(id=int(id)).execute()[1] for id in following]
        wildcards = ','.join(['?']*len(following))
        q = 'SELECT * FROM POSTS WHERE author in ({})'.format(wildcards)
        q+=' LIMIT ? OFFSET ?'
        following.append(n)
        following.append(p)
        all_posts = db.raw(q,following)
        all_posts = [format_post(row) for row in all_posts]
        all_posts.sort(reverse=True,key=lambda x: int(float(x["meta"]["published"])))
        return {
            'posts': all_posts
        }

@dummy.route('/user/follow', strict_slashes=False)
class Follow(Resource):
    @dummy.response(200, 'Success')
    @dummy.response(400, 'Malformed Request')
    @dummy.param('username','username of person to follow')
    @dummy.doc(description='''
        Identical to PUT /user/follow but doesn't require any authentication
        Allows you to act as a "Anon" user.
    ''')
    def put(self):
        u = get_dummy_user()
        u_id = int(u[0])
        follow_list = text_list_to_set(u[4])
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

@dummy.route('/user/unfollow', strict_slashes=False)
class UnFollow(Resource):
    @dummy.response(200, 'Success')
    @dummy.response(400, 'Malformed Request')
    @dummy.param('username','username of person to follow')
    @dummy.doc(description='''
        Identical to PUT /user/unfollow but doesn't require any authentication
        Allows you to act as a "Anon" user.
    ''')
    def put(self):
        u = get_dummy_user()
        u_id = int(u[0])
        following = text_list_to_set(u[4])
        to_follow = request.args.get('username',None)
        if to_follow == u[1]:
            abort(400,'Malformed Request')
        if to_follow == None or not db.exists('USER').where(username=to_follow):
            abort(400,'Malformed Request Or Unknown username')
        to_follow = db.select('USER').where(username=to_follow).execute()[0]
        if to_follow in following:
            db.raw('UPDATE USERS SET FOLLOWED_NUM = FOLLOWED_NUM - 1 WHERE ID = ?',[to_follow])
        following.discard(to_follow)
        db.update('USER').set(following=set_to_text_list(following)).where(id=u_id).execute()

        return {
            'message': 'success'
        }
