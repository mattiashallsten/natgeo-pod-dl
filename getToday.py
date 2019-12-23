#!/usr/bin/python3

import os
import datetime

import urllib
from bs4 import BeautifulSoup

def makeImagesDir():
    if not os.path.exists('./images'):
        os.mkdir('./images')

def downloadImage():
    date = datetime.date.today()
    url = 'https://www.nationalgeographic.com/photography/photo-of-the-day/'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    
    for meta in soup.findAll('meta'):
        link = meta.get('content')
        if meta.get('property') == "og:image":
            print('Downloading...')
            f = open('images/' + str(date) + '.jpg' ,'wb')
            f.write(urllib.request.urlopen(link).read())
            f.close()
            print('Downloaded, put in images directory!')

makeImagesDir()
downloadImage()


