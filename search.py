# ActionChains - Automating a cookie clicker!
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:/Program Files (x86)/Google/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(2)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click()

for i in range()
