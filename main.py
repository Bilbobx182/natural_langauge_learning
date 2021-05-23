import spacy
from collections import Counter
import re
import string

# TODO LIST :
"""
- ASYNC the IO, make processing the file faster.
"""


class NLU():

    def deEmojify(self,text):
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

    def load_cleansed_data(self):
        """
        Clean up the data.txt
        - lower to standardise  what we have.
        - remove special characters
        :return: data.txt
        """
        with open('data.txt', 'r') as file:
            data = file.read()

        cleansed_emoji =  self.deEmojify(data)
        self.cleansed = ''.join(word.strip(string.punctuation) for word in cleansed_emoji).replace("\n", "")

    def get_lementised(self):
        """
        :param data.txt: str
        :return: lementised str
        """
        lementised = ""
        for token in self.doc:
            lementised = lementised + " " + (token.lemma_)
        self.cleansed = lementised
        # Re-set the document to the lementised data.txt.
        self.doc = self.nlp(self.cleansed)

    def get_most_common_words(self):
        return (Counter(self.cleansed.split()).most_common())[:100]

    def render_most_common(self, counter_data):
        x = 1
        for item in counter_data:
            print(f"{x}:{item[0]}")
            x += 1

    def get_verbs_and_nouns(self):
        print("Noun phrases:", [chunk.text for chunk in self.doc.noun_chunks if " " in chunk.text])
        print("Verbs:", [token.lemma_ for token in self.doc if token.pos_ == "VERB" and (len(token.lemma_) > 3)])

    def __init__(self):
        self.nlp = spacy.load("en_core_web_trf")
        # Set the document to our cleansed data.txt
        self.load_cleansed_data()
        self.doc = self.nlp(self.cleansed)
        # Get the lementised wording
        self.get_lementised()
        # Get the most common words
        self.render_most_common(self.get_most_common_words())
        # Get the verbs and nouns
        self.get_verbs_and_nouns()


nlu = NLU()
