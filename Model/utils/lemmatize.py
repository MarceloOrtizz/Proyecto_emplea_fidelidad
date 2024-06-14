from nltk.stem import SnowballStemmer

def lemmatize(tokens: list):
    """This method is used to lemmatize the text"""
    stemmer = SnowballStemmer('spanish')
    lemmatized_tokens = [stemmer.stem(word) for word in tokens]
    return lemmatized_tokens