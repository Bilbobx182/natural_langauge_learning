import praw
import os
try:
    SECRET_KEY = 'iib1qXPAxmxdQ19PNaz9gYpc7E4'
    CLIENT_KEY = 'J9ktfMVd_jn1qQ'
    reddit = praw.Reddit(
        client_id=CLIENT_KEY,
        client_secret=SECRET_KEY,
        password="123wweme",
        user_agent="Test",
        username="eternal_atom",
    )
    print(reddit.user.me())

except Exception as e:
    print(e)

reddit.subreddit.