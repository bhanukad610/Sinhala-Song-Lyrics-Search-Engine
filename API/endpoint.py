import json
import requests

URL = "http://localhost:9200/songs/_search"

post_body = {
   "query":{
      "query_string":{
         "query":"මගේ පුංචි"
      }
   }
}

print(type(post_body))


try:
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = (requests.post(URL, data = json.dumps(post_body), headers = headers)).text

    res = json.loads(response)
    hits = res['hits']['hits'][0]

    print(type(hits))

    # for i in hits:
    #     print(i['_source']['Title'])

except:
    print("Error")