import json
import os
import re
from util import deEmojify,clean

def get_files():
    paths = []
    for root, dirs, files in os.walk("messages/inbox"):
        for name in files:
            if name.endswith((".json")):
                full_path = os.path.join(root, name)
                paths.append(full_path)
    print(paths)
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
        data.append(chat)
    return data
