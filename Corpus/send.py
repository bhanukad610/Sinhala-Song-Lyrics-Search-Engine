import urllib2
import json
import pandas as pd


df = pd.read_csv('sinhala_songs_corpus_final.csv')
URL = "http://54.172.47.106:9200/songs/song/"

check = []

for i in range(len(df['Artist'])):
        title = df['title-en'][i]

        if title not in check:
                check.append(title)

                song_obj = {
                        "Artist" :df['Artist'][i],
                        "Lyrics" : df['Lyrics'][i],
                        "Key" : df['Key'][i],
                        "Genre" : df['Genre'][i],
                        "Music" : df['Music'][i],
                        "Song" : df['Song'][i],
                        "Visits" : df['Visits'][i],
                        "Title" : df['Title'][i],
                        "Title-english" : df['title-en'][i]
                }


                try:
                        req = urllib2.Request(URL)
                        req.add_header('Content-Type', 'application/json')
                        response = urllib2.urlopen(req, json.dumps(song_obj))
                except:
                        print("Error")
