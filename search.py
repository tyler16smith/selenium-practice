# Selenium web testing automation
from selenium.webdriver.common.keys import Keys # access keys like "enter"
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

PATH = "C:/Program Files (x86)/Google/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)

# search 'python'
search = driver.find_element_by_name("s")
search.send_keys("python")
search.send_keys(Keys.RETURN)

# wait for the webpage to open
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name("article")

    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)

finally:
    driver.quit()
