import requests 
from bs4 import BeautifulSoup 
import csv
import json
import unicodedata
import re 

title = u'mage hitha piree \u2013 \u0db8\u0d9c\u0dd9 \u0dc4\u0dd2\u0dad \u0db4\u0dd2\u0dbb\u0dd3'

def isEnglish(s):
    return re.search('[a-zA-Z]', s)

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def get_song_obj(title):
    title_en = title.encode('ascii',errors='ignore')
    title_en = title_en.rstrip()
    title_en = title_en.replace(" ", "-")
    URL_for_song = "https://sinhalasongbook.com/" + title_en
    r_song = requests.get(URL_for_song) 
    soup_song = BeautifulSoup(r_song.content, 'lxml')

    con0 = soup_song.find('h3')
    key = con0.text.split(':')

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

    con1 = soup_song.find('div', class_ = "su-column su-column-size-3-6")
    artist = (con1.find('span', class_="entry-categories").text).split(':')[1]
    genre = (con1.find("span", class_= "entry-tags").text).split(':')[1]

    con2 = soup_song.find('div', class_ = "su-column su-column-size-2-6")
    lyrics_artist = (con2.find('span', class_="lyrics").text).split(':')[1]
    music = (con2.find("span", class_= "music").text).split(':')[1]

    lyrics = ""
    gutar = ""

    con3 = (soup_song.find("pre")).text.splitlines()
    for line in con3:
        line_striped = (re.sub(' +', ' ', line)).strip()
        if(isEnglish(line_striped) or ("|"  in line_striped)):
            if(len(line_striped) > 0):
                # print(line_striped)
                gutar += line_striped + " "
        else:
            if(len(line_striped) > 0):
                lyrics += line_striped + " "

    song_obj = {
        "Artist" : (re.sub(' +', ' ', unicodedata.normalize('NFKD', artist).encode('ascii', 'ignore'))).strip(),
        "Lyrics" : (re.sub(' +', ' ', unicodedata.normalize('NFKD', lyrics_artist).encode('ascii', 'ignore'))).strip(),
        "Key" : (re.sub(' +', ' ', key[1].encode("utf-8"))).strip(),
        "Genre" : (re.sub(' +', ' ', unicodedata.normalize('NFKD', genre).encode('ascii', 'ignore'))).strip(),
        "Music" : (re.sub(' +', ' ', unicodedata.normalize('NFKD', music).encode('ascii', 'ignore'))).strip(),
        "Song" : (re.sub(' +', ' ', lyrics.encode("utf-8"))).strip(),
        "Guitar" : (re.sub(' +', ' ', unicodedata.normalize('NFKD', gutar).encode('ascii', 'ignore'))).strip(),
        "Title" : (re.sub(' +', ' ', sin_title).strip())
    }

    return song_obj

# get_song_obj(title)
print(get_song_obj(title))