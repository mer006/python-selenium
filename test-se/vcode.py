#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import ddddocr

'''
获取动态图形验证码
1.定位图形验证码元素
2.使用screenshot方法将验证码截图
3.将图片亮度对比度调高以提高识别精准度使用PIL库  --没做
4.使用ddddocr第三方库识别验证码
'''
#ec
def firefoxDriver():
    image_path = 'C:/Users/12176/Desktop/_VerifyCode.jpg'
    server = webdriver.Firefox()
    server.maximize_window()
    server.get("http://192.168.85.45:8082/Account/FindPassword")
    sleep(1)
    server.maximize_window()
    sleep(2)
    #定位到动态图形验证码图片
    image = server.find_element(By.XPATH,'//img[@id="icode"]')
    #将图形码截图保存到image_path
    image.screenshot(image_path)

    #使用第三方库ddddocr识别图形码字符
    ocr = ddddocr.DdddOcr()
    with open(image_path,'rb') as f:
        image_bytes = f.read()
    icode = ocr.classification(image_bytes)
    print('icode:',icode)
    sleep(3)
    server.quit()

firefoxDriver()
