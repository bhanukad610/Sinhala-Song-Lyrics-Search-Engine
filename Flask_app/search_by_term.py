#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import json
import requests

artist_key_words = ['ගෙ', 'ගැයූ','ගයන', 'කියන', 'කියූ', 'ගායනා']
lyrics_key_words = ['ලියූ', 'ලියන', 'ලිව්ව', 'රචනා', 'රචිත', 'ලීව']
music_key_words = ['සංගීත']
genre_key_words = ['පොප්', 'ක්ලැසික්', 'දේවානුභාවයෙන්','පොප්ස්','ඩුවට්ස්','ක්ලැසික්','යුගල','ඕල්ඩීස්','කැලිප්සෝ','ළමා']

aggs =      {
                "Title filter": {
                "terms": {
                    "field": "Title.keyword",
                    "size": 5
                }
                },
                "Artist filter": {
                "terms": {
                    "field": "Artist.keyword",
                    "size": 5
                }
                },
                "Lyrics filter": {
                "terms": {
                    "field": "Lyrics.keyword",
                    "size": 5
                }
                },
                "Genre filter": {
                "terms": {
                    "field": "Genre.keyword",
                    "size": 5
                }
                },
                "Music filter": {
                "terms": {
                    "field": "Artist.keyword",
                    "size": 5
                }
                }
            }

def generate_query(term, size, sort):
    if(sort):
        query = {
                    "size" : size,
                    "sort": [{"Visits": {"order": "desc"}}],
                    "query":{
                        "query_string":{
                            "query": term
                        }
                    },
                    "aggs" : aggs
                    }
    else:
        query = {
                    "size" : size,
                    "query":{
                        "query_string":{
                            "query": term
                        }
                    },
                    "aggs" : aggs
                    }
    return query

def generate_query_with_keywords(mustObj, size, sort):

    if(sort):
        query =   {
            "sort": [{"Visits": {"order": "desc"}}],
            "size": size,
            "query": {
                "bool": {
                "must": [
                    {
                    "bool": {
                        "must": mustObj
                    }}]
                }
            },
            "aggs": aggs
            }
    else:
        query =   {
            "sort": [{"Visits": {"order": "desc"}}],
            "size": size,
            "query": {
                "bool": {
                "must": [
                    {
                    "bool": {
                        "must": mustObj
                    }}]
                }
            },
            "aggs": aggs
            }
    return query


def detect_keywords(term):
    mustobj = []
    words = term.split()

    for i in range (len(words)):
        word = words[i]
        if word  in artist_key_words:
            artist = words[i-2] + " "+ words[i-1]
            matchObjArtist = {"term" : {"Artist.keyword" : {"value" : artist}}}
            mustobj.append(matchObjArtist)

        if word  in lyrics_key_words:
            lyrics = words[i-2] + " "+ words[i-1]
            matchObjLyrics = {"term" : {"Lyrics.keyword" : {"value" : lyrics}}}
            mustobj.append(matchObjLyrics)
        
        if word  in music_key_words:
            music = words[i-2] + " "+ words[i-1]
            matchObjMusic = {"term" : {"Music.keyword" : {"value" : music}}}
            mustobj.append(matchObjMusic)

        if word  in genre_key_words:
            matchObjGenre = {"term" : {"Genre.keyword" : {"value" : word}}}
            mustobj.append(matchObjGenre)

    return mustobj

URL = "http://localhost:9200/songs/_search"

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def perfom_query(query, sort):
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            response = (requests.post(URL, data = json.dumps(query), headers = headers)).text
            res = json.loads(response)
            hits = res['hits']['hits']
            songs = []

            for song in hits:
                songs.append(song['_source'])

            
            facets = res['aggregations']
            
            if(sort): 
                response_body = {
                    "results" : songs
                }
            else:
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


def get_number(term):
    words = term.split()
    number = 0
    text = ""
    for i in words:
        if hasNumbers(i):
            number = int(i)
        else:
            text += i + " "
    return number, text

def search_by_term(term):
    words = term.split()

    if len(words) >= 5:
        mustObj = detect_keywords(term)
        if(len(mustObj) > 0):
            if(hasNumbers(term)):
                #search by keywords + sort N results + facets
                size, text = get_number(term)
                sort = True
                query = generate_query_with_keywords(mustObj, size, sort)
            else:
                #earch by keywords  + facets 
                size = 20
                sort = False
                query = generate_query_with_keywords(mustObj, 20, sort)
        else:
            if(hasNumbers(term)):
                #query search + facets + sort N
                size, text = get_number(term)
                sort = True
                query = generate_query(text, size, sort)
            else:
                 #query search + facets
                 size, text = get_number(term)
                 sort = False
                 query = generate_query(text, 20, sort)

    else:
        if(hasNumbers(term)):
            size, text = get_number(term)
            sort = True
            query = generate_query(text, size, sort)
        else:
            sort = False
            size, text = get_number(term)
            query = generate_query(text, 20, sort)
    

    try:
        return perfom_query(query, sort)
    except:
        print("Error")