import nltk
import spacy
import itertools
import collections
from itertools import dropwhile
import config
from read_faceboo import read_facebook_data
from deep_translator import PonsTranslator, exceptions

WORD_FREQUENCY_LIMIT = 75


def get_most_common_words(data):
    my_most_common = [item[0] for item in (collections.Counter(data.most_common()[:100]))]
    return my_most_common


def calculate_word_commonality(common_words):
    my_most_common  = get_most_common_words(common_words)[:100]
    res = len(set(my_most_common) & set(config.WIKI_WORDS)) / float(len(set(my_most_common) | set(config.WIKI_WORDS))) * 100
    print(f"Your word commonality to the world is {round(res)}%")

def cleanse_lemma(chat_messages):
    lemma = nltk.wordnet.WordNetLemmatizer()
    lementised = ""
    for token in chat_messages:
        if len(token) > 1 or token not in ['v']:
            lementised = lementised + " " + (lemma.lemmatize(token))
    return lementised


def get_count(data):
    """
    This is *THE* critical method to the project.
    Basically, 
    :param data:
    :return:
    """
    sentences = [line.strip().split(" ") for line in list(itertools.chain.from_iterable(data))]
    words = list(itertools.chain.from_iterable(sentences))
    counts = collections.Counter(words)

    for key, count in dropwhile(lambda key_count: key_count[1] >= WORD_FREQUENCY_LIMIT, counts.most_common()):
        del counts[key]
    if(config.MOST_COMMON):

        print("--MOST COMMON Words and translations--")
        x = 1
        for item in counts.most_common(100):
            try:
                print(f"{x}: EN {item[0]} JP : {PonsTranslator(source='english', target='japanese').translate(item[0], return_all=True)[:3]} frequency : {item[1]}")
            except:
                print(f"{x}: EN {item[0]}  frequency : {item[1]}")
            x += 1



    calculate_word_commonality(counts)
    return (counts)


def get_verbs_and_nouns(doc, words):
    noun_phrases = list(set([chunk.text for chunk in doc.noun_chunks if " " in chunk.text]))

    print("--Noun Phrases--")
    print(f" {noun_phrases}")

    verbs = list(set([token.lemma_ for token in doc if token.pos_ == "VERB" and (len(token.lemma_) > 3)]))

    # Remove all words, that aren't verbs, return the most common verbs used.
    most_common_verbs = {k: words[k] for k in verbs}
    ordered_verbs = {k: v for k, v in sorted(most_common_verbs.items(), key=lambda item: item[1], reverse=True)}

    print("--VERBS--")
    for item in ordered_verbs:
        try:
            print(f"EN {item} PT : {PonsTranslator(source='english', target='portuguese').translate(item, return_all=True)[:3]} frequency : {ordered_verbs[item]}")
        except exceptions.TranslationNotFound:
            print(f"EN {item} PT: No Translation Found! frequency : {ordered_verbs[item]}")

if __name__ == "__main__":
    print("Started reading data.\n processing....")
    data = read_facebook_data()
    words = get_count(data)
    all_lemma = cleanse_lemma(words.keys())
    nlp = spacy.load("en_core_web_trf")
    doc = nlp(all_lemma)

    if(config.NOUN_ANALYSIS and config.VERB_ANALYSIS):
        get_verbs_and_nouns(doc, words)
