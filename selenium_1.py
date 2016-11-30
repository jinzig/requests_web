from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

url = 'https://www.linkedin.com/'
browser = webdriver.PhantomJS(executable_path='/Applications/phantomjs')
browser.get(url)
time.sleep(5)
elem_name = browser.find_element_by_id('login-email')
elem_name_2 = browser.find_element_by_id('login-password')
elem_name.send_keys('jinzig@gmail.com')
elem_name_2.send_keys('0451gznij' + Keys.RETURN)
time.sleep(5)
browser.get('http://www.linkedin.com/nhome/')
# print(content)

content = BeautifulSoup(browser.page_source, 'html.parser').prettify()
print(content)
