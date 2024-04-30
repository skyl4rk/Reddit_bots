import feedparser
from datetime import datetime#, timezone
import time
import praw

search_term = ["michigan", "ann%20arbor","battle%20creek","benton%20harbor","dearborn","detroit","ferndale","flint","grand%20rapids","hamtramck","kalamazoo","lansing","livonia","manistee","muskegon","okemos","pentwater","petoskey","port%20huron","royal%20oak","saginaw","south%20haven","st%20joseph","traverse%20city","upper%20peninsula","ypsilanti"]

blocked_strings = ["sports", "track and field", "obituary", "mhoops", "fury", "lugnuts", "athlete", "baseball", "basketball", "softball", "rise","saginaw spirit", "hockey", "cornerback", "lions", "tigers", "lineman", "lineback", "coach", "maize", "harbaugh", "udfa", "free agent", "draft", "nfl", "athletics", "football", "ufl", "pistons", "nba"]

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
dupes = open(r"/path/to/dupes.txt","w+")
dupes.close()

subreddit = r.subreddit("<destination_subreddit>")

request_time = (int(time.time()))
begin_timeframe = request_time - 3600 #
blocked = 0
search_index = 0
while search_index < len(search_term):
    print(search_term[search_index])
    rss_url = f'https://news.google.com/rss/search?q={search_term[search_index]}&hl=en-US&gl=US&ceid=US%3Aen'
    feed = feedparser.parse(rss_url)
        
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        description = entry.description
        pubdate = entry.published
        source = entry.source
        pubdate_tsp = int(datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z").timestamp())
        pubdate_gmt = pubdate_tsp - 14400
#        print(pubdate)
        
        if pubdate_gmt > begin_timeframe:
            index = 0
            blocked = 0
            title_lower = title.lower()

            while index < len(blocked_strings):
                if blocked_strings[index] in title_lower:
                    blocked = blocked + 1
                index += 1
            if blocked == 0:
                with open(r"/path/to/dupes.txt") as f:
                    if not title in f.read():
                        print(pubdate)
                        print(title)
                        subreddit.submit(title, url=link)
                        print("Posted")
                        dupes = open(r"/path/to/dupes.txt","a")
                        dupes.write(title)
                        dupes.write("\n")
                        dupes.close()
                        time.sleep(1)
                index += 1
                blocked = 0
            else:
                print(title)
                print("Blocked")
                blocked = 0
    else:
        print(f"Ending search of {search_term[search_index]}")
    search_index += 1