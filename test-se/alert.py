#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#ec
def firefoxDriver():
    server = webdriver.Firefox()
    server.maximize_window()
    server.get("http://192.168.85.45:9090/admin/Login.aspx")
    
    username_loc = (By.ID,"userName")
    WebDriverWait(server,10).until(EC.presence_of_all_elements_located(username_loc))
    server.find_element(*username_loc).send_keys('12176')
    server.find_element(By.ID,"userPwd").send_keys('12336')
    print('密码为：',server.find_element(By.ID,"userPwd").get_attribute("value"))
    sleep(1)
    server.find_element(By.ID, "btnSubmit").click()
    '''
    使用switch_to.alert切换到alert
    '''
    sleep(2)
    alert = server.switch_to.alert
    print(alert.text)
    alert.accept()


    ''' 使用WebDriverWait获取alert
    alert = WebDriverWait(server,10).until(EC.alert_is_present())
    #获取弹框信息
    msg = alert.text
    print(msg)
    sleep(2)
    alert.accept() #点击确定
    #alert.dismiss()  #点击取消
    #alert.send_keys("")  #输入内容
    #alert.text  #获取弹框信息
    '''
    sleep(2)
    
    server.find_element(By.ID,"userPwd").clear()
    server.find_element(By.ID,"userPwd").send_keys('123456')
    server.find_element(By.ID, "btnSubmit").click()
    
    sleep(6)
    server.quit()
firefoxDriver()