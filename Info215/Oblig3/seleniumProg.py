from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

op = Options()
op.add_argument('--headless')
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = s, options = op)

url = "https://sites.google.com/view/nikt2024?usp=sharing"
driver.get(url) 
driver.implicitly_wait(10)

link_visited = set()
num_links = 0
for link in driver.find_elements(By.TAG_NAME, 'a'):
    href = link.get_attribute('href')
    if href and 'sites.google.com' in href not in link_visited:
        link_visited.add(href)

for internal_url in link_visited:
    driver.get(internal_url)
    texts = driver.find_elements(By.XPATH, "//span[@class='C9DxTc ']")
    for text in texts:
        print(text.text)

for link in link_visited:
    print(link)
print(f'Links visited: {len(link_visited)}')

driver.quit()