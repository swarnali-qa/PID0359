import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome("C:\\Python36-32\\selenium\\webdriver\\chromedriver.exe")

#navigate to the application's home page
driver.get("http://google.com")
driver.maximize_window()
time.sleep(5)
search_field=driver.find_element_by_link_text("Gmail")
search_field.click()
driver.implicitly_wait(3)
search_field=driver.find_element_by_id("identifierId")
search_field.send_keys("etsqa10@gmail.com")
search_field=driver.find_element_by_class_name("CwaK9")
search_field.click()
driver.implicitly_wait(3)
search_field=driver.find_element_by_name("password")
search_field.send_keys("ets@072017")
search_field=driver.find_element_by_class_name("CwaK9")
search_field.click()
