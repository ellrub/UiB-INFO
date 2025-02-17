from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Web_scraping'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

for link in bs.find('div', {'class': 'div-col'}).find_all('a'):
    href = link.get('href')
    full_url = urljoin(url, href)
    load_page = urlopen(full_url)
    new_bs = BeautifulSoup(load_page, 'html.parser')

    for new_link in new_bs.find('p'):
        text = new_link.get_text()
        print(text)