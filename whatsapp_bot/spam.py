from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

chrome =webdriver.Chrome(ChromeDriverManager().install())

chrome.get("https://web.whatsapp.com/")
time.sleep(15)
print("scan is complete")
search_box = chrome.find_element_by_class_name("_2_1wd")
search_box.send_keys("search the grp or person u want to spam")
search_box.send_keys(Keys.ENTER)

'''message_box = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
message_box.send_keys("hello")
message_box.send_keys(Keys.ENTER)'''

for i in range(0,10000):
    message_box = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    message_box.send_keys("message u want to spam")
    message_box.send_keys(Keys.ENTER)

    #  emoji=[":-)"]