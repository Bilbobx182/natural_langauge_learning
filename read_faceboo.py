import os
import json
from nltk.sentiment import SentimentIntensityAnalyzer
from util import clean
import config

def get_files():
    """
    Gets a list of paths in the messages folder.
    :return:
    """
    paths = []
    for root, dirs, files in os.walk("messages/inbox"):
        for name in files:
            if name.endswith((".json")):
                full_path = os.path.join(root, name)
                paths.append(full_path)
    return paths


def read_facebook_data():
    """
    Read the json data.
    Clean it.
    Return the data.
    """
    data = []
    my_messages = ""
    for file in get_files():
        chat = []
        with open(file) as f:
            d = json.load(f)
            for message in d['messages']:
                if "Ciar" in message['sender_name'] and 'content' in message:
                    my_messages += message['content']
                    if 'http' not in message['content']:
                        cleansed = clean(message['content'])
                        if cleansed.isascii():
                            chat.append(cleansed)

        if(config.CHECK_SENTIMENT):
            print(f"Sentiment Analysis chat {file.split('messages/inbox/')[1]}")
            print("-------------------")
            sia = SentimentIntensityAnalyzer()
            print(sia.polarity_scores(my_messages))
            my_messages = ""
        data.append(chat)
    return data
