from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.read(), 'html.parser')
namelist = bs.find_all(text = 'the prince')
print(len(namelist))
