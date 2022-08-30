#Tutorial: https://www.youtube.com/watch?v=pUUhvJvs-R4&list=PLRzwgpycm-FgQ9lP_JTfrCa9O573XiJph&index=1&ab_channel=JohnWatsonRooney
#Step 1: install selenium and webdriver for my version of my broswer i.e. Chrome 100.0.4896.127 and store it in same folder as Python files
#Chrome Drivers link: https://chromedriver.storage.googleapis.com/index.html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

#How to open a webpage
url = "https://www.google.com/"
driver.get(url)

time.sleep(2)

'''To input data into an element. 
First inspect element and find the "XPath" of the element
'''
url = "https://the-internet.herokuapp.com/login"

driver.get(url)

#send_keys() allows us to actually send/enter in info/characters for that element 
driver.find_element_by_xpath('//*[@id="username"]').send_keys("tomsmith")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("SuperSecretPassword!")
driver.find_element_by_xpath('//*[@id="login"]/button').click()

time.sleep(3)


#To scrape data that is loaded dynamically after the website is fully loaded statically

url = "https://the-internet.herokuapp.com/dynamic_loading/2"

driver.get(url)

driver.find_element_by_xpath('//*[@id="start"]/button').click()

#keep checking whether the element below has loaded
#max wait time is 10 sec, much better than using time.sleep() for waiting for dynamic info
driver.implicitly_wait(10)
text = driver.find_element_by_xpath('//*[@id="finish"]/h4').text
print(text)


driver.quit()
