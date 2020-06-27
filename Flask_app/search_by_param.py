import json
import requests

def search_by_param(parameter, term):
        URL = "http://localhost:9200/songs/_search"
        query = {
                "query": {
                    "match": {
                    parameter: term}
                    }
                }


        try:
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            response = (requests.post(URL, data = json.dumps(query), headers = headers)).text

            res = json.loads(response)
            hits = res['hits']['hits']
            songs = []

            for song in hits:
                songs.append(song['_source'])

            
            response_body = {
                "hits" : len(songs),
                "results" : songs
            }
            return response_body

        except:
            print("Error")

# search_by_param("වික්ටර් රත්නායක", "Artist")