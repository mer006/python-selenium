from selenium import webdriver
from time import sleep


def firefoxDriver():
    server = webdriver.Firefox(executable_path="D:/app/firefox/geckodriver.exe")
    server.get("https://www.baidu.com")
    sleep(3)
    server.quit()