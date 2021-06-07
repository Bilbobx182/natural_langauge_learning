import json
import os
import re
from util import deEmojify, clean
import numpy as np

def get_files():
    paths = []
    for root, dirs, files in os.walk("messages/inbox"):
        for name in files:
            if name.endswith((".json")):
                full_path = os.path.join(root, name)
                paths.append(full_path)
    return paths


def read_facebook_data():
    data = []
    for file in get_files():
        chat = []
        with open(file) as f:
            d = json.load(f)
            for message in d['messages']:
                if "Ciar" in message['sender_name'] and 'content' in message:
                    chat.append(clean(message['content']))

                    # We chunk the data like this so we can process the data
                    if len(chat) > 50:
                        data.append(chat)
                        chat = []
        data.append(chat)
    return data
