from use import webdriver
from use.webdriver.common.by import By
from use.webdriver.support.ui import WebDriverWait
from use.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=dp_fod_sccl_2/130-8117768-4452455")

try:
    # Wait until the price dollar element is present
    price_dollar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
    )

    # Wait until the price cent element is present
    price_cent = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-price-fraction"))
    )

    print(f"The price of the item is {price_dollar.text}.{price_cent.text}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
