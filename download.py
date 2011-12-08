#!/usr/bin/python
#Filename:download.py
import urllib2
from BeautifulSoup import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import os
import sys

starturl = r'http://movie.douban.com/subject/4920528/photos?type=S'
def download(url):
    soup = bs(urlopen(url))
    parsed = list(urlparse.urlparse(url))

    for image in soup.findAll("img"):
        print "Image:%(src)s" % image
        filename = image["src"].split("/")[-1]
        parsed[2] = image["src"]
        if parsed[2].find('thumb') != -1:
            imageurl = parsed[2].replace('thumb','raw')
        else:
            imageurl = parsed[2]
        print "ImagePath:%s" % imageurl
        outpath = os.path.join(filename)
        #outpath = os.path.dirname(os.path.abspath(__file__))
        print outpath
        if image["src"].lower().startswith("http"):
            urlretrieve(imageurl, outpath)
        else:
            urlretrieve(urlparse.urlunparse(parsed),outpath)

    nexturl = soup.find(rel='next')['href']
    print nexturl
    if nexturl != None:
        download(nexturl)

download(starturl)

