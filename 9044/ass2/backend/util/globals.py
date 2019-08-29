import secrets
from app import db
from flask_restplus import Resource, abort, reqparse, fields

def unpack(j,*args,**kargs):
    r = [j.get(arg,None) for arg in args]
    if kargs.get("required",True):
        [abort(kargs.get("error",400)) for e in r if e == None]
    return r

def gen_token():
    token = secrets.token_hex(32)
    while db.exists("USER").where(curr_token=token):
        token = secrets.token_hex(32)
    return token

def authorize(r):
    t = r.headers.get('Authorization',None)
    if not t:
        abort(403,'Unsupplied Authorization Token')
    try:
        t = t.split(" ")[1]
    except:
        abort(403,'Invalid Authorization Token')
    if not db.exists("USER").where(curr_token=t):
        abort(403,'Invalid Authorization Token')
    return db.select("USER").where(curr_token=t).execute()

def get_dummy_user():
    return db.select("USER").where(id=1).execute()

def text_list_to_set(raw,process_f=lambda x:x):
    if raw == None:
        return set()
    return set([process_f(x) for x in raw.split(",") if x != ''])

def set_to_text_list(l):
    return ",".join([str(x) for x in l])

def format_post(post):
    comments = []
    for c_id in text_list_to_set(post[8], process_f=lambda x:int(x)):
        comment = db.select("COMMENT").where(id=c_id).execute()
        comments.append({
            "author":  comment[1],
            "published":  comment[2],
            "comment": comment[3]
        })
    return {
        "id": post[0],
        "text": post[3],
        "title": post[2],
        "meta": {
            "author": post[1],
            "subseddit": post[9],
            "published": post[4],
            "upvotes": list(text_list_to_set(post[5],process_f=lambda x:int(x)))
        },
        "thumbnail": post[6],
        "image": post[7],
        "comments": comments
    }
