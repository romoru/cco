
import json
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup 

url = 'http://www.dennobaio.jp/'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
   the_page = response.read()
   #print (the_page)
   soup = BeautifulSoup(the_page, 'lxml')
   print (soup.)


