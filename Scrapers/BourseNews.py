from enum import Enum
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException


class Category(Enum):
    evenements = 1
    apprendre = 2
    decryptage = 3
    maroc = 4

driver = webdriver.Firefox(executable_path=r'C:\Users\OTHMANE\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe')

def open(i):
    cat=Category(i).name
    driver.get('https://www.boursenews.ma/articles/'+cat)

#open(1)
def scraper(k):
    for i in range(0,k):
        driver.get(urls[i])
        time.sleep(3)
        globals()['text{0}'.format(i)] = []
        try:
            par=driver.find_element_by_xpath('//div[@class="article_detail_description"]/h2/strong')
            eval('text' + str(i)).append(par.text)
        except WebDriverException:
            driver.refresh()
            time.sleep(4)
        except NoSuchElementException:
            continue
        pars = driver.find_elements_by_xpath('//div[@class="article_detail_description"]/p/span/span')
        for d in pars:
            eval('text' + str(i)).append(d.text)

urls=[]
titles=[]
dates=[]
def scroll(i,n):
    cat=Category(i).name
    driver.get('https://www.boursenews.ma/articles/'+cat)
    time.sleep(3)
    for p in range(2,n+1):
        headers=driver.find_elements_by_xpath('//div[@class="col-xs-12 col-sm-12 col-md-8 col-lg-8"]/h3/a')
        for h in headers:
            titles.append(h.text)
            ref=h.get_attribute('href')
            urls.append(ref)
            datetime=h.find_element_by_tag_name('span')
            dates.append(datetime.text)

        time.sleep(5)
        elem=driver.find_element_by_xpath('//li/a[@href="/articles/'+cat+'/'+str(p)+'"]')
        driver.execute_script("arguments[0].click();", elem)
        time.sleep(5)
    scraper(len(urls))


scroll(4,4)