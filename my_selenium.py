import time

from selenium import  webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

path ='C:\\Users\\bitcamp\\____\\jarvis\\crolling\\data'
chromdriver = 'C:\\Users\\bitcamp\\____\\jarvis\\crolling\\data\\chromedriver.exe'


class MySelenium(object):
    def __init__(self):
        self.driver = webdriver.Chrome(chromdriver)


    def velog(self):
        driver = self.driver
        searchname = '개발일기'
        diary = []
        driver.get('https://velog.io/@kisy324')
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        user = soup.find('div', {'class':'sc-tilXH hRLnHq'})
        u = driver.find_elements_by_css_selector('#root > div.sc-jlyJG.bbyJzT.sc-gipzik.cmNMNC > div.sc-cHGsZl.gWOoyb.sc-hrWEMg.fOsrtz > div:nth-child(4) > div.sc-dqBHgY.dDPIoV > div > div:nth-child(3) > p')
        # u = driver.find_elements_by_xpath('//*[@id="root"]/div[2]/div[3]/div[4]/div[3]/div/div[3]/p')
        # a = driver.find_elements_by_css_selector('#root > div.sc-jlyJG.bbyJzT > div.sc-cHGsZl.gWOoyb.sc-TOsTZ.cjdTHz > div.sc-jqCOkK.heXNii > div:nth-child(1) > div.user-info > a > img')
        # a.click()
        print(user)
        print(u)
        # blog = soup.find_all('p', attrs={'class': 'sc-jbKcbu jXsEWL'})
        # driver.find_element_by_class_name('sc-kgAjT cLKEkd sc-cJSrbW heneQz').send_keys('개발일기')
        # search = driver.find_element_by_css_selector('#root > div.sc-jlyJG.bbyJzT > div.sc-cHGsZl.gWOoyb.sc-hmXxxW.jTiCaz > div > div > input')
        # search = driver.find_element_by_class_name('#root > div.sc-jlyJG.bbyJzT > div.sc-cHGsZl.gWOoyb.sc-iSDuPN.fdvsQb > div > div > input')
        # driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/div/input').send_keys('개발일기')
        # sel = pre_in.find_element_by_tag_name('placeholder').send_keys('개발일기')
        # sel.send_key(Keys.RETURN)
        # driver.implicitly_wait(time_to_wait=10)
        # driver.close()
        # select = Select(pre_in.find_element_by_tag_name('value'))
        # sel = select.select_by_value(value='개발일기')
        # print(sel)
        # soup = BeautifulSoup(driver.page_source, 'html.parser')
        # all_divs = soup.find_all('개발일기', attrs={'input'})
        # print(all_divs)

if __name__ == '__main__':
    sel =MySelenium()
    sel.velog()

