from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from time import sleep



def open_browser(type_):
    try:
       drive=getattr(webdriver,type_)()
    except Exception as e:
        print(e)
        drive=webdriver.Chrome()
    return drive

class Style:
    def __init__(self,type_):
        self.drive=open_browser(type_)
        self.drive.implicitly_wait(5)
        self.drive.maximize_window()


    def open(self,url):
        self.drive.get(url)

    def locate(self,name,value):
        return self.drive.find_element(name,value)

    def input(self,name,value,txt):
        self.locate(name,value).send_keys(txt)

    def click(self,name,value):
        self.locate(name,value).click()

    def quit(self):
        self.drive.quit()

    def sleep(self,time_):
        self.sleep(time_)

    def swichto_frame(self,value):
        self.drive.switch_to.frame(value)
