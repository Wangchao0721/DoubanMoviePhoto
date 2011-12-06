#!/usr/bin/python
#Filename:download.py
import urllib2
from BeautifulSoup import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import os
import sys

url = r'http://movie.douban.com/subject/4920528/photos?type=S'
out_folder = "/test/"
def main(url):
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
    print "ImagePath:%s" % parsed[2]
    outpath = os.path.join(filename)
    if image["src"].lower().startswith("http"):
      urlretrieve(imageurl, outpath)
    else:
      urlretrieve(urlparse.urlunparse(parsed), outpath) 

main(url)
