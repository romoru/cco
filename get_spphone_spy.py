import sys
import lxml.html
import requests
from selenium import webdriver

dis = {
    'ASUS':'https://www.asus.com/jp/Phone/ZenFone-Products/'
    ,'SONY':'https://www.sonymobile.co.jp/xperia/'
}


target_url = dis["ASUS"]
driver = webdriver.PhantomJS()
driver.get(target_url)
print (driver.page_source)
# root=lxml.html.formstring(driver.page_source)
# links=root.cssselect()


