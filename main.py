import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article


nltk.download('punkt')


url = 'https://www.benzinga.com/news/21/01/19109942/elon-musk-teases-tesla-ai-day'

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')

analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

root = tk.Tk()
