#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By

#ec
def firefoxDriver():
    server = webdriver.Firefox()
    server.maximize_window()
    server.get("http://192.168.85.45")
    server.maximize_window()
    sleep(2)
    ECtest_link_loc = (By.XPATH,'//span[text()="EC测试"]')
    WebDriverWait(server,20).until(EC.presence_of_all_elements_located(ECtest_link_loc))
    #点击EC测试链接url
    server.find_element(*ECtest_link_loc).click()
    print('当前url：'+server.current_url)
    print(server.current_window_handle)
    sleep(3)
    handlers = server.window_handles
    #切换到最后一个窗口，即新打开的窗口
    server.switch_to.window(handlers[-1])
    print(server.current_url)
    print(server.current_window_handle)
    sleep(2)
    server.find_element(By.ID,"userName").send_keys('160601')
    sleep(2)
    server.quit()

firefoxDriver()