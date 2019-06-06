from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import lxml.etree as LE
import requests
import time
import pandas as pd

driver = webdriver.Firefox()
driver.get('https://coinmarketcap.com/')

name = list()
website = list()
a=0
m = 0
while a<11:

        a = a + 1
        
        
        try:
                driver.find_elements_by_xpath('//button[@class="banner-alert-close-button js-close"]')[0].click()
        except:
                pass
        driver.find_elements_by_xpath('//a[@class="currency-name-container link-secondary"]')[m].click()
        name_1 = driver.find_elements_by_xpath('//span[@class="text-bold h3 text-gray text-large"]')[0].text
        name.append(name_1)
        try:
                for link in driver.find_elements_by_xpath('//a[contains(text(),"Source Code")]'):
                        link_1 = link.get_attribute('href')
        except:
                driver.get('https://coinmarketcap.com/')
                for link_1 in driver.find_elements_by_xpath('//a[@class="currency-name-container link-secondary"]')[m]:
                        link_1 = link.get_attribute('href')
        
        website.append(link_1)
        m = m + 1
        driver.get('https://coinmarketcap.com/')


df = pd.DataFrame({'name': name ,'link': website})
df.to_csv('Criptonic.csv', index=False, encoding='utf-8')
print(df)

driver.quit()
