# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# url = 'https://en.wikipedia.org/wiki/Ukraine'
# html = urlopen(url)
# bs = BeautifulSoup(html, 'html.parser')

# thumbnail_div = bs.find_all('div', {'class': 'thumbinner'})

# for thumbnail in thumbnail_div:
#     thumbnail_img_link = thumbnail.find('a').get('href')
#     thumbnail_caption = thumbnail.find('div', {'class': 'thumbcaption'}).get_text()

#     print(f"'{thumbnail_img_link}' - {thumbnail_caption}")






from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

# Extract and print title, price and image source of the thumbnail for each book on the first page.
# Book title = h3 --> a --> 'title'
# Book price = div (class 'product_price') --> first p text
# Book img source = img (class 'thumbnail') 'src'
# article (class 'product_pod')

book_listing = bs.find_all('article', {'class': 'product_pod'})

for book in book_listing:
    title = book.find('h3').find('a').get('title')
    price = book.find('div', {'class': 'product_price'}).find('p').get_text()
    image = book.find('img', {'class': 'thumbnail'}).get('src')

    print(f"Title: {title}, Price: {price},\nThumbnail: {image}")