from  selenium import webdriver
import time
from enum import Enum

from selenium.common.exceptions import WebDriverException, NoSuchElementException

driver = webdriver.Firefox(executable_path=r'C:\Users\OTHMANE\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe')

class Category(Enum):
    economiques = 1
    entreprises = 2

def open(i):
    cat=Category(i).name
    driver.get('https://laquotidienne.ma/articles/actualites-'+cat)



def scraping(k):
    for i in range(0,k):
        driver.get(urls[i])
        time.sleep(3)
        globals()['text{0}'.format(i)] = []
        try:
            pars = driver.find_elements_by_xpath('//div[@class="contenu_desc"]/p/span/span')
            for p in pars:
                eval('text' + str(i)).append(p.text)
        except WebDriverException:
            driver.refresh()
            time.sleep(4)
            try:
                pars = driver.find_elements_by_xpath('//div[@class="contenu_desc"]/p/span/span')
                for p in pars:
                    eval('text' + str(i)).append(p.text)
            except NoSuchElementException:
                continue
        except NoSuchElementException:
            continue



urls=[]
titles=[]
dates=[]
def scroll(i,n):
    cat = Category(i).name
    driver.get('https://laquotidienne.ma/articles/actualites-' + cat)
    time.sleep(5)

    for p in range(2,n+1):
        headers=driver.find_elements_by_xpath('//div[@class="list_article_detail"]/h2/a')
        for h in headers:
            titles.append(h.text)
            urls.append(h.get_attribute('href'))
        dt=driver.find_elements_by_xpath('//div[@class="list_article_detail"]/h2/a/span')
        for d in dt:
            dates.append(d.text)
        time.sleep(5)
        elem=driver.find_element_by_xpath('//li/a[@href="/articles/actualites-'+cat+'/'+str(p)+'"]')
        driver.execute_script("arguments[0].click();", elem)
        time.sleep(5)
    scraping(len(urls))

scroll(1,10)