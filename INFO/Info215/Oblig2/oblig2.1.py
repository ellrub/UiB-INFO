# Import the necessary modules. urllib.request is a built in module, 
# while BeautifulSoup has to be installed first with pip install
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# urlopen is from the urllib.request module. The urlopen function sends a request to the server, 
# the HTML content is then returned and stored in the variable.
# BeautifulSoup takes the HTML content from the html variable and parses it. Parsing is basically 
# analyzing the symbols in a string. BeautifulSoup parses it into an object with a nested data 
# structure, which allows us to navigate and search the HTML with different methods.
url = 'https://en.wikipedia.org/wiki/Star_Wars:_The_Rise_of_Skywalker'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser') 

# The methods refered to above would be the methods you see below.
for link in bs.find_all('a'): # Finds and loops through all the <a> tags and returns a list of them.
    href = link.get('href') # Returns the value from an attribute in a tag, in this case the href inside <a> tag.
    text = link.get_text() # Returns the text inside a tag, in this case the text insde the <a> tag
    if href: # Checks that the href is not None.
        full_url = urljoin(url, href) # get('href') returns the relative URL, urljoin combines that with the original absolute URL to create a new absolute URL 
        print(f'Text: {text}, URL: {full_url}') # If both conditions from the check above is met, then Text and URL is printed

for image in bs.find_all('img'):
    src = image.get('src')
    full_src = urljoin(url, src)
    print(f'Image source: {full_src}')