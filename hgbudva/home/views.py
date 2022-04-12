import os
from os.path import join
import json

from django.http import HttpResponse

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


def search_hgbr(request):

    query_lang = request.GET['lang']
    query_input = request.GET['query']


    query_lang_clean = query_lang.lower()
    query_list = query_input.lower().split(' ')
    query_list_clean = [q if q.isalnum() else '' for q in query_list]

    result_list = []

    f = open(join(PROJECT_DIR, 'home/static/search/search_result.json'), "r")

    formatted_list = json.load(f)
    for formatted_obj in formatted_list['results']:
        if all(q in formatted_obj['keywords'] for q in query_list_clean):
            if formatted_obj['lang'] == query_lang:
                result_list.append({'title': formatted_obj['title'],
                                   'url':formatted_obj['url']})
                
    return HttpResponse(json.dumps({'results':result_list}))
