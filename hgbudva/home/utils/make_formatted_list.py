import os
import json


urls = open('urls.txt', 'r')
formatted = open('formatted.txt', 'a')

url = 'en/hotel-slovenska-plaza-in-budva/3-star-guest-rooms/'

search_list = []

for url in urls.readlines():
    search_obj = {
        'url':url
    }
    url = url.replace('/','-').rstrip()
    url_keywords = url.split('-')
    search_obj['lang'] = url_keywords[3]
    search_obj['keywords']= url_keywords[4:-1]
    search_obj['title']=' '.join(url_keywords[4:-1]).title()
    search_list.append(search_obj)
result = {
    "results": search_list
    }

json.dump(result, formatted)
