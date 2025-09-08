from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

op = Options()
op.add_argument('--headless')
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = s, options = op)

url = "https://sites.google.com/view/nikt2024?usp=sharing"
driver.get(url) 

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="h.rdjh98q96cki_l"]/div/span'))
    )
except TimeoutException:
    print('Did not find the element')

finally:
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