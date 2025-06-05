# L-01

# from urllib.request import urlopen # Standard Python library module
# from bs4 import BeautifulSoup # Needs to be installed before it can be used

# url = 'https://en.wikipedia.org/wiki/Ukraine'
# html = urlopen(url)
# bs = BeautifulSoup(html, 'html.parser')

# for thumbnail in bs.find_all('div', {'class': 'thumbinner'}):
#     imglink = thumbnail.find('a').get('href')

#     caption_txt = thumbnail.find('div', {'class': 'thumbcaption'}).get_text()

#     print(f"'{imglink}'\n{caption_txt}")

# I've assumed that the structure of 'thumbinner' does not change throuought the apge.
# Meaning that this is what i'm going for:
# We first look for a <div> tag with the class 'thumbinner'
# We then look inside that <div> and grab the first <a> tag, which according to the structure,
# contains the href to the image.
# We then look for a <div> tag with the class of 'thumbcation', still inside 'thumbinner', and 
# grab all the text from any tag insde.
# In the end we print out the link, newline, and then the text

# L-02

# from urllib.request import urlopen # Standard Python library module
# from bs4 import BeautifulSoup # Needs to be installed before it can be used

# url = 'https://www.pythonscraping.com/pages/page3.html'
# html = urlopen(url)
# bs = BeautifulSoup(html, 'html.parser')

# # for product_img_link in bs.find('table').find_all('img'):
# #     product_img_link = product_img_link.get('src')
# #     print(f"'{product_img_link}'")

# for product_img in bs.find_all('table'):
#     for product_img_link in product_img.find_all('img'):
#         product_img_link = product_img_link.get('src')
#         print(f"'{product_img_link}'")

# # Considering that the output example shows a relative path '../img/...', i'm assuming no URL's,
# # and that it's only the relative path that's the task here.

# Broad-Q1

# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# url = 'https://en.wikipedia.org/wiki/Winter_Olympic_Games'
# html = urlopen(url)
# bs = BeautifulSoup(html, 'html.parser')

# # This is assuiming that this is the only table with this class (which it's probably not),
# # but there are no unique identifiers.
# table = bs.find('table', {'class': 'wikitable'})
# rows = table.find('tbody').find_all('tr')[1:] # Skipping the header row with [1:]

# for row in rows:
#     cells = row.find_all('td')
#     nation_name = cells[0].find('a').get_text()
#     total_medals = cells[4].get_text()

#     print(f"{nation_name} - {total_medals}")

# Broad-Q2

# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# url = 'https://en.wikipedia.org/wiki/Leonardo_da_Vinci'
# html = urlopen(url)
# bs = BeautifulSoup(html, 'html.parser')

# for gallerybox_link in bs.find_all('li', {'class': 'gallerybox'}):
#     gallery_link = gallerybox_link.find('a').get('href')
#     print(f"'{gallery_link}'")

# L-01

# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# url = 'https://en.wikipedia.org/wiki/Ukraine'
# html = urlopen(url)
# bs = BeautifulSoup(html, 'html.parser')

# for thumbnail in bs.find_all('div', {'class': 'thumbinner'}):
#     thumbnail_link = thumbnail.find('a').get('href')

#     thumbnail_caption_div = thumbnail.find('div', {'class': 'thumbcaption'}).get_text()

#     print(f"'{thumbnail_link}'\n{thumbnail_caption_div}")

# L-02

# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# url = 'https://www.pythonscraping.com/pages/page3.html'
# html = urlopen(url)
# bs = BeautifulSoup(html, 'html.parser')

# table = bs.find('table', {'id': 'giftList'})

# for img in table.find_all('img'):
#     img = img.get('src')
#     print(f"'{img}'")
