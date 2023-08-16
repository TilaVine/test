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

class BaiDuPage(object):
    def __init__(self,type_):
        self.wbc = open_browser(type_)
        self.wbc.maximize_window()
        self.input_element = (By.ID, 'kw')
        self.btn_element = (By.ID, 'su')

    def goto_baidu(self,url):
        self.wbc.get(url)

    def test_search(self,url,kw):
        self.goto_baidu(url)
        self.wbc.find_element(*self.input_element).send_keys(kw)
        self.wbc.find_element(*self.btn_element).click()
        sleep(5)

class TestBaiDu(unittest.TestCase):
    def setUp(self) -> None:
        self.baiduPage=BaiDuPage('Chrome')

    def test_search(self):
        self.baiduPage.test_search('http://www.baidu.com','美秀集团')


if __name__ == '__main__':
    unittest.main()