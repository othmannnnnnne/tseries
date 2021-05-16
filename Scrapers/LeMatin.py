from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
from enum import Enum
driver = webdriver.Firefox(executable_path=r'C:\Users\OTHMANE\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe')


class Category(Enum):

    actu = 1
    entreprise = 2
    analyse = 3


def open(i):
    cat = Category(i).name
    driver.get('http://lematin.ma/journal/eco-'+cat)

#open(3)


def headers(i,n):
    cat = Category(i).name
    driver.get('http://lematin.ma/journal/eco-' + cat)
    for p in range(2,n):
        url="https://lematin.ma/journal/eco-"+cat+"/"+str(p)
        driver.get(url)
        time.sleep(3)

#headers(3,10)

#summ=[]
##def article(uri):

#   driver.get(uri)
#   time.sleep(5)
#   subs = driver.find_element_by_xpath('//article[@class="card p-1 mb-2"]/h4')
#   summ.append(subs.text)
#   driver.back

#def createList(i):
#globals()['text{0}'.format(i)] = []
#return eval('text'+str(i))

def scrap_text(i):
    globals()['text{0}'.format(i)] = []
    pars = driver.find_elements_by_xpath('//main[@role="article"]/article/div/p')
    for p in pars:
        try:
            eval('text' + str(i)).append(p.text)
        except NoSuchElementException:
            try:
                eval('text' + str(i)).append(p.strong.text)
            except NoSuchElementException:
                continue


summaries = []
authors = []
dates=[]
def articles():
    k=0
    for uri in urls:
        driver.get(uri)
        time.sleep(3)
        try:
            subs = driver.find_element_by_xpath('//article[@class="card p-1 mb-2"]/h4')
            summaries.append(subs.text)
        except NoSuchElementException:
            time.sleep(5)
            driver.get(uri)
            time.sleep(10)
            try:
                subs = driver.find_element_by_xpath('//article[@class="card p-1 mb-2"]/h4')
                summaries.append(subs.text)
            except NoSuchElementException:
                continue

        datetime = driver.find_element_by_xpath('//p[@class="author"]/time')
        dates.append(datetime.text)
        try:
            auth = driver.find_element_by_xpath('//p[@class="author"]/span/a')
            authors.append(auth.get_attribute('title'))
            if authors[-1] == '':
                authors.pop()
                aut = driver.find_element_by_xpath('//p[@class="author"]/span/a/img')
                authors.append(aut.get_attribute('alt'))

        except NoSuchElementException:
            authors.append("none")
        time.sleep(1)
        scrap_text(k)
        k=k+1

urls=[]
def scraper():
    liens = driver.find_elements_by_xpath('//div[@class="card h-100"]/a')
    for l in liens:
        try:
            urls.append(l.get_attribute("href"))
            time.sleep(1)
        except StaleElementReferenceException:
            urls.append('NA')
    liens2 = driver.find_elements_by_xpath('//div[@class="card h-100 bg-dark text-white"]/a')
    for j in liens2:
        urls.append(j.get_attribute("href"))
        time.sleep(1)



titles = []
def scroll(i,n):
    cat = Category(i).name
    driver.get('http://lematin.ma/journal/eco-' + cat)
    for p in range(2,n+1):
        header = driver.find_elements_by_class_name("card-title-2")
        header4 = driver.find_elements_by_xpath('//div[@class="card-img-overlay"]/h4')
        for h in header:
            titles.append(h.text)
        for j in header4:
            titles.append(j.text)
        scraper()
        time.sleep(10)
        elem=driver.find_element_by_xpath('//li/a[@href="/journal/eco-'+cat+'/'+str(p)+'/"]')
        driver.execute_script("arguments[0].click();", elem)
        time.sleep(6)

    articles()


scroll(3,3)