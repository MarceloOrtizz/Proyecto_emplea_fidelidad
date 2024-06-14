import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

def tokenize(text: str):
    """This method is used to tokenize the text"""
    tokens = word_tokenize(text.lower(), language='spanish')
    return tokens