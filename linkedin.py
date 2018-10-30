from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get("https://linkedin.com")
#This line adds the email to username
driver.find_element_by_xpath('//*[@id="login-email"]').send_keys("username@gmail.com")

#This line adds the password for the password button
driver.find_element_by_xpath('//*[@id="login-password"]').send_keys("passwd")

#This line clicks on login button where username and password added
driver.find_element_by_xpath('//*[@id="login-submit"]').click()

#This line clicks on "My Network"
driver.find_element_by_xpath('//*[@id="mynetwork-nav-item"]/a/span[2]').click()
