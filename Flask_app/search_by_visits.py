import json
import requests

def search_by_visits(visits, host):
        gte = None
        lte = None

        if len(visits) == 1:
            gte = int(visits[0])
        else:
            gte = int(visits[0])
            lte = int(visits[1])
 
        URL = "http://" + str(host) + ":9200/songs/_search"
        query = {
                "size" : 10,
                "query": {
                        "range": {
                        "Visits": {
                            "gte": gte,
                            "lte": lte
                        }
                        }
                },
                "aggs" : {
                    "Title filter" : {
                        "terms" : { 
                        "field" : "Title.keyword",
                        "size": 5
                        } 
                    },
                    "Artist filter" : {
                        "terms" : { 
                        "field" : "Artist.keyword",
                        "size": 5
                        
                        } 
                    },
                    "Lyrics filter" : {
                        "terms" : { 
                        "field" : "Lyrics.keyword",
                        "size": 5
                        
                        } 
                    },
                    "Genre filter" : {
                        "terms" : { 
                        "field" : "Genre.keyword",
                        "size": 5
                        } 
                    },
                    "Music filter" : {
                        "terms" : { 
                        "field" : "Artist.keyword",
                        "size": 5
                        
                        } 
                    }
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

            
            facets = res['aggregations']
            
            response_body = {
                "results" : songs,
                "facets" : {
                    "Title filter" : facets['Title filter']['buckets'],
                    "Genre filter" : facets['Genre filter']['buckets'],
                    "Artist filter" : facets['Artist filter']['buckets'],
                    "Lyrics filter" : facets['Lyrics filter']['buckets'],
                    "Music filter" : facets['Music filter']['buckets'],
                }      
            }
            print(query)
            return response_body

        except:
            print("Error")