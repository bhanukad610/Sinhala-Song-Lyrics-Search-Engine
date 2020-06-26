import json
import requests

def search_by_term(term):
        URL = "http://localhost:9200/songs/_search"
        query = {
                "query":{
                    "query_string":{
                        "query": term
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

            return response_body

        except:
            print("Error")

# search_by_term("ලතාවේ")