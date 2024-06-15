from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, "html.parser")

x = bs.find(lambda tag: len(tag.attrs) == 2)
print(x)