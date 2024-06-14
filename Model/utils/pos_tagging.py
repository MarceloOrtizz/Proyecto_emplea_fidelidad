import spacy
from spacy.lang.es.examples import sentences 

nlp = spacy.load("es_core_news_sm")

def pos_tagging(tokens: list):
 return [w.text for w in  nlp(' '.join(tokens)) if w.pos_ in ['NOUN', 'ADJ', 'VERB']]