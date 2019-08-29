import sqlite3
import os
from random import randint, choice
import requests
import base64
from tqdm import tqdm
from PIL import Image
from io import BytesIO

desc = [
    "It's a delight to trust somebody so completely.",
    "It's mysterious what attracts you to a person.",
    "I, uh, don't think I'm, y'know, so different than your average, y'know, average.",
    "It's nice to play a character that has a soulful, dependent, close relationship. It must mean my character is interesting in some way.",
    "I travel for work, but recently, friends said I should take major trips.",
    "I love to be directed. They can trust me and go.",
    "No matter how you travel, it's still you going.",
    "If any movie people are watching this show, please, for me, have some respect. You wanna sell some tickets, act like you know what you're talking about.",
    "The woods are lovely,dark and deep,But I have promises to keep, and miles to go before I sleep. - Robert Frost",
    "Someone I loved once gave me a box full of darkness,it took me years to understand that this,too, was a gift.",
    "And so being young, and dipped in folly, I fell in love with melancholy. - Edgar Allan Poe",
    "We were together, I forgot the rest. - Walt Whitman",
    "There is freedom waiting for you, on the breezes of sky, and you ask “what if I fall?”, Oh but my darling, what if you fly? - Erin Hanson",
    "Photos are the only way,to hold on to what you knew, because the moments they show never change, when the people in them do.- Erin Hanson",
    "There will come a day I know it, when you'll love yourself as I love you, and you won't view your scars as ugly,but a tally of times you made it through.- E.H.",
    "This life is but a garden bed,the rain it comes and goes, but you can prick yourself on all the thorns, or you can learn to love the rose.- E.H.",
    "You told me that you had my back, and I thought that it was true, now my shadow's still behind me, but where on earth are you? - E.H.",
    "There's untamed electricity,coursing through his veins, and it shocks you when you kiss him, but my god it's worth the pain. - E.H.",
    "I let my phone ring into silence, since I am not who they're looking for, although they might have the right number, I'm not the right person anymore. - E.H.",
    "Let me be your one, let me be your only,let me be the only thing, that stops you feeling lonely. - E.H.",
    "Every time they're at the sea, the oceans start to weep, wishing they were half as wide, as his love for her is deep. E.H.",
    "He stood alone for a million souls",
    "He was a warrior without a sword.",
    "You own me with your words and distance me with punctuations ?!",
    "More of you I used in my poetry, more of me I spent in you.",
    "Make sure my poetries don't change your mind, cause your pictures once changed mine.",
    "Each time I type your name the backspace freezes.",
    "I swear I believed all your 'I swear's",
    "I will write,dad; I will be right.",
    "A fist full of dust and me; a sky full of star-dust and you.",
    "His family was Hindu enough to ask,her family was Muslim enough to accept.",
    "HerNOs were replied by HNO3 on her face",
    "The unexamined life is not worth living",
    "Whereof one cannot speak, thereof one must be silent",
    "Entities should not be multiplied unnecessarily",
    "The life of man (in a state of nature) is solitary, poor, nasty, brutish, and short",
    "I think therefore I am...Cogito, ergo sum”",
    "He who thinks great thoughts, often makes great errors",
    "We live in the best of all possible worlds",
    "What is rational is actual and what is actual is rational",
    "God is dead! He remains dead! And we have killed him.",
    "There is but one truly serious philosophical problem, and that is suicide",
    "One cannot step twice in the same river",
    "The greatest happiness of the greatest number is the foundation of morals and legislation",
    "To be is to be perceived",
    "Happiness is not an ideal of reason but of imagination",
    "No man's knowledge here can go beyond his experience",
    "God is not willing to do everything, and thus take away our free will and that share of glory which belongs to us",
    "Liberty consists in doing what one desires",
    "It is undesirable to believe a proposition when there is no ground whatever for supposing it true",
    "Even while they teach, men learn",
    "There is only one good, knowledge, and one evil, ignorance",
    "If God did not exist, it would be necessary to invent Him",
    "This is patently absurd; but whoever wishes to become a philosopher must learn not to be frightened by absurdities",
    "One cannot conceive anything so strange and so implausible that it has not already been said by one philosopher or another",
    "Leisure is the mother of philosophy",
    "Philosophy is a battle against the bewitchment of our intelligence by means of language",
    "There is only one thing a philosopher can be relied upon to do, and that is to contradict other philosophers",
    "We are what we repeatedly do. Excellence, then, is not an act, but a habit",
    "Only one man ever understood me, and he didn’t understand me",
    "The mind is furnished with ideas by experience alone",
    "Life must be understood backward. But it must be lived forward",
    "Science is what you know. Philosophy is what you don't know",
    "Metaphysics is a dark ocean without shores or lighthouse, strewn with many a philosophic wreck",
    "Philosophy is at once the most sublime and the most trivial of human pursuits",
    "History is Philosophy teaching by examples",
    "He who is unable to live in society, or who has no need because he is sufficient for himself, must be either a beast or a god",
    "You can discover more about a person in an hour of play than in a year of conversation",
    "Things alter for the worse spontaneously, if they be not altered for the better designedly",
    "All that is necessary for the triumph of evil is that good men do nothing",
    "Is man merely a mistake of God's? Or God merely a mistake of man's?",
    "I would never die for my beliefs because I might be wrong",
    "Religion is the sign of the oppressed ... it is the opium of the people",
    "Happiness is the highest good",
    "If men were born free, they would, so long as they remained free, form no conception of good and evil",
    "The greater the difficulty, the more glory in surmounting it",
    "Whatever is reasonable is true, and whatever is true is reasonable",
    "Morality is not the doctrine of how we may make ourselves happy, but of how we may make ourselves worthy of happiness",
    "Man is condemned to be free",
    "It is one thing to show a man that he is in error, and another to put him in possession of truth",
    "I don’t know why we are here, but I’m pretty sure it is not in order to enjoy ourselves",
    "That man is wisest who, like Socrates, realizes that his wisdom is worthless",
    "The only thing I know is that I know nothing",
    "All is for the best in the best of all possible worlds",
    "The function of prayer is not to influence God, but rather to change the nature of the one who prays",
    "Man is born free, but is everywhere in chains",
    "Man will never be free until the last king is strangled with the entrails of the last priest",
    "If you would be a real seeker after truth, it is necessary that at least once in your life you doubt, as far as possible, all things",
    "Happiness lies in virtuous activity, and perfect happiness lies in the best activity, which is contemplative",
    "I can control my passions and emotions if I can understand their nature",
    "Philosophers have hitherto only interpreted the world in various ways; the point, however, is to change it",
    "It is wrong always, everywhere and for everyone, to believe anything upon insufficient evidence",
    "Virtue is nothing else than right reason",
    "Freedom is secured not by the fulfilling of one's desires, but by the removal of desire",
    "In everything, there is a share of everything",
    "A little philosophy inclineth man's mind to atheism; but depth in philosophy bringeth men’s minds about to religion",
    "The brave man is he who overcomes not only his enemies but his pleasures",
    "Good and evil, reward and punishment, are the only motives to a rational creature",
    "To do as one would be done by, and to love one's neighbor as oneself, constitute the ideal perfection of utilitarian morality",
    "Everything that exists is born for no reason, carries on living through weakness, and dies by accident",
    "Man is the measure of all things",
    "We are too weak to discover the truth by reason alone",
    "The mind is furnished with ideas by experience alone"
]

comment_store = [
    "lol",
    "lmao",
    "nice!",
    "mood",
    "JEALOUS!",
    "wish i was there",
    "sorry to hear about the divorce...",
    "tell the kids i love them!",
    "WOW!",
    "wowee",
    "wowweeeee",
    "wOwEeeee",
    "so cool!",
    "I love this shot!",
    "really makes you think...",
    "that is so crazy hahaha",
    "haha this is so cool we should take photos together... haha jk .... unless?",
    "my grandma takes better photos then you",
    "bit rough there",
    "wow! what is your setup like?",
    "what camera do you use?",
    "this changed my life",
    "i am in LOVE",
    "this sucks",
    "are you kidding me? unfollowed",
    "omg sick invite",
    "you are so right",
    "this is so cute",
    "adorable i can't wait to see what you make next :)",
    "is that what i think it is?",
    "good but not as good as my stuff",
    "i have nothing better to do so i'm gonna say this is bad",
    "give up honestly",
    "just..wow amazing work!",
    "ok sure but you realise that according to all known laws of aviation bees should not be able to fly and that really feeds into my theory about how all birds are fake, think about it have you eve- oh no the FBI are here, TELL MY TRU-",
    "birds are real stop asking",
    "the sky! wow! it exists huh!",
    "big mood",
    "wow bood",
    "i for one disagree but i respect your opinion",
    "i agree! why are more people not saying this",
    "um i don't like this so i'm gonna get it taken down, my dad owns microsoft he can do that"
]

# bad but i just don't care :)
total_comments = 0

def rand_pick(count, l, exclude=None):
    cpy = [e for e in l]
    excluded_count = 0
    if exclude != None:
        excluded_count = 1
    if (count - excluded_count) == len(cpy):
        return cpy
    if (count - excluded_count) > len(cpy):
        raise Exception(f"Requested count ({count - excluded_count}) exceeds length of provided list ({len(cpy)})")
    result = []
    while len(result) != count:
        i = randint(0,len(cpy)-1)
        if cpy[i] == exclude:
            continue
        result.append(cpy[i])
        del cpy[i]
    return result

def clear_db(c):
    c.execute('DROP TABLE IF EXISTS USERS')
    c.execute('DROP TABLE IF EXISTS POSTS')
    c.execute('DROP TABLE IF EXISTS COMMENTS')

def create_tables(c):
    c.execute('CREATE TABLE USERS(\
        id INTEGER PRIMARY KEY,\
        username text,\
        name text,\
        password text,\
        email text,\
        curr_token text,\
        following text,\
        followed_num integer default 0\
    )')

    c.execute('CREATE TABLE POSTS(\
        id INTEGER PRIMARY KEY,\
        author TEXT,\
        title TEXT,\
        description TEXT,\
        published TEXT,\
        likes TEXT,\
        thumbnail TEXT,\
        src TEXT,\
        comments TEXT,\
        tag TEXT\
    )')

    c.execute('CREATE TABLE COMMENTS(\
        id INTEGER PRIMARY KEY,\
        author TEXT,\
        published TEXT,\
        comment TEXT\
    )')

def gen_users(c):
    with open(os.path.join('users.csv')) as f:
        lines = [l.strip().split(',') for l in f.readlines()]
    # ignore header + Anon
    lines = lines[2:]
    users = {}
    all_ids = list(range(0, len(lines)))
    for id, pair in enumerate(lines):
        users[id] = {
            'username': pair[0].strip(),
            'password': pair[1].strip(),
            'following': [],
            'followed': 0
        }
    for id in range(len(lines)):
        for friend in rand_pick(randint(1,35), all_ids, exclude=id):
            users[id]['following'].append(friend)
            users[friend]['followed'] += 1
    for id in users.keys():
        user = users[id]
        un = user['username']
        n = user['username']
        e = f"{user['username']}@unsw.edu.au"
        pw = user['password']
        f = ','.join([str(x) for x in user['following']])
        fc = user['followed']
        c.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?)", (id+2,un,n,pw,e,'',f,fc))
    return users

# returns some random description
def gen_desc_text():
    return desc[randint(0,len(desc)-1)]

# returns some random comment
def gen_comment_text():
    return comment_store[randint(0,len(comment_store)-1)]

# returns image, thumbnail, tag
def rand_img():
    tag = choice(['mountains', 'shower-thoughts', 'ocean'])
    url = f"https://loremflickr.com/800/800/{tag}"
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception(f'Failed on {url}')
    img = base64.b64encode(r.content).decode("utf-8")
    size = (150,150)
    im = Image.open(BytesIO(r.content))
    im.thumbnail(size, Image.ANTIALIAS)
    buffered = BytesIO()
    im.save(buffered, format='PNG')
    thumbnail = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return (img,thumbnail,tag)

def gen_comment(users, post_time, c):
    global total_comments
    author_id = list(users.keys())[randint(0,len(users.keys())-1)]
    values = (
        total_comments,
        users[author_id]['username'],
        str(randint(post_time+5, 1563540878)),
        gen_comment_text()
    )
    c.execute("INSERT INTO COMMENTS VALUES(?,?,?,?)", values)
    total_comments += 1
    return total_comments-1


def gen_posts(count, users, c):
    for _ in tqdm(range(count)):
        if randint(1,2) == 1:
            [img, tn, tag] = rand_img()
        else:
            [img, tn, tag] = [None, None, 'shower-thoughts']
        post_time = randint(1550580917,1563540878)
        author_id = list(users.keys())[randint(0,len(users.keys())-1)]
        desc = gen_desc_text()
        title = " ".join(desc.split(" ")[:2])
        values = (
            _,
            users[author_id]['username'],
            title,
            desc,
            str(post_time),
            ','.join([str(x) for x in rand_pick(randint(0,20), users.keys())]),
            tn,
            img,
            ','.join([str(gen_comment(users, post_time, c)) for _ in range(randint(0,10))]),
            tag
        )
        c.execute("INSERT INTO POSTS VALUES (?,?,?,?,?,?,?,?,?,?)",values)

def gen_db():
    # connect
    conn = sqlite3.connect(os.path.join('test.sqlite3'))
    c = conn.cursor()

    clear_db(c)
    create_tables(c)

    # Create anon user
    c.execute('INSERT INTO USERS VALUES(1,"Anon","Anon","password","Anon@unsw.edu.au","","",0)')
    # create rest
    users = gen_users(c)

    gen_posts(200, users, c)

    # clean up
    conn.commit()
    c.close()
    conn.close()


if __name__ == "__main__":
    gen_db()