#works for python 3+
import googletrans
from googletrans import Translator
import json
import csv
import pandas as pd

translator = Translator()

df = pd.read_csv('songs_corpus_with_english_1.csv')

df_title = []
for title in df['Title']:
    df_title.append(title.replace("-", " "))
df['Title'] = df_title

cols_to_trans = ['Artist','Lyrics', 'Genre', 'Music', 'Title']
for col in cols_to_trans:
    temp = []
    print(col)
    for i in df[col]:
        translated = translator.translate(i, dest='sinhala').text
        while(1):
            if(i == translated):
                print(i, translated)
                translated = translator.translate(i, dest='sinhala').text
                print("translated again")
                print(i, translated)
            else:
                break
        temp.append(translated)
    df[col] = temp
print(df.head())

df.to_csv('sinhala_songs_corpus.csv')