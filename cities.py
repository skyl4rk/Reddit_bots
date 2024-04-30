import praw
from datetime import datetime,timezone
import time

username="<authentication info removed>" # Reddit username
password="<authentication info removed>" # Reddit password
client_id="<authentication info removed>" # Reddit App Client ID
client_secret="<authentication info removed>" # Reddit App Secret ID

reddit_instance = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent="test_bot"
    )

def city_crosspost(city):
    bot_time = datetime.now(timezone.utc).timestamp()
    try:
        subreddit = reddit_instance.subreddit(city)
        new_submissions = subreddit.new(limit=20)
        print("________________________")
        print(city)
        for submission in new_submissions:
            print(submission.title)
            post_created = submission.created_utc
            if bot_time - post_created < 3600:
                print('crosspost this post')
                submission.crosspost('<destination_subreddit>', send_replies=False)
                print(' - success')
        time.sleep(3)
    except:
        print(city + "was not processed correctly")
        
cities = ["michigan","annarbor","battlecreek","baycitymichigan","bentonharbor","bigrapids","dearborn","detroit","downriver","ferndale","flint","grandrapids","greatlakes","grossepointe","hamtramck","harborsprings","hollandmichigan","huroncounty","imlaycity","jacksonmi","kzoo","lakemichigan","lansing","livingstoncountymich","livonia","manistee","metrodetroit","michigan_politics","midland","mlive","monroemi","muskegon","newaygocounty","nwmi","okemos","pentwater","petoskey","plymouthmi","porthuron","royaloak","saginaw","southhaven","st_joseph","thethumb","traversecity","upperpeninsula","washtenawcountymi","yooper","ypsi"]

for x in cities:
    city_crosspost(x)
    
