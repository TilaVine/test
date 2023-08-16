from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class BasePage(object):
    def __init__(self,wbc):
        self.wbc=wbc

    def get_element(self,*loc):
        return self.wbc.find_element(*loc)

    def input_text(self,text,*loc):
        self.get_element(*loc).send_keys(text)

    def click(self,*loc):
        self.wbc.find_element(*loc).click()

    def get_title(self):
        return self.wbc.title

class BaiDuPage(BasePage):
    def __init__(self,wbc):
        BasePage.__init__(self,wbc)
        wbc.get('http://www.baidu.com')

    def test_search(self):
        loc=(By.ID,'kw')
        loc2=(By.ID,'su')
        self.input_text('美秀集团',*loc)
        self.click(*loc2)
        sleep(5)

if __name__ == '__main__':
    wbc=webdriver.Chrome()
    wbc.maximize_window()
    baiduPage=BaiDuPage(wbc)
    baiduPage.test_search()
