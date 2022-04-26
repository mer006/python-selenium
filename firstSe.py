from unittest import result
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import re


def firefoxDriver():
    server = webdriver.Firefox()
    server.maximize_window()
    server.get("http://192.168.85.45:9091/Account/Login")
    server.find_element(By.ID,"username").send_keys('160601')
    server.find_element(By.ID,"password").send_keys('123456')
    server.find_element(By.ID, "btnSubmit").click()
    sleep(3)
    assert server.page_source

    mainwindow = server.current_window_handle
    print(server.current_url)
    print('mainwindow',mainwindow)
    server.find_element(By.XPATH,"//*[div='绩效管理']").click()
    server.find_element(By.XPATH,"//*[@id='_easyui_tree_6']").click()
    #print(server.page_source)
    print(server.current_url)

    #定位到iframe
    iframe = server.find_element(By.XPATH,"//*[@id='_panel_/SalePerformance/BasePerformance/Index']/iframe")
    server.switch_to.frame(iframe)
    print(server.current_window_handle)
    print(server.page_source)
    server.find_element(By.XPATH, "//*[@id='_easyui_textbox_input2']").send_keys('ZH06')

    sleep(3)
    server.quit()

firefoxDriver()