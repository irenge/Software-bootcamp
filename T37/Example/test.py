import spacy
nlp = spacy.load('en_core_web_sm')

garden = u"Mary gave the child the dog bit a Band-Aid. I told the girl the cat scratched Bill would help her. The man who whistles tunes pianos. Until the police arrest the drug dealers control the street. The man who hunts ducks out on weekends"

doc = nlp(garden)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
