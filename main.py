import spacy
from collections import Counter
from const import MOST_COMMON
from multiprocessing import Pool
from read_faceboo import read_facebook_data
from whatsapp import load_whatsapp_data


# TODO LIST :


class NLU():

    def get_lementised(self):
        """
        :param data.txt: str
        :return: lementised str
        """
        lementised = ""
        for token in self.doc:
            lementised = lementised + " " + (token.lemma_)
        self.lementised = lementised
        self.doc = self.nlp(lementised)

    def get_most_common_words(self, data):
        my_most_common = [item[0] for item in (Counter(data.split()).most_common())[:100]]
        self.all.append(' '.join(my_most_common))
        print(f"length of data is {len(data)}")
        return my_most_common

    def render_most_common(self, common_words):
        x = 1
        for item in common_words:
            print(f"{x}:{item}")
            x += 1
        res = len(set(common_words) & set(MOST_COMMON)) / float(len(set(common_words) | set(MOST_COMMON))) * 100
        print(f"Your word commonality to the world is {round(res)}%")

    def get_verbs_and_nouns(self):
        print("Noun phrases:", [chunk.text for chunk in self.doc.noun_chunks if " " in chunk.text])
        print("Verbs:", [token.lemma_ for token in self.doc if token.pos_ == "VERB" and (len(token.lemma_) > 3)])

    def process_data(self, data):
        print("Starting process")
        for chat in data:
            print("--------")
            self.doc = self.nlp(''.join(chat))
            # self.f_doc = self.nlp(read_facebook_data())

            # Get the lementised wording
            self.get_lementised()
            # Get the most common words
            self.render_most_common(self.get_most_common_words(''.join(chat)))
            # Get the verbs and nouns
            self.get_verbs_and_nouns()

        self.render_most_common(self.all)

    def __init__(self):
        self.nlp = spacy.load("en_core_web_trf")
        self.all = []
        # Set the document to our cleansed data.txt

        # wapp = load_whatsapp_data()
        self.data = read_facebook_data()


if __name__ == "__main__":
    nlu = NLU()
    nlu.process_data(nlu.data)
