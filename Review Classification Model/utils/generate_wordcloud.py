import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(
    df: pd.DataFrame, 
    name_column_text: str
):
    """This function is used to generate the wordclouds of the text"""
    filtered_text = ' '.join(df[name_column_text].to_list())
    print(f" unique tokens for class: {len(set(filtered_text.split()))}")
    if filtered_text:
        wordcloud = WordCloud(width=800, height=600, background_color='white',
                              colormap='viridis', max_words=150, contour_color='steelblue',
                              contour_width=2, prefer_horizontal=0.8).generate(filtered_text)
        plt.figure(figsize=(8, 8))  # Tamaño de la figura para mejorar la resolución
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f"Word Cloud")
        plt.show()