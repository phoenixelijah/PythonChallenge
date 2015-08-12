from lxml import html
import requests
import re
page = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
print(page)
tree = html.fromstring(page.text)
myTest = tree.xpath('//')
#myText = tree.xpath('//span[@class="html-commment"]/text()')
myText = """"""
print 'the text: ', myText
print "".join(re.findall("[A-Za-z]", myText))