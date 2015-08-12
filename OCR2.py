from bs4 import BeautifulSoup
from urllib2 import urlopen
import requests
import re
url = raw_input("http://www.pythonchallenge.com/pc/def/ocr.html")
r = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")
data = r.text

#print(data)
print "".join(re.findall("[A-Za-z]", data))

