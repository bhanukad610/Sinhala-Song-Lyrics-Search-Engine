import requests 
from bs4 import BeautifulSoup 
import csv
from scrap_song import get_song_obj 
import re

artists = [
    'Premakeerthi De Alwis',
    'Karunarathna Abeysekara',
    'Kumaradasa Saputhanthri',
    'Cyril A Seelawimala',
    'Rambukkana Siddhartha Thero',
    'M.S.Fernando',
    'Kularathna Ariyawansa',
    'Dharmasiri Gamage',
    'Dharmarathna Perera',
    'Saman C Weerasinghe',
    'Sunil Ariyarathna',
    'Clarence Wijewardena',
    'Bandara Wijethunga',
    'Somathilaka Jayamaha',
    'Mahagama Sekara',
    'Rathna Sri Wijesinge',
    'Rookantha Gunathilaka',
    'Sunil R Gamage',
    'Namal Udugama',
    'Lushan Bulathsinhala',
    'Ajantha Ranasinghe',
    'Nihal Gamhewa',
    'Bandula Nanayakkarawasam',
    'Upali Dhanawalawithana',
    'Somapala Leelananda',
    'Yamuna Malani Perera',
    'Sunil Sarath Perera',
    'Rohana Baddaga',
    'Hemasiri Halpita',
    'Mahinda Dissanayaka',
    'K.D.K.Dharmawardhana'
]

songs = []
count = 0



for artist in artists:
    artist_name = artist.lower()
    artist_name = artist_name.replace(" ", "-")
    print(artist_name)


    for page_number in range(13):
        URL_for_page = "https://sinhalasongbook.com/page/"+str(page_number)+"?lyrics="+artist_name
        r_artist_page = requests.get(URL_for_page)
        soup_artist_page = BeautifulSoup(r_artist_page.content, 'lxml')

        for song in soup_artist_page.find_all('article'):
            if len(song) > 2:
                song_name = song.a.text
                song_name = song_name.lower()
                
                try:
                    song_obj = get_song_obj(song_name)
                    songs.append(song_obj)
                    count += 1
                    print(song_name, count)
                except:
                    print(song_name, "Error!")

csv_columns = ['Artist','Lyrics','Key', 'Genre', 'Music', 'Song', 'Title', 'Guitar', 'Visits']
csv_file = "songs_corpus_with_english_final.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for song in songs:
            writer.writerow(song)
except IOError:
    print("I/O error")