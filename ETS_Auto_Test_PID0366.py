import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#naviaget to chrome driver
#creating browser instance
driver=webdriver.Chrome("C:\\Python36-32\\selenium\\webdriver\\chromedriver.exe")


#TC001 #check if the home page is coming properly
#navigate to the application's home page
driver.get("http://www.ets-demo.com/s/startwriteIndia/dev/")
print(driver.title)
driver.maximize_window()
search_field=driver.find_element_by_link_text("Home").click()
search_field=driver.find_element_by_tag_name("html")
search_field.send_keys(Keys.END)
time.sleep(5)


#TC002 #check if the site map is working
#navigate site map in home page
search_field=driver.find_element_by_link_text("Site Map").click()
search_field=driver.find_element_by_tag_name("html")
search_field.send_keys(Keys.END)
time.sleep(3)
search_field.send_keys(Keys.HOME)
#naviaget to home page
driver.back()


#TC003 #check if the Ideas for use and its functionalities are working
#navigate to home page to go to Idea for use page
search_field=driver.find_element_by_tag_name("html")
search_field.send_keys(Keys.END)
search_field=driver.find_element_by_link_text("Idea For Use").click()
time.sleep(8)
search_field=driver.find_element_by_tag_name("html")
search_field.send_keys(Keys.END)
search_field=driver.find_element_by_link_text("Ideas for Parents").click()
time.sleep(8)
#naviagte to Ideas for use page
driver.back()
search_field=driver.find_element_by_tag_name("html")
search_field.send_keys(Keys.END)
time.sleep(8)
search_field=driver.find_element_by_link_text("Ideas for Teachers").click()
time.sleep(8)
search_field=driver.find_element_by_tag_name("html")
search_field.send_keys(Keys.END)
time.sleep(8)
search_field.send_keys(Keys.HOME)
#naviagte to Ideas for use page
driver.back()
#naviagte to Home page
driver.back()
time.sleep(8)



#TC004 #check if the Blog page is working
#navigate to Blog page
search_field=driver.find_element_by_tag_name("html")
search_field.send_keys(Keys.END)
search_field=driver.find_element_by_link_text("Blog").click()
time.sleep(8)
#naviagte to Home page
driver.back()


#TC005 #check if the Logo is redirecting to Eclipse site
#navigate to eclipse site after clicking on logo
search_field=driver.find_element_by_class_name("img-responsive").click()
driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL+'w')





