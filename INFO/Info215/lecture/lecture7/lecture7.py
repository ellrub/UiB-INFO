import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp('Apple is looking at buying U.K startup for $1 billion')

# 2 for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)

for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children])

spacy.displacy.render(doc, style='ent', jupyter=True)
# 1 print(doc[0].text)
# 1 print(doc[1].text)