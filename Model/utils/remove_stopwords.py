import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def remove_stopwords(string, stopwords = stopwords):
    return ' '.join(
        [
            match.group(0) for match in re.compile('[A-zÀ-ú]+').
            finditer(string.lower())
            if match.group(0) not in stopwords.words('spanish')
        ]
    )