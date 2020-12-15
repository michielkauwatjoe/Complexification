#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import re

BASEURL = 'http://www.complexification.net'
URL = "http://www.complexification.net/gallery"
retrievedUrls = []


def getLinks(url, depth=2):
    if depth == 0:
        return
    else:
        depth -= 1

    retrievedUrls.append(url)
    try:
        response = requests.get(url)
    except:
        print('badly formed url %s' % url)
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.findAll('a'):#, attrs={'href': re.compile("^http://")}):
        newUrl = link.get('href')
        if newUrl in retrievedUrls:
            continue
        if newUrl.startswith('http'):
            if newUrl.startswith(BASEURL):
                print(newUrl)

        elif newUrl.endswith('html'):
            newUrl = newUrl.split('/')[-1]
            newUrl = BASEURL + '/' + newUrl
            print(newUrl)
            getLinks(newUrl, depth=depth)
        elif not newUrl.startswith('.'):
            newUrl = BASEURL + '/' + newUrl
            print(newUrl)
            getLinks(newUrl, depth=depth)
        else:
            print(' * %s' % newUrl)


getLinks(URL)
