#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import urllib
import urllib2
import json
#import jsonlib

# CHANGE the referer URL below FOR YOUR OWN.
REFERER = 'http://www.twigraphy.org/'

API_KEY = "key=AIzaSyAESOk9qWf6TqH6tAd1qX708s4TyHaR6Ak"

BASEURLS = {
    'web': 'http://ajax.googleapis.com/ajax/services/search/web',
    'local': 'http://ajax.googleapis.com/ajax/services/search/local',
    'video': 'http://ajax.googleapis.com/ajax/services/search/video',
    'blog': 'http://ajax.googleapis.com/ajax/services/search/blogs',
    'news': 'http://ajax.googleapis.com/ajax/services/search/news',
    'book': 'http://ajax.googleapis.com/ajax/services/search/books',
    'image': 'http://ajax.googleapis.com/ajax/services/search/images',
    'en2ja': 'https://www.googleapis.com/language/translate/v2?'+API_KEY+'&source=en&target=ja',
    'ja2en': 'https://www.googleapis.com/language/translate/v2?'+API_KEY+'&source=ja&target=en'
}

def search(query, referer=REFERER, type='web', **kwargs):
    # Find the URL for the specific type of Google AJAX Search API.
    baseurl = BASEURLS.get(type)
    if baseurl is None:
        raise TypeError

    # Add the necessary arguments.
    kwargs.update({
        #'v': 1.0,
        'q': query,
    })

    # Build the URL.
    url = '&'.join((baseurl, urllib.urlencode(kwargs)))

    # Debug
    #print url
    #url = 'https://www.googleapis.com/language/translate/v2?key=AIzaSyAESOk9qWf6TqH6tAd1qX708s4TyHaR6Ak&target=ja&q=Hello'
    
    # Add a referer HTTP header to the request.
    req = urllib2.Request(url)
    req.add_header('Referer', referer)
    f = urllib2.urlopen(req)

    # Translate the JSON response to a Python object.
    return json.load(f) #jsonlib.read(f.read())

def read_file(filename):
    if os.path.exists('./'+filename) == False:
        print "No such a file."
        return        
    input = open(filename, "r")
    return input.read()        

if __name__ == '__main__':
    if not (len(sys.argv) == 3):
        print "Usage: python api-translate.py FILENAME TYPE"
        exit()

    filename = sys.argv[1] #.encode('utf-8')
    t = sys.argv[2]
    query = read_file(filename)    
    sentence_list = query.split('\n')
    for sentence in sentence_list:
        res = search(sentence, type=t)
        print res['data']['translations'][0]['translatedText'].encode("utf-8")
    # Show the full response from the service.
    #print response
    # Show the Google count for the query.
    #print res['responseData']['cursor']['estimatedResultCount']

    # Debug
    #print str(res['responseData'])
    
    # Show Only Content
    i = 1

