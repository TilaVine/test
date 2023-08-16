import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass...')
        cls.wbc=webdriver.Chrome()
        cls.wbc.get('http://www.baidu.com')
        cls.wbc.maximize_window()
    def setUp(self) -> None:
        print('setup....')

    def tearDown(self) -> None:
        print('tearDown....')

    def test01(self):
        self.wbc.find_element(By.ID,'kw').send_keys('美秀集团')
        sleep(3)
        print('test01')

    def test02(self):
        print('test02')



    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass....')
        cls.wbc.quit()

if __name__ == '__main__':
    unittest.main()