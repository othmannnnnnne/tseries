from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException, WebDriverException

driver = webdriver.Firefox(executable_path=r'C:\Users\OTHMANE\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe')


def open():
    driver.get('https://www.lavieeco.com/economie/')

def scraping(k):
    for i in range(0,k):
        driver.get(urls[i])
        time.sleep(2)
        globals()['text{0}'.format(i)] = []
        try:
            par = driver.find_element_by_xpath('//div[@class="single-post-excerpt post-excerpt-bc"]/p')
            eval('text'+str(i)).append(par.text)
        except WebDriverException:
            driver.refresh()
            time.sleep(4)
            try:
                par = driver.find_element_by_xpath('//div[@class="single-post-excerpt post-excerpt-bc"]/p')
                eval('text' + str(i)).append(par.text)
            except NoSuchElementException:
                continue
        except NoSuchElementException:
            continue

        try:
            pars=driver.find_element_by_xpath('//div[@class="entry-content clearfix single-post-content"]/p')
            eval('text'+str(i)).append(pars.text)
        except NoSuchElementException:
            continue

titles=[]
urls=[]
dates=[]

def scroll(n):
    open()
    time.sleep(3)
    for p in range(2,n+1):
        elem = driver.find_element_by_xpath('//span[@class="loaded icon"]')
        driver.execute_script("arguments[0].click();", elem)
        time.sleep(2)
    headers = driver.find_elements_by_xpath('//a[@class="post-title post-url"]')
    for h in headers:
        titles.append(h.text)
        urls.append(h.get_attribute('href'))
    dt = driver.find_elements_by_xpath('//time[@class="post-published updated"]')
    for d in dt:
        dates.append(d.text)

    scraping(len(urls))



scroll(2)