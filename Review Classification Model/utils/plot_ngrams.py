import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

def plot_ngrams(df: pd.DataFrame, 
                name_column_text: str, 
                name_column_target: str, 
                ngram_range=(2, 3), 
                top_n=5) -> None:
    """This function is used to plot the n-grams of the text
    Args:
        df (pd.DataFrame): DataFrame with the text to analyze
        ngram_range (tuple, optional): Range of n-grams to analyze. Defaults to (2, 3).
        top_n (int, optional): Number of n-grams to return. Defaults to 10."""
    unique_categories = df[name_column_target].unique()[:8]

    fig, axs = plt.subplots(len(unique_categories), 2, figsize=(12, 2 * len(unique_categories)))

    for i, category in enumerate(unique_categories):
        filtered_text = df[df[name_column_target] == category][name_column_text]
        filtered_text = filtered_text.astype(str) 
        
        vectorizer = CountVectorizer(ngram_range=ngram_range)
        X = vectorizer.fit_transform(filtered_text)
        
        # Obtener los n-gramas y su frecuencia
        ngram_freq = list(zip(vectorizer.get_feature_names_out(), X.sum(axis=0).tolist()[0]))
        ngram_freq = sorted(ngram_freq, key=lambda x: x[1], reverse=True)
        
        bigrams = [ngram[0] for ngram in ngram_freq if len(ngram[0].split()) == 2][:top_n]
        bigram_frequencies = [ngram[1] for ngram in ngram_freq if len(ngram[0].split()) == 2][:top_n]
        
        trigrams = [ngram[0] for ngram in ngram_freq if len(ngram[0].split()) == 3][:top_n]
        trigram_frequencies = [ngram[1] for ngram in ngram_freq if len(ngram[0].split()) == 3][:top_n]

        if bigrams:
            axs[i, 0].barh(bigrams, bigram_frequencies, color='skyblue')
            axs[i, 0].set_xlabel('Frequency')
            axs[i, 0].set_title(f'Top {top_n} Bigrams:\n{category[:45]}...', fontsize=6)
            axs[i, 0].invert_yaxis()

            for j, freq in enumerate(bigram_frequencies):
                axs[i, 0].text(freq, j, str(freq), ha='left', va='center')

        if trigrams:
            axs[i, 1].barh(trigrams, trigram_frequencies, color='salmon')
            axs[i, 1].set_xlabel('Frequency')
            axs[i, 1].set_title(f'Top {top_n} Trigrams:\n{category[:45]}...', fontsize=6)
            axs[i, 1].invert_yaxis()

            for j, freq in enumerate(trigram_frequencies):
                axs[i, 1].text(freq, j, str(freq), ha='left', va='center')

    plt.subplots_adjust(hspace=0.5)
    plt.tight_layout()
    plt.show()