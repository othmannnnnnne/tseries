from selenium import webdriver
import time
from enum import Enum

from selenium.common.exceptions import WebDriverException, NoSuchElementException

driver = webdriver.Firefox(executable_path=r'C:\Users\OTHMANE\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe')

class Category(Enum):
    entreprises = 1
    economie = 2

def open(i):
    cat = Category(i).name
    driver.get('https://www.medias24.com/economie/'+cat+'.html')

#open(2)

def scraper(k):
    for i in range(0,k):
        driver.get(urls[i])
        time.sleep(3)
        globals()['text{0}'.format(i)] = []
        try:
            pars = driver.find_elements_by_xpath('//div[@class="chapo-options"]/div/p')
            for par in pars:
                eval('text' + str(i)).append(par.text)
        except WebDriverException:
            driver.refresh()
            time.sleep(4)
            try:
                pars = driver.find_elements_by_xpath('//div[@class="chapo-options"]/div/p')
                for par in pars:
                    eval('text' + str(i)).append(par.text)
            except NoSuchElementException:
                continue
        except NoSuchElementException:
            continue
        try:
            pars = driver.find_elements_by_xpath('//div[@class="chapo-options"]/p')
            for par in pars:
                eval('text' + str(i)).append(par.text)
        except NoSuchElementException:
            continue


titles=[]
urls=[]
dates=[]
def scroll(i,n):
    cat=Category(i).name
    driver.get('https://www.medias24.com/economie/'+cat+'.html')
    time.sleep(7)
    button=driver.find_element_by_xpath('//div[@class="mc-closeModal"]')
    driver.execute_script("arguments[0].click();", button)

    for p in range(2,n+1):
        headers=driver.find_elements_by_xpath('//h2[@class="titre"]')
        for h in headers:
            titles.append(h.text)
        links=driver.find_elements_by_xpath('//article/div[@class="text-zone"]/a')
        for l in links:
            urls.append(l.get_attribute('href'))
        dt=driver.find_elements_by_xpath('//p[@class="meta-date"]/span/i')
        for d in dt:
            dates.append(d.text)

        time.sleep(3)
        elem=driver.find_element_by_xpath('//li[@class="pagination-next"]/a')
        driver.execute_script("arguments[0].click();", elem)
        time.sleep(3)

    scraper(len(urls))



scroll(1,10)