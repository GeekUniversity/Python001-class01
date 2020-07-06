# Author Andy Fang
# -*- coding:utf-8 -*-
from selenium import webdriver
import requests
import time
from os import path
try:
    brower = webdriver.Chrome("chromedriver.exe")
    url = 'https://shimo.im/welcome'
    brower.get(url)
    login_btn = brower.find_element_by_xpath('/html/body/div[1]/div[1]/header/nav/div[3]/a[2]/button')
    time.sleep(2)
    login_btn.click()
    brower.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('18017212522')
    time.sleep(4)
    brower.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('11111111111')
    time.sleep(5)
    submit_but = brower.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')
    submit_but.click()
    time.sleep(5)

except Exception as e:
    print(e)
finally:
    brower.close()
