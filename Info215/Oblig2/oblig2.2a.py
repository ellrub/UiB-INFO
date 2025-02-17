from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Star_Wars:_The_Rise_of_Skywalker')
bs = BeautifulSoup(html, 'html.parser')

tds = bs.find_all('td', {'class': 'yes table-yes2 notheme'})

for td in tds:
    print(td.parent.get_text())