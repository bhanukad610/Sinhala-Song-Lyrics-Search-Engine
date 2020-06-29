# Sinhala-Song-Lyrics-Search-Engine
Song lyrics search engine for Sinhalese language using Elasticsearch. 

The corpus contains sinhala songs with following parameters.The corpus is created by using the https://sinhalasongbook.com/ website.

1. 'Artist' - the artist
2. 'Lyrics'- the lyrics artist
3. 'Key'- guitar key
4. 'Genre' - genre of the song
5. 'Music' - the musician of the song
6. 'Song'- lyrics content
7. 'Title' - title of the song
8. 'title-en' - title in english
9. 'Visits' - number of visits to the song

#### Endpoints and techniques used in designing indexing and querying

| Endpoint  | Request Type | Functionality | Example |
| ------------- | ------------- | ---------- | -----------|
| /searchBy  | GET  | Ruled based classification explained in the diagram  |  /searchBy term=වික්ටර් රත්නායක ගෙ ක්ලැසික් නුඹේ නමින් මා දුක්වී ගොතනා කවි වැල් නුඹට 2 |
| /searchBy/param  | GET  | Search by specific filed with a term  |  /seachBy/param searchby=Title&term=බඹරෙකු හැඬුවා |
| /searchBy/visits  | GET  | Range search by visits  |  searchBy/visits?visists=500,1000 |
| /multisearchBy/param  | GET  | Multi-search with set of fields with a term  |  multiSearchBy/param?searchby=Song,Title,Artist&term=නුඹ වගෙයි |
| /facetedSearch  | POST  | After selecting filters from received facets request to this with the term and selected filters  |  /facetedSearch { “term”: “බඹරෙකු හැඬුවා“, “filter” : [    {“Lyrics” : "උපාලි ධනවලවිථන"}, {“Artist”: “මිල්ටන් මල්ලවරාච්චි”}]}  | 
| /advancedSeach  | POST  | Search with given set of fields including range of visit  |  {"filter" : [       {"keyword" : "Artist",      "value": "ක්ලැරන්ස් විජේවර්ධන" },     {"keyword" : "Genre",       "value": "පැරණි පොප්ස්" },     {"keyword" : "Music",       "value": "ක්ලැරන්ස් විජේවර්ධන" },     {"keyword" : "Lyrics",       "value": "ක්ලැරන්ස් විජේවර්ධන" }  ],  "range": {"gte" : 100,            "lte": 1000}} |

#### Ruled based classification in /searchBy
Search text should be in Sinhala.
![alt text](https://github.com//[reponame]/blob/[branch]/image.jpg?raw=true)
