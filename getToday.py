import os
import datetime

import urllib
from bs4 import BeautifulSoup

def makeImagesDir():
    if not os.path.exists('./images'):
        os.mkdir('./images')

def downloadImage():
    date = datetime.date.today()
    url = 'https://www.nationalgeographic.com/photography/photo-of-the-day/2019/12/malaysia-borneo-palm-oil-terrace/'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    
    for link in soup.findAll('meta'):
        content = link.get('content')
        if content.endswith('1900.1.jpg'):
            print('Downloading...')
            f = open('images/' + str(date) + '.jpg' ,'wb')
            f.write(urllib.request.urlopen(content).read())
            f.close()
            print('Downloaded, put in images directory!')

makeImagesDir()
downloadImage()


