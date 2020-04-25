from selenium import webdriver
import time

browser = webdriver.Chrome()
url ='Https://google.com'
browser.get(url)

time.sleep(2)
"""

"""
name = 'q'
search_el = browser.find_element_by_name(name)
search_el.send_keys("selenium python")

submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
print(submit_btn_el.get_attribute('name'))
time.sleep(2)
submit_btn_el.click()