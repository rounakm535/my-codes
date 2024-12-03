from use import webdriver
from use.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")


search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

selector = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(selector.text)

path = driver.find_element(By.XPATH, value="//*[@id='site-map']/div[2]/div/ul/li[3]/a")
print(path.text)


loop = driver.find_element(By.XPATH, value="//*[@id='content']/div/section/div[3]/div[2]")
print(loop.text)
driver.quit()