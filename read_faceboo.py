import glob
import json
import os
import multiprocessing
import time
import re
import string
def deEmojify(text):
    """
    https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python

    :param text:
    :return:
    """
    regrex_pattern = re.compile(pattern="["
                                        u"\U0001F600-\U0001F64F"  # emoticons
                                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                        "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)

def get_files():
    paths = []
    for root, dirs, files in os.walk("messages/inbox"):
        for name in files:
            if name.endswith((".json")):
                full_path = os.path.join(root, name)
                paths.append(full_path)
    return paths

def read_facebook_data():
    filedata = {filename: json.loads(''.join(open(filename, 'r').readlines())) for filename in get_files()}
    filedata.keys()

    mychat = []
    for chat in  filedata.keys():
        try:
            for message in filedata[chat]['messages']:
                if 'Ciar' in message['sender_name']:
                    cleansed = re.sub(r'[^\w\s]','',message['content'].lower().replace("\n",""))
                    print(deEmojify(cleansed))
        except:
            continue

if __name__ == "__main__":
    read_facebook_data()