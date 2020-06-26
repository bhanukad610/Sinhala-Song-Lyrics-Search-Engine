import requests 
from bs4 import BeautifulSoup 
import csv
import json
import unicodedata
import re 

title1 = u'adara-gangulehi'
title2 = u'yawwana-uyane'

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
    # print(con0.text)
    key = con0.text.split(':')
    

    key_fin = ""
    if len(key) > 1:
        key_fin = key[1]
    else:
        key_fin = key[0]
    print(key_fin)
    con1 = soup_song.find('div', class_ = "su-column su-column-size-3-6")
    artist = (con1.find('span', class_="entry-categories").text).split(':')[1]

    try:
        visits = (soup_song.find('div', class_="tptn_counter").text)
        visits_num = ""
        for i in visits:
            if(i.isnumeric()):
                visits_num += i
        visits_num = int(visits_num)
    except:
        print("Error in visits")
    
    genre = "No"
    try:
        genre = (con1.find("span", class_= "entry-tags").text).split(':')[1]
    except:
        genre = "No"

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
                gutar += line_striped + " "
        else:
            if(len(line_striped) > 0):
                lyrics += line_striped + " "

    song_obj = {
        "Artist" : (re.sub(' +', ' ', unicodedata.normalize('NFKD', artist).encode('ascii', 'ignore'))).strip(),
        "Lyrics" : (re.sub(' +', ' ', unicodedata.normalize('NFKD', lyrics_artist).encode('ascii', 'ignore'))).strip(),
        "Key" : (re.sub(' +', ' ', key_fin.encode("utf-8"))).strip(),
        "Genre" : (re.sub(' +', ' ', genre.encode("utf-8"))).strip(),
        "Music" : (re.sub(' +', ' ', unicodedata.normalize('NFKD', music).encode('ascii', 'ignore'))).strip(),
        "Song" : (re.sub(' +', ' ', lyrics.encode("utf-8"))).strip(),
        "Guitar" : (re.sub(' +', ' ', unicodedata.normalize('NFKD', gutar).encode('ascii', 'ignore'))).strip(),
        "Title" : (re.sub(' +', ' ', title_en).strip()),
        "Visits" : visits_num
    }

    return song_obj

# get_song_obj(title2)
# print(get_song_obj(title))