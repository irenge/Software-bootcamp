import spacy
gardenpathSentences = [u"One of the Saying is Mary gave the child the dog bit a Band-Aid.", u"The man who whistles tunes pianos: 1999.", u"Until the police arrest the drug dealers control the street", u"The man who hunts ducks out on weekends", u"Best UK movies Cannes Film Festival in 2022", u"The old man the boat. ", u"USA, DR Congo, UK, Nigeria, South Africa, Russia, Ukraine", "The Prime Minister of Scotland,Mrs Nicolas Surgeon resigned from her office today at 12PM" ]
nlp = spacy.load('en_core_web_sm')
print (gardenpathSentences)
docs = [ nlp(doc) for doc in gardenpathSentences]
print(docs)
# tokenise and entity recognition
for doc in docs:
     print([token.orth_ for token in doc if not token.is_punct | token.is_space], end = "\t")
     print([(i, i.label_, i.label) for i in doc.ents])

print(spacy.explain("GPE")) # Countries, cities, states, (UK, 'GPE', 384) , This make completely sense as UK is a country
print(spacy.explain("PERSON")) # People, including fictional ,  (Mrs Nicolas Surgeon, 'PERSON', 380) , it makes sense as it is associated with the Mrs Nicolas Surgeon who is a person though not fictional


