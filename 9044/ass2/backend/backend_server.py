#!/usr/bin/env python3

#
# DO NOT CHANGE THIS FILE
#

import os, sys, sqlite3

DATABASE_URL = 'https://cgi.cse.unsw.edu.au/~cs2041/19T2/seddit.sqlite3'

def main(host='127.0.0.1', port=None):
    try:
        create_database()
        check_database()
        run(host, port)
    except ImportError as e:
        print('ERROR:', e, file=sys.stderr)
        if sys.version_info < (3,6):
            print('The backend requires Python 3.6 or later - you appear to be using Python {}.{}'.format(*sys.version_info), file=sys.stderr)
        else:
            print('A module required by the backend is missing.', file=sys.stderr)
            print('See the instructions in backend/README.md for installing the required modules.', file=sys.stderr)
            print('Ask in the forum if you can not fix this problem.', file=sys.stderr)
        sys.exit(1)

def run(host, port):
    if port is not None:
        run1(host, port)
    else:
        for port in range(5000, 5100):
            try:
                run1(host, port)
                break
            except OSError as e:
                if 'Address in use' in str(e):
                    continue

def run1(host, port):
    from app import app
    import namespaces.post
    import namespaces.auth
    import namespaces.user
    import namespaces.dummy
    os.environ['HOST'] = host
    os.environ['PORT'] = str(port)
    app.run(debug=True, host=host, port=port)

def create_database():
    database_dir = os.path.join('db')
    database_file = os.path.join(database_dir, 'test.sqlite3')
    if not os.path.exists(database_dir):
        print(' * [DATABASE WIZARD] No db folder was detected, Creating', database_dir)
        os.mkdir(database_dir)
    if not os.path.exists(database_file):
        print(' * [DATABASE WIZARD] No db file was detected, Creating', database_file)
        import ssl, urllib.request
        with urllib.request.urlopen(DATABASE_URL, context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)) as response:
            db = response.read()
        with open(database_file, "wb") as f:
            f.write(db)
        print(' * [DATABASE WIZARD]', database_file, 'created')

def check_database():
    database_dir = os.path.join('db')
    database_file = os.path.join(database_dir, 'test.sqlite3')
    print(' * [DATABASE WIZARD] Checking Database')
    conn = sqlite3.connect(database_file)
    c = conn.cursor()
    all_users = c.execute("SELECT id,following FROM USERS").fetchall()
    for u in [x for x in all_users if "0" in str(x[1]).split(",")]:
        print(f' * [DATABASE WIZARD] ... Patching user {u[0]}')
        fl = ",".join([str(int(x) + 2) for x in u[1].split(",")])
        c.execute("UPDATE USERS SET FOLLOWING=? WHERE ID=?",(fl, u[0]))
    all_posts = c.execute("SELECT id,likes FROM POSTS").fetchall()
    
    for p in [x for x in all_posts if "0" in str(x[1]).split(",")]:
        print(f' * [DATABASE WIZARD] ... Patching post {p[0]}')
        ll = ",".join([str(int(x) + 2) for x in p[1].split(",")])
        c.execute("UPDATE POSTS SET LIKES=? WHERE ID=?",(ll, p[0]))
    conn.commit()
    c.close()
    conn.close()
    print(' * [DATABASE WIZARD] Database Healthy')

def usage():
    print('Usage:', sys.argv[0], '[host]', '[port]')
    print('or:', sys.argv[0], '[port]')
    print('or:', sys.argv[0])

if __name__ == "__main__":
    try:
        if len(sys.argv) == 3:
            main(host=sys.argv[1], port=int(sys.argv[2]))
        elif len(sys.argv) == 2:
            main(port=int(sys.argv[1]))
        elif len(sys.argv) == 1:
            main()
        else:
            usage()
    except ValueError:
        usage()