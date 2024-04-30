import praw
from datetime import datetime,timezone
import time

username="<authentication info removed>" # Reddit username
password="<authentication info removed>" # Reddit password
client_id="<authentication info removed>" # Reddit App Client ID
client_secret="<authentication info removed>" # Reddit App Secret ID

r = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent="test_bot"
    )

def search_crosspost(sub, searchterm):
    bot_time = datetime.now(timezone.utc).timestamp()
    try:
        subreddit = r.subreddit(sub)
        for submission in r.subreddit(sub).search(searchterm):
            post_created = submission.created_utc
            if bot_time - post_created < 86400:
                print("________________________")
                print(sub + " - " + searchterm)
                print(submission.title)
                with open(r"/path/to/dupes.txt") as f:
                    if not submission.title in f.read():
                        print('crosspost this post')
                        submission.crosspost('<destination_subreddit>', send_replies=False)
                        print(' - success')
                        dupes = open(r"/path/to/dupes.txt","a")
                        dupes.write(submission.title)
                        dupes.write("\n")
                        dupes.close()
                        time.sleep(3)
    except:
        print(sub + " was not processed correctly")

dupes = open(r"/path/to/dupes.txt","w+")
dupes.close()

subs = ["politics","news","todayilearned","samegrassbutgreener","geography","askanamerican","publicfreakout","damnthatsinteresting","oldschoolcool","oddlysatisfying","funny","nottheonion","askreddit","interestingasfuck","pics"]
search_terms = ["michigan","ann arbor","battle creek","benton harbor","big rapids","dearborn","detroit","ferndale","flint","grand rapids","hamtramck","kalamazoo","lansing","livonia","manistee","marquette","midland","muskegon","okemos","pentwater","petoskey","port huron","royal oak","saginaw","south haven","st joseph","traverse city","upper peninsula","ypsilanti"]
for x in subs:
    for y in search_terms:
        print(x + " - " + y)
        search_crosspost(x,y)    