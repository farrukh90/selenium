from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get("https://phptravels.org/clientarea.php")
driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys("user@phptravels.com")
driver.find_element_by_xpath('//*[@id="inputPassword"]').send_keys("demouser")
driver.find_element_by_xpath('//*[@id="login"]').click()
time.sleep(15)
driver.quit()
