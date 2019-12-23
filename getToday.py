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

    # Read through the object created by soup, find every meta tag
    for meta in soup.findAll('meta'):
        link = meta.get('content')
        # If the meta tag has the property "og:image", download the file
        if meta.get('property') == "og:image":
            print('Downloading...')

            # Open a file in the images directory, define a name, download the file
            f = open('images/' + str(date) + '.jpg' ,'wb')
            f.write(urllib.request.urlopen(link).read())
            f.close()
            print('Downloaded, put in images directory!')

makeImagesDir()
downloadImage()


