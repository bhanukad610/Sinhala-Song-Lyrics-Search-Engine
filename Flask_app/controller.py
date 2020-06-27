from flask import Flask
from flask import request

from search_all import search_all
from search_by_param import search_by_param
from search_by_term import search_by_term
from multi_search import multi_search
from search_by_visits import search_by_visits
from facetedSearch import facetedSearch
from advancedSearch import advancedSearch

app = Flask(__name__)

@app.route('/')
def hello_world():
    return search_all()

@app.route('/searchBy')
def searchby_term():
    term = request.args.get('term')
    return search_by_term(term)

@app.route('/searchBy/param')
def searchby_param():
    parameter = request.args.get('searchby')
    term = request.args.get('term')
    return search_by_param(parameter, term)

@app.route('/searchBy/visits')
def searchby_rating():
    visits = (request.args.get('visits')).split(",")
    return search_by_visits(visits)

@app.route('/multiSearchBy/param')
def multi_searchby_param():
    parameter = (request.args.get('searchby')).split(",")
    term = request.args.get('term')
    return multi_search(parameter, term)

@app.route('/facetedSearch', methods=['GET', 'POST', 'DELETE', 'PUT'])
def faceted_search():                                                                                                                              
    data = request.get_json()
    return facetedSearch(data)

@app.route('/advancedSearch', methods=['GET', 'POST', 'DELETE', 'PUT'])
def advanced_search():                                                                                                                              
    data = request.get_json()
    return advancedSearch(data)