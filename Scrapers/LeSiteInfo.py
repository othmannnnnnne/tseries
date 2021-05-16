from selenium import webdriver
import time
from enum import Enum

from selenium.common.exceptions import WebDriverException, NoSuchElementException

driver = webdriver.Firefox(executable_path=r'C:\Users\OTHMANE\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe')


class Category(Enum):
    maroc = 1
    economie = 2

def open(i):
    cat = Category(i).name
    driver.get("https://www.lesiteinfo.com/"+cat)

#open(2)



def scraper(k):
    for i in range(0,k):
        driver.get(urls[i])
        globals()['text{0}'.format(i)] = []
        try:
            bloc = driver.find_element_by_class_name("entry-content entry clearfix")
            pars = bloc.find_elements_by_xpath('//p')
            for p in pars:
                eval('text' + str(i)).append(p.text)
        except WebDriverException:
            driver.refresh()
            time.sleep(5)
            try:
                bloc = driver.find_element_by_xpath('//div[@class="entry-content entry clearfix"]')
                pars = bloc.find_elements_by_tag_name('p')
                for p in pars:
                    eval('text' + str(i)).append(p.text)
            except NoSuchElementException:
                continue
        except NoSuchElementException:
            continue

urls=[]
titles=[]
def scroll(i,n):
    cat = Category(i).name
    driver.get("https://www.lesiteinfo.com/"+cat)
    time.sleep(3)

    for p in range(2,n+1):
        headers = driver.find_elements_by_xpath('//h2[@class="post-title"]/a')
        for h in headers:
            titles.append(h.text)
            urls.append(h.get_attribute('href'))

        time.sleep(4)
        elem=driver.find_element_by_xpath('//span[@class="last-page first-last-pages"]/a')
        driver.execute_script("arguments[0].click();", elem)
        time.sleep(3)

    scraper(len(urls))

scroll(2,2)