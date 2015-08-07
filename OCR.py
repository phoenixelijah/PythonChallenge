__author__ = 'vogda04'
import requests
import lxml
page = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
print(page)
tree = lxml.html.fromString(page.text)