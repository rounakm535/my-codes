from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")


f_name = driver.find_element(By.NAME, value="fName")
l_Name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")


f_name.send_keys("Rounak")
l_Name.send_keys("mishra")
email.send_keys("mishra.rounak15@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()
