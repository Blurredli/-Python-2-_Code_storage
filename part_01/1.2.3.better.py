from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
        html.info().get_content_charset('utf-8')
    except HTTPError as e:
        print(f"HTTP error occurred: {e.code}")
        return None
    try:
        bs = BeautifulSoup(html.read(), "html.parser")
        title = bs.body.h1.get_text() if bs.body.h1 else None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return title
title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Tiele cound not be found")
else:
    print(title)