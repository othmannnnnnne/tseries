from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException, WebDriverException

driver = webdriver.Firefox(executable_path=r'C:\Users\OTHMANE\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe')

def open():
    driver.get('https://www.h24info.ma/economie/entreprises/')

def scraper(k):
    for i in range(0,k):
        driver.get(urls[i])
        time.sleep(3)
        globals()['text{0}'.format(i)] = []
        try :
            par = driver.find_element_by_xpath('//div[@class="td-post-content tagdiv-type cf-tweet-this cf-tt-target cf-tt-abutted cf-tt-abutted-top cf-tt-out-of-bounds cf-tt-out-of-bounds-top cf-tt-element-attached-bottom cf-tt-element-attached-center cf-tt-target-attached-top cf-tt-target-attached-center"]/p/strong')
            eval('text' + str(i)).append(par.text)

        except WebDriverException:
            driver.refresh()
            time.sleep(5)
            try:
                par = driver.find_element_by_xpath('//div[@class="td-post-content tagdiv-type cf-tweet-this cf-tt-target cf-tt-abutted cf-tt-abutted-top cf-tt-out-of-bounds cf-tt-out-of-bounds-top cf-tt-element-attached-bottom cf-tt-element-attached-center cf-tt-target-attached-top cf-tt-target-attached-center"]/p/strong')
                eval('text' + str(i)).append(par.text)
            except NoSuchElementException:
                continue
        except NoSuchElementException:
            continue
        try :
            pars = driver.find_elements_by_xpath('//div[@class="td-post-content tagdiv-type cf-tweet-this cf-tt-target cf-tt-abutted cf-tt-abutted-top cf-tt-out-of-bounds cf-tt-out-of-bounds-top cf-tt-element-attached-bottom cf-tt-element-attached-center cf-tt-target-attached-top cf-tt-target-attached-center"]/p')
            for p in pars:
                eval('text' + str(i)).append(par.text)
        except NoSuchElementException:
            continue



dates=[]
urls=[]
titles=[]
def scroll(n):
    open()
    time.sleep(3)
    for p in range(2,n+1):
        headers = driver.find_elements_by_xpath('//div[@class="td_module_14 td_module_wrap td-animation-stack"]/div/div/div/h1/a')
        for h in headers:
            titles.append(h.get_attribute('title'))
            urls.append(h.get_attribute('href'))
        dt = driver.find_elements_by_xpath('//div[@class="td_module_14 td_module_wrap td-animation-stack"]/div/div/div/span/time')
        for d in dt:
            dates.append(d.text)

        time.sleep(3)
        driver.get('https://www.h24info.ma/economie/entreprises/page/'+str(p))
        time.sleep(4)

    scraper(len(urls))



scroll(10)