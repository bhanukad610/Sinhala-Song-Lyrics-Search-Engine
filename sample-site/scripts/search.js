// Define basePath to elasticsearch and index
var basePath = 'http://localhost:9200';
var index = 'songs'

var loadingdiv = $('#loading');
var noresults = $('#noresults');
var resultdiv = $('#results');
var searchbox = $('input#search');
var timer = 0;

// Executes the search function 500 milliseconds after user stops typing
searchbox.keyup(function () {
  clearTimeout(timer);
  timer = setTimeout(search, 1000);
});

// Get response from elasticsearch
var getResponse = function (query) {
  var url = basePath + '/' + index + '/' + '_search';
  return fetch(url, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: '{"size":50,"query":{"multi_match":{"query":"' + query + '"}}}'
  })
  .then(function(response) {
    return response.text();
  })
  .then(function(data){
    var data_obj = JSON.parse(data);
    return data_obj
  })
}

async function search() {
  // Clear results before searching
  noresults.hide();
  resultdiv.empty();
  loadingdiv.show();
  // Get the query from the user
  let query = searchbox.val();
  // Only run a query if the string contains at least three characters
  if (query.length > 2) {
    // Make the HTTP request with the query as a parameter and wait for the JSON results
    let response = await getResponse(query)
    // Get the part of the JSON response that we care about
    let results = response['hits']['hits'];
    if (results.length > 0) {
      loadingdiv.hide();
      // Iterate through the results and write them to HTML
      resultdiv.append('<p>Found ' + results.length + ' results.</p>');
      for (var item in results) {
        //let url = 'https://www.imdb.com/title/' + results[item]._id;
        //let image = results[item]._source.fields.image_url;
        let title = results[item]._source.fields.title;
        //let plot = results[item]._source.fields.plot;
        //let year = results[item]._source.fields.year;
        // Construct the full HTML string that we want to append to the div
        resultdiv.append('<div class="result">' +
        '<a href="' + url + '"><img src="' + image + '" onerror="imageError(this)"></a>' +
        '<div><h2><a href="' + url + '">' + title + '</a></h2><p>' + year + ' &mdash; ' + plot + '</p></div></div>');
      }
    } else {
      noresults.show();
    }
  }
  loadingdiv.hide();
}

// Tiny function to catch images that fail to load and replace them
function imageError(image) {
  image.src = 'images/no-image.png';
}
