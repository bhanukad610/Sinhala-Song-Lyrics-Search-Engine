# Sinhala-Song-Lyrics-Search-Engine
Song lyrics search engine for Sinhalese language using Elasticsearch and python. 

The corpus contains Sinhala songs with the following parameters. The corpus is created by using the https://sinhalasongbook.com/ website.

1. 'Artist' - the artist
2. 'Lyrics'- the lyrics artist
3. 'Key'- guitar key
4. 'Genre' - the genre of the song
5. 'Music' - the musician of the song
6. 'Song'- lyrics content
7. 'Title' - the title of the song
8. 'title-en' - title in English
9. 'Visits' - the number of visits to the song

### Directory 
├── Corpus: original data, the processed data and the python script to put to Elasticsearch  
├── Flask_app: Backend of the search engine  
├── lyrics: Python scripts used to prepare the corpus


### Quick start
#### Pre requesists : 
- Python, Flask, requests library and Elasticsearch needed in your PC.

#### Steps : 
1. Clone the repository.
2. Run an Elasticsearch instance on port 9200.
3. Go to the folder Corpus. Run the python script send.py to put the corpus to the Elasticsearch.
4. Then go to the Flask_app folder and open a terminal and run the following commands. 
  ```
source venv/bin/activate
export FLASK_APP=controller
flask run
```
5. Now you can create requests to below-mentioned endpoints.

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
