
import json,csv
import bs4 

import sys
import lxml.html
from lxml.cssselect import CSSSelector
# import requests
from selenium import webdriver

# site_file = 'https://ja.wikipedia.org/wiki/Android%E7%AB%AF%E6%9C%AB%E4%B8%80%E8%A6%A7'
site_file=open("site.html", "r")

contents=site_file.read()

# res.text=lxml.html.fromstring( contents )
dom=bs4.BeautifulSoup(contents, "html.parser")
print ( dom.select('.wikitable.sortable') )
# sel = CSSSelector('div.wikitable')

# print (sel.css)

# links=par_text.cssselect('title')[0].text
# print (links)