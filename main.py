from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing.context import Process

import multiprocessing as mp
import spacy
from collections import Counter
from const import MOST_COMMON
from multiprocessing import Pool
from read_faceboo import read_facebook_data
from whatsapp import load_whatsapp_data
from datetime import datetime
import collections
import itertools
import nltk

def cleanse_lemma(chat_messages):
    print("--Processing--")
    # nlp = spacy.load("en_core_web_trf")
    # doc = nlp(' '.join(chat_messages))
    lemma = nltk.wordnet.WordNetLemmatizer()
    ps = nltk.wordnet.WordNetLemmatizer()
    lementised = ""
    for token in chat_messages:
        if len(token) > 1 or token not in ['v']:
            lementised = lementised + " " + (lemma.lemmatize(token))
    return lementised


def get_count(data):
    sentences = [line.strip().split(" ") for line in  list(itertools.chain.from_iterable(data))]
    words = list(itertools.chain.from_iterable(sentences))
    counts = collections.Counter(words)
    print(counts)
    return(counts)


if __name__ == "__main__":
    print("start =", datetime.now())
    data = read_facebook_data()
    words = get_count(data)
    all_lemma = cleanse_lemma(words.keys())
    print(all_lemma)
    print("end =", datetime.now())




    # sys.stdout = open('DATA_OUTPUT.txt', 'w')
    # datetime object containing current date and time
    # sys.stdout.close()
