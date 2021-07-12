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

link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    # waiting load until element search
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    # go back
    driver.back()
    driver.back()
    driver.back()

    # go forward
    driver.forward()
    driver.forward()

except:
    driver.quit()

time.sleep(5)
