#! /usr/bin/python3

from urllib.request import urlopen

from bs4 import BeautifulSoup

user_input = input("What do you want to know about the Wheel of Time?")
url = f"https://wot.fandom.com/wiki/{user_input}?so=search"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)

"""
import nltk   
from urllib.request import urlopen

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"    
html = urlopen(url).read()    
raw = nltk.clean_html(html)  
print(raw)


import time
import webdriver

# start web browser
browser=webdriver.Chrome()

# get source code
browser.get("https://en.wikipedia.org")
html = browser.page_source
time.sleep(2)
print(html)

# close web browser
browser.close()

url=('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')

page = urlopen(url)
print(page)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)

import re
everything=re.findall()
print(everything)


#soup = BeautifulSoup(site)
#print(soup.prettify())
"""


