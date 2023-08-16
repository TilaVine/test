import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Unittestt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.drive=webdriver.Chrome()
        cls.drive.get('http://www.baidu.com')
        cls.title=None

    @classmethod
    def tearDownClass(cls):
        cls.drive.quit()

    # def setUp(self):
    #     # self.drive=webdriver.Chrome()
    #     # self.drive.get('http://www.baidu.com')

    # def tearDown(self):
    #     self.drive.quit()

    def test_search01(self):
        input_=self.drive.find_element(By.ID,'kw')
        input_.send_keys('美秀集团')

        button=self.drive.find_element(By.ID,'su')
        button.click()
        Unittestt.title=self.drive.title
        self.assertEquals(self.title,'百度一下，你就知道',msg='断言失败')
        sleep(3)

    def test_search02(self):
        self.drive.find_element(By.ID,'kw').clear()
        input_ = self.drive.find_element(By.ID, 'kw')
        input_.send_keys('美秀集团贝斯')
        button = self.drive.find_element(By.ID, 'su')
        button.click()
        sleep(3)

if __name__ == '__main__':
    unittest.main()
