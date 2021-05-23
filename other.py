# with open('whatsapp.txt', 'r') as file:
#     data.txt = lines = file.read().splitlines()

# Manually cleaning the data.txt
# for line in data.txt:
#     if("n: " in line and "<Media omitted>" not in line):
#         printable = line.split("n: ")[1]
#         if("http" not in printable):
#             print(printable)





# doc = nlp(data.txt)
# words = [token.text.lower()
#          for token in doc
#          if not token.is_stop and not token.is_punct]
#
# # noun tokens that arent stop words or punctuations
# nouns = [token.text.lower()
#          for token in doc
#          if (not token.is_stop and
#              not token.is_punct and
#              token.pos_ == "NOUN")]
#
# # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# # print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
#
#
# # five most common tokens
# print("----------")
# print("MOST COMMON")
# print("----------")
#
# word_freq = Counter(words)
# common_words = word_freq.most_common(100)
#
# print("----------")
# print("MOST NOUN")
# print("----------")
#
# noun_freq = Counter(nouns)
# common_nouns = noun_freq.most_common(100)
#
# print("----------")
# print("AI")
# print("----------")
#
# # Find named entities, phrases and concepts
# for entity in doc.ents:
#     print(entity.text, entity.label_)