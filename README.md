# Reddit_bots

Scrape Google News using search terms, post to Reddit using googlenews.py. 

Search subreddits using search terms, crosspost submissions to a subreddit using search.py. 

Mirror a subreddit by crossposting submissions to another subreddit using cities.py.

To obtain Reddit App credentials, log in to reddit with your username/password. Go to "Settings": "Safety and Privacy".  Scroll to bottom. Click on "Manage third-party app authorization".  "Create an app". Name the app (any name). Select "Script".  Write a description if you wish. In "Redirect uri", type: "http://localhost:8080". Click on the I'm not a robot captcha, when complete, click on "create an app".  Copy the Client ID and the Secret ID and save them for future use.

Review the scripts and replace any items in "< >" with text appropriate to your device and destination subreddit.

You should start a subreddit to use these scripts with you as moderator.

Change the search terms to those which you would prefer.  Change the blocked strings to things you do not want to see in your feed.

Check the time zone adjustment, the current adjustment is for US Eastern Time, - 4 hours (in seconds). Some scripts may not require adjustment.

Run the scripts daily, or hourly using cron and the .sh files.

Before running cron, run in terminal with the crosspost or submit line disabled by commenting it out.  You may then fine tune your search terms and blocked strings. When you are satisfied with the result, uncomment the submit or crosspost line, and run with cron.



