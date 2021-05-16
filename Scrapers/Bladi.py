from selenium import webdriver
import time
from enum import Enum

from selenium.common.exceptions import WebDriverException, NoSuchElementException

driver = webdriver.Firefox(executable_path=r'C:\Users\OTHMANE\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe')

class Category(Enum):
    economie = 1
    maroc = 2

def open(i):
    cat=Category(i).name
    driver.get("https://www.bladi.net/"+cat+".html")

#open(1)

def scraper(k):
    for i in range(0,k):
        driver.get(urls[i])
        time.sleep(3)
        globals()['text{0}'.format(i)] = []
        try:
            pars = driver.find_elements_by_xpath('//div[@class="mtl mbm"]/p')
            for p in pars:
                eval('text'+str(i)).append(p.text)
        except WebDriverException:
            driver.refresh()
            driver.wait(5)
            try:
                pars = driver.find_elements_by_xpath('//div[@class="mtl mbm"]/p')
                for p in pars:
                    eval('text' + str(i)).append(p.text)
            except NoSuchElementException:
                continue
        except NoSuchElementException:
            continue

urls=[]
titles=[]
dates=[]
summaries=[]
def scroll(i,n):
    cat=Category(i).name
    driver.get("https://www.bladi.net/"+cat+".html")
    time.sleep(3)
    for p in range(1,n+1):
        headers = driver.find_elements_by_xpath('//div[@class="mbs "]/h2')
        for h in headers:
            titles.append(h.text)
        summs = driver.find_elements_by_xpath('//div[@class="mbs "]')
        for s in summs:
            summaries.append(s.text)
        links = driver.find_elements_by_xpath('//div[@class="grid3 "]/a')
        for l in links:
            urls.append(l.get_attribute('href'))
        dt = driver.find_elements_by_xpath('//div[@class="accueil"]/span')
        for d in dt:
            dates.append(d.text)

        time.sleep(5)
        elem = driver.find_element_by_xpath('//a[@href="'''+cat+'.html?debut_suite_rubrique='+str(p*12)+'#pagination_suite_rubrique"]')
        driver.execute_script("arguments[0].click();", elem)
        time.sleep(3)
    scraper(len(urls))

scroll(1,4)