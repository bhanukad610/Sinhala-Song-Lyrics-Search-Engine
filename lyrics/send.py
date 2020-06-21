import urllib2
import json
import pandas as pd


df = pd.read_csv('sinhala_songs_corpus.csv')
URL = "http://localhost:9200/songs/song/"


for i in range(len(df['Artist'])):
        song_obj = {
                "Artist" :df['Artist'][i],
                "Lyrics" : df['Lyrics'][i],
                "Key" : df['Key'][i],
                "Genre" : df['Genre'][i],
                "Music" : df['Music'][i],
                "Song" : df['Song'][i],
                "Guitar" : df['Guitar'][i],
                "Title" : df['Title'][i]
        }


        try:
                req = urllib2.Request(URL)
                req.add_header('Content-Type', 'application/json')
                response = urllib2.urlopen(req, json.dumps(song_obj))
        except:
                print("Error")
