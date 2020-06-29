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

### Quick start
#### Pre requesists : 
- Python and flask and Elasticsearch needed in your PC.

#### Steps : 
1. Clone the repository.
2. Run an Elasticsearch instance on port 9200.
3. Go to the folder Corpus. Run the python script send.py to put the corpus to the elasticsearch.
4. Then go to the Flask_app folder and open a terminal and run the follwing commands. 
  ```
source venv/bin/activate
export FLASK_APP=controller
flask run
```
5. Now you can create requests to below mentioned endpoints.

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
Search text should be in Sinhala

![alt text](https://github.com/bhanukad610/Sinhala-Song-Lyrics-Search-Engine/blob/master/Flask_app/IR%20-%20Rules.png?raw=true)

##### Keywrods used for diffrent fileds:
- artist_key_words = ['ගෙ', 'ගැයූ','ගයන', 'කියන', 'කියූ', 'ගායනා']
- lyrics_key_words = ['ලියූ', 'ලියන', 'ලිව්ව', 'රචනා', 'රචිත', 'ලීව']
- music_key_words = ['සංගීත']
- genre_key_words = ['පොප්', 'ක්ලැසික්', 'දේවානුභාවයෙන්','පොප්ස්','ඩුවට්ස්','ක්ලැසික්','යුගල','ඕල්ඩීස්','කැලිප්සෝ','ළමා']

#### Usage of advanced features
- Used facet feature selected set of queries. In Elasticseach, aggregations are used for that purpose. Top 5 facets in the selected field are taken.
- Range queries were used to filter by the total number of visits.
