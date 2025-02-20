from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Star_Wars:_The_Rise_of_Skywalker')
bs = BeautifulSoup(html, 'html.parser')

tds = bs.find_all('td', {'class': 'yes table-yes2 notheme'})

for td in tds:
    print(td.parent.get_text())

'''
The colum containing the data about Award and Date of ceremony always belongs to the
first tablerow and just spans accross multiple rows so that it looks correct visually,
but this mean that the data only lives in the first colum in the series.
'''