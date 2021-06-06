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

def clean(text):
    return ''.join(word.strip(string.punctuation) for word in text).replace("\n", "").lower()