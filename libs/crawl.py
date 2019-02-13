import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

#options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size=1920x1080')
#options.add_argument("disable-gpu")



def getPageStr(pageNo):
    driver = webdriver.Chrome('C:/chromedriver/chromedriver')

    driver.implicitly_wait(3)

    driver.get('http://soramall.net/shop/main/intro_adult.php')

    driver.find_element_by_name('m_id').send_keys('kensiro12')
    driver.find_element_by_name('password').send_keys('k12345')
    driver.find_element_by_name('password').send_keys(Keys.ENTER)


    #driver.implicitly_wait(3)
    #driver.get_screenshot_as_file("test-web02.png")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="container"]/div[1]/nav/ul/li[9]/a').click()


    base_url = 'http://soramall.net/shop/goods/goods_list.php?np={}&sp=1&category=022&sort=hit&order=desc'
    url = base_url.format(pageNo)
    driver.get(url)
    html = driver.page_source

    return html

    #driver.quit()

'''
    driver.get('http://soramall.net/shop/goods/goods_list.php?np=2&sp=1&category=022&sort=hit&order=desc')
    html = driver.page_source

    return html

    driver.quit()
'''

