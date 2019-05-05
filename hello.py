from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Firefox()
driver.get('https://www.championat.com/football/_russiapl/tournament/2599/table/')
print("done")

name_1 = list()
score_1 = list()
a=0
m = 0
while a<16:

        a = a + 1
        n = driver.find_elements_by_xpath('//span[@class="table-item__name"]')[m].text
        name_1.append(n)
        s = driver.find_elements_by_xpath('//td[@class="result-table__points _center"]/strong')[m].text
        score_1.append(s)
        m = m + 1
        
df = pd.DataFrame({'name': name_1 ,'score': score_1})
df.to_csv('FootBall.csv', index=False, encoding='utf-8')
print(df)

driver.quit()
