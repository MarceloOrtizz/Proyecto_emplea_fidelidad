import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def analyze_ngrams(df: pd.DataFrame, 
                   name_column_text: str, 
                   name_column_target : str, 
                   top_n=10, 
                   ngram_range=(2, 3)) -> None:
    """This function is used to analyze the n-grams of the text
    Args:
        df (pd.DataFrame): DataFrame with the text to analyze
        ngram_range (tuple, optional): Range of n-grams to analyze. Defaults to (2, 3).
        top_n (int, optional): Number of n-grams to return. Defaults to 10.
    Returns:
        None"""
    unique_categories = df[name_column_target].unique()[:10]

    for category in unique_categories:
        filtered_text = df[df[name_column_target] == category][name_column_text]
        filtered_text = filtered_text.astype(str)  # Asegúrate de que el texto esté en formato string
        
        # crear un objeto CountVectorizer para n-gramas
        vectorizer = CountVectorizer(ngram_range=ngram_range)
        X = vectorizer.fit_transform(filtered_text)
        
        # obtener los n-gramas y su frecuencia
        ngram_freq = list(zip(vectorizer.get_feature_names_out(), X.sum(axis=0).tolist()[0]))
        ngram_freq = sorted(ngram_freq, key=lambda x: x[1], reverse=True)[:top_n]
    
        print(f"Top {top_n} n-grams for category '{category}':")
        for ngram, freq in ngram_freq:
            print(f"{ngram}: {freq} times")
        print("\n")