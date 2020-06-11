import urllib2
import json

# Opening JSON file 
f = open('song_lyrics.json',) 

# returns JSON object as 
# a dictionary 
data = json.load(f)
URL = "http://localhost:9200/songs/song/"

for song in data:
    try:    
            req = urllib2.Request(URL)
            req.add_header('Content-Type', 'application/json')
            response = urllib2.urlopen(req, json.dumps(song))
    except:
            print("Error")

# Closing file 
f.close()
