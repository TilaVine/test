from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from time import sleep

class TestBaiDu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.wbc=webdriver.Chrome()
        cls.wbc.maximize_window()


    def test_baidu(self):
        self.wbc.get('http://www.baidu.com')
        self.wbc.find_element(By.ID,'kw').send_keys('selenium')
        self.wbc.find_element(By.ID,'su').click()
        sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.wbc.quit()

if __name__ == '__main__':
    unittest.main()