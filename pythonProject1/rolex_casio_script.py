from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")
search_field = driver.find_element(By.XPATH, "//input[@placeholder = 'Search for anything']")
search_field.send_keys("Watch")
search_btn = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//input[@value = 'Search']")))
search_btn.click()
brand_rolex = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//li[@class = 'x-refine__main__list--value' and @name = 'Brand']//input[@aria-label = 'Rolex']")))
brand_rolex.click()

# Find all elements that contain both title and price
rolex_items = driver.find_elements(By.XPATH, "//div[contains(@class, 's-item__info')]")

rolex_titles_gallery = {}
rolex_prices_gallery = {}
rolex_mismatch = []

title_text = ''
price_text = ''
title_element = ''
price_element = ''

# Go through each item and retrieve title and price together

for index, item in enumerate(rolex_items[2:4], start=1):  # first two empty
    title_element = item.find_element(By.XPATH, ".//span[@role = 'heading']")
    price_element = item.find_element(By.XPATH, ".//span[contains(@class, 's-item__price')]")

    title_text = title_element.text
    price_text = price_element.text

# Store title and price
    if 'rolex' in title_text.lower():
        rolex_titles_gallery[f"title_{index}"] = title_text
        rolex_prices_gallery[f"price_{index}"] = price_text
    else:
        rolex_mismatch.append(title_text)

# Navigate to Rolex single view
title_element.click()

handles = driver.window_handles
driver.switch_to.window(handles[-1])
print("Switched to New Window Title:", driver.title)

rolex_title_single_page_view = driver.find_element(By.XPATH, "//div[@id = 'mainContent']//h1[contains(@class, 'x-item-title__mainTitle')]/span")
rolex_price_single_page_view = driver.find_element(By.XPATH, "//div[@id = 'mainContent']//div[contains(@class, 'x-price-primary')]/span")
rolex_title = rolex_title_single_page_view.text
rolex_price = rolex_price_single_page_view.text

driver.close()
driver.switch_to.window(handles[0])
# Verify title and prices are the same on gallery and on single view page
assert title_text.lower().replace(' ', '') == rolex_title.lower().replace(' ', '')
assert price_text.lower().replace(' ', '').split('$')[-1] == rolex_price.lower().replace(' ', '').split('$')[-1]

# Displaying mismatch if any
print("Mismatched item in rolex gallery:", rolex_mismatch)

# uncheck rolex
brand_rolex = driver.find_element(By.XPATH, "//li[@class = 'x-refine__main__list--value' and @name = 'Brand']//input[@aria-label = 'Rolex']")
brand_rolex.click()

# Select Casio ========================================================================================================
brand_casio = driver.find_element(By.XPATH, "//li[@class = 'x-refine__main__list--value' and @name = 'Brand']//input[@aria-label = 'Casio']")
brand_casio.click()
casio_items = driver.find_elements(By.XPATH, "//div[contains(@class, 's-item__info')]")

casio_titles = {}
casio_prices = {}
casio_mismatch = []

for index, item in enumerate(casio_items[2:4], start=1):
    title_element = item.find_element(By.XPATH, ".//span[@role = 'heading']")
    price_element = item.find_element(By.XPATH, ".//span[contains(@class, 's-item__price')]")

    title_text = title_element.text
    price_text = price_element.text

    # Store titles and prices in a dict for further needs
    if 'casio' in title_text.lower():
        casio_titles[f"title_{index}"] = title_text
        casio_prices[f"price_{index}"] = price_text
    else:
        casio_mismatch.append(title_text)

# Navigate to Casio page
title_element.click()
handles = driver.window_handles
driver.switch_to.window(handles[-1])
print("Switched to New Window Title:", driver.title)

# Find Casio title and price on Casio single page
casio_title_single_page_view = driver.find_element(By.XPATH, "//div[@id = 'mainContent']//h1[contains(@class, 'x-item-title__mainTitle')]/span")
casio_price_single_page_view = driver.find_element(By.XPATH, "//div[@id = 'mainContent']//div[contains(@class, 'x-price-primary')]/span")
casio_title = casio_title_single_page_view.text
casio_price = casio_price_single_page_view.text
# Assert titles and prices the same on gallery page and on single view page
assert title_text.lower().replace(' ', '') == casio_title.lower().replace(' ', '')
assert price_text.lower().replace(' ', '').split('$')[-1] == casio_price.lower().replace(' ', '').split('$')[-1]

print("Mismatched items in casio gallery:", casio_mismatch)

driver.close()

