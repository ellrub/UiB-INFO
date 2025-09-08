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

'''
Much like in task 2.1, we import the neccessary libs. We define the url we want to open
and use beautifulsoup to parse the url. We then create a for loop that look for divs with the class div-col
and fetches all a tags from those divs, in this case only one div. We also collect all the url from the a tags,
make sure to make the absolute links, open and parse them.

We then use a second for loop to loop through all the links we open, and grab the text from the first p tag.
Due to some p tags being empty, some urls will not return an article to be printed
'''