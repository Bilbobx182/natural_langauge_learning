import nltk
import spacy
import itertools
import collections
from itertools import dropwhile
import config
from read_faceboo import read_facebook_data

WORD_FREQUENCY_LIMIT = 50


def cleanse_lemma(chat_messages):
    print("--Processing--")
    lemma = nltk.wordnet.WordNetLemmatizer()
    lementised = ""
    for token in chat_messages:
        if len(token) > 1 or token not in ['v']:
            lementised = lementised + " " + (lemma.lemmatize(token))
    return lementised


def get_count(data):
    sentences = [line.strip().split(" ") for line in list(itertools.chain.from_iterable(data))]
    words = list(itertools.chain.from_iterable(sentences))
    counts = collections.Counter(words)

    for key, count in dropwhile(lambda key_count: key_count[1] >= WORD_FREQUENCY_LIMIT, counts.most_common()):
        del counts[key]
    if(config.MOST_COMMON):
        print(counts)
    return (counts)


def get_verbs_and_nouns(doc, words):
    noun_phrases = list(set([chunk.text for chunk in doc.noun_chunks if " " in chunk.text]))
    print(f"Noun Phrases : {noun_phrases}")


    verbs = list(set([token.lemma_ for token in doc if token.pos_ == "VERB" and (len(token.lemma_) > 3)]))

    # Remove all words, that aren't verbs, return the most common verbs used.
    most_common_verbs = {k: words[k] for k in verbs}
    ordered_verbs = {k: v for k, v in sorted(most_common_verbs.items(), key=lambda item: item[1], reverse=True)}

    for item in ordered_verbs:
        print(f'{item} : {ordered_verbs[item]}')


if __name__ == "__main__":
    data = read_facebook_data()
    words = get_count(data)
    all_lemma = cleanse_lemma(words.keys())
    nlp = spacy.load("en_core_web_trf")
    doc = nlp(all_lemma)

    if(config.NOUN_ANALYSIS and config.VERB_ANALYSIS):
        get_verbs_and_nouns(doc, words)
