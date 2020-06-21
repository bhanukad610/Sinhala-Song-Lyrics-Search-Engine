#works for python 3+ and run in colab
#ascci errors will occur otherwise
import googletrans
from googletrans import Translator
import json
import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests 
import re 

translator = Translator()

df = pd.read_csv('sinhala_songs_corpus.csv')

temp_title = []
for title in df['Title']:
    title_en = title.replace(" ", "-")
    URL_for_song = "https://sinhalasongbook.com/" + title_en
    r_song = requests.get(URL_for_song) 
    soup_song = BeautifulSoup(r_song.content, 'lxml')
    title_sin = soup_song.find('h1', class_ = "entry-title")

    title_sin = str(title_sin.text).strip()
    title_sin = (re.sub(' +', ' ', title_sin)).strip()

    words = title_sin.split()

    sin_title = ""
    check = False

    for i in words:
        if(check):
            sin_title += i + " "
        if i == "–":
            check = True
    sin_title = sin_title.strip()
    temp_title.append(sin_title)
    print(sin_title)