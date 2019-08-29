from app import api,db
from util.globals import *
from util.models import *
from flask_restplus import Resource, abort, reqparse, fields
from PIL import Image
from io import BytesIO
import base64
import time
from flask import request

posts = api.namespace('post', description='Post Services')

def shrink(src):
    size = (150,150)
    im = Image.open(BytesIO(base64.b64decode(src)))
    im.thumbnail(size, Image.ANTIALIAS)
    buffered = BytesIO()
    im.save(buffered, format='PNG')
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

@posts.route('/public', strict_slashes=False)
class Global(Resource):
    @posts.response(200, 'Success', post_list_details)
    @posts.doc(description='''Allows a non-auth'd user to fetch the latest 20 posts by all users.''')
    def get(self):
        q = 'SELECT * FROM POSTS p ORDER BY p.published DESC LIMIT 20'

        latest_posts = db.raw(q, [])
        latest_posts = [format_post(row) for row in latest_posts]
        latest_posts.sort(reverse=True,key=lambda x: int(float(x["meta"]["published"])))

        return {
            'posts': latest_posts
        }


@posts.route('/', strict_slashes=False)
class Post(Resource):
    @posts.response(200, 'Success', post_id_details)
    @posts.response(403, 'Invalid Auth Token')
    @posts.response(400, 'Malformed Request / Image could not be processed')
    @posts.expect(auth_details,new_post_details)
    @posts.doc(description='''
        Lets you make a new post. Text and Title must be supplied, however providing a image is
        optional. The Supplied text/title must be non empty and if provided the image must be a valid
        png image encoded in base 64 (only png is supported at the present moment).
        If either of these requirements is not met the request is considered malformed.
        Note the image just needs to be the base64 data, no meta data such as 'data:base64;'
        is required. Putting it in will make the data invalid.
        Returns the post_id of the new post on success.
    ''')
    def post(self):
        j = request.json
        u = authorize(request)
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

    @posts.response(200, 'Success')
    @posts.response(403, 'Invalid Auth Token / Unauthorized to edit Post')
    @posts.response(400, 'Malformed Request')
    @posts.param('id','the id of the post to update')
    @posts.expect(auth_details, update_post_details)
    @posts.doc(description='''
        Lets you update a post without changing metadata.
        Published date, upvotes, comments etc. will be left untouched.
        At least one of the paramaters must be supplied.
        The id of the post to update must also be supplied,
        a invalid id will make the request be considered malformed.
        The current user pointed to by the auth token must be
        the author of the post pointed to by id otherwise a
        unauthorized error will be raised.\
        Provided strings must be non empty or else the request is considered malformed.
    ''')
    def put(self):
        j = request.json
        try:
            id = int(request.args.get('id',None))
        except:
            abort(400, 'Malformed request')
        u = authorize(request)
        u_username = u[1]
        if not j or not id:
            abort(400, 'Malformed request')
        if not db.exists('POST').where(id=id):
            abort(400, 'Malformed request')
        # check the logged in user made this post
        post_author = db.select('POST').where(id=id).execute()[1]
        if u[1] != post_author:
            # exposing what post id's are valid and unvalid
            # may be a security issue lol
            abort(403, 'You Are Unauthorized To Edit That Post')
        (desc,title,src) = unpack(j,'text','title','image',required=False)
        if desc == None and src == None and title == None:
            abort(400, 'Malformed Request')
        if desc != None and desc == '':
            abort(400, 'Malformed Request')
        if src != None and src == '':
            abort(400, 'Malformed Request')
        if title != None and title == '':
            abort(400, 'Malformed Request')
        updated = {}
        if desc:
            updated['description'] = desc
        if src:
            updated['src'] = src
            updated['thumbnail'] = shrink(src)
        if title:
            updated['title'] = title
        db.update('POST').set(**updated).where(id=id).execute()
        return {
            'message': 'success'
        }

    @posts.response(200, 'Success')
    @posts.response(400, 'Missing Username/Password')
    @posts.response(403, 'Invalid Auth Token')
    @posts.expect(auth_details)
    @posts.param('id','the id of the post to delete')
    @posts.doc(description='''
        Lets you delete the post referenced by 'id'.
        id must be supplied and the user pointed to by
        the auth token must be the author of the post.
        If the user is not the autor of the post referenced
        by 'id' a unauthorized error is raised.
        If id is invalid or not supplied the request is considered
        malformed.
    ''')
    def delete(self):
        u = authorize(request)
        try:
            id = int(request.args.get('id',None))
        except:
            abort(400, 'Malformed request')
        if not id:
            abort(400,'Malformed Request')
        if not db.exists('POST').where(id=id):
            abort(400,'Malformed Request')
        p = db.select('POST').where(id=id).execute()
        if p[1] != u[1]:
            abort(403,'You Are Unauthorized To Make That Request')
        comment_list = text_list_to_set(p[8])
        [db.delete('COMMENT').where(id=c_id).execute() for c_id in comment_list]
        db.delete('POST').where(id=id).execute()
        return {
            'message': 'success'
        }
    @posts.response(200, 'Success',post_details)
    @posts.response(400, 'Missing Username/Password')
    @posts.response(403, 'Invalid Auth Token')
    @posts.expect(auth_details)
    @posts.param('id','the id of the post to fetch')
    @posts.doc(description='''
        Lets you fetch a post referenced by 'id'.
        id must be supplied and valid, the request is considered
        malformed otherwise.\
        The returned object contains standard information such as
        the description text, username of the author, and published time
        as a UNIX Time Stamp.\
        In addition the meta section of the object contains a list of user id's
        of the users who have upvoted the post.\
        The src is supplied in base64 encoding as is a thumbnail,
        The thumbnail is of size 150px by 150px.\
        If there was no image on the post both src and thumbnail are null.\
        There is also a list of comments supplied. Each comment has the comment text,
        the username of the author who made the comment and a UNIX timestamp of
        the the comment was posted.
    ''')
    def get(self):
        u = authorize(request)
        try:
            id = int(request.args.get('id',None))
        except:
            abort(400, 'Malformed request')
        p = db.select('POST').where(id=id).execute()
        if not p:
            abort(400,'Malformed Request')
        return format_post(p)

@posts.route('/vote', strict_slashes=False)
class Vote(Resource):
    @posts.response(200, 'Success')
    @posts.response(403, 'Invalid Auth Token')
    @posts.response(400, 'Malformed Request')
    @posts.param('id','the id of the post to vote on')
    @posts.expect(auth_details)
    @posts.doc(description='''
        Lets the user pointed to by the auth token upvote
        the post referenced by 'id'.
        'id' must be supplied and valid, the request is considered
        malformed otherwise.
        If the post is already upvoted by the user pointed to by the auth token
        nothing is done.
    ''')
    def put(self):
        u = authorize(request)
        try:
            id = int(request.args.get('id',None))
        except:
            abort(400, 'Malformed request')
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

    @posts.response(200, 'Success')
    @posts.response(403, 'Invalid Auth Token')
    @posts.response(400, 'Malformed Request')
    @posts.param('id','the id of the post to remove an upvote for')
    @posts.expect(auth_details)
    @posts.doc(description='''
        Lets the user pointed to by the auth token remove their upvote for
        the post referenced by 'id'.
        'id' must be supplied and valid, the request is considered
        malformed otherwise.
        If the post is not upvoted by the user pointed to by the auth token
        nothing is done.
    ''')
    def delete(self):
        u = authorize(request)
        try:
            id = int(request.args.get('id',None))
        except:
            abort(400, 'Malformed request')
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

@posts.route('/comment', strict_slashes=False)
class Comment(Resource):
    @posts.response(200, 'Success')
    @posts.response(403, 'Invalid Auth Token')
    @posts.response(400, 'Malformed Request')
    @posts.param('id','the id of the post to comment on')
    @posts.expect(auth_details,comment_details)
    @posts.doc(description='''
        Lets the user pointed to by the auth token comment on
        the post referenced by 'id'.
        'id' must be supplied and valid, the request is considered
        malformed otherwise.
        The posted json must contain a "comment" field with a non
        empty comment as the value, otherwise the request is considered
        malformed.
    ''')
    def put(self):
        u = authorize(request)
        j = request.json
        try:
            id = int(request.args.get('id',None))
        except:
            abort(400, 'Malformed request')
        if not j:
            abort(400, 'Malformed request')
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
        comment_list = text_list_to_set(p[8],process_f=lambda x: int(x))
        comment_list.add(comment_id)
        comment_list = set_to_text_list(comment_list)
        db.update('POST').set(comments=comment_list).where(id=id).execute()
        return {
            'message': 'success'
        }
