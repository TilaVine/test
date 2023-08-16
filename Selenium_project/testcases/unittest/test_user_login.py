from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util
import unittest
import pytest

class TestUserLogin(unittest.TestCase):
    # def __init__(self):
    #     self.wbc=webdriver.Chrome()
    #     # self.wbc.get('http://www.jpress.cn/user/login')
    #     self.wbc.get('http://localhost:8080/jpress/admin/login')
    #     self.wbc.maximize_window()

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass...')
        cls.wbc = webdriver.Chrome()
        cls.wbc.get('http://localhost:8080/jpress/admin/login')
        cls.wbc.maximize_window()

    def test_user_login_username_error(self):
        username=''
        pwd='123456'
        expected='账号不能为空'

        self.wbc.find_element(By.NAME,'user').send_keys(username)
        self.wbc.find_element(By.NAME,'pwd').send_keys(pwd)
        self.wbc.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/div/form/div[4]/div/div/button').click()

        WebDriverWait(self.wbc,5).until(EC.alert_is_present())
        alert=self.wbc.switch_to.alert
        sleep(3)
        assert alert.text==expected
        alert.accept()

        self.wbc.quit()


    def test_user_login_ok(self):
        username='admin'
        pwd='123456'
        captcha = ''
        expected='用户中心'

        self.wbc.find_element(By.NAME,'user').send_keys(username)
        self.wbc.find_element(By.NAME,'pwd').send_keys(pwd)
        captcha = util.get_code(self.wbc, '//*[@id="captcha-img"]')
        self.wbc.find_element(By.ID, 'captcha').send_keys(captcha.upper())
        self.wbc.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/div/form/div[4]/div/div/button').click()
        WebDriverWait(self.wbc, 5).until(EC.alert_is_present())
        sleep(3)
        assert self.wbc.title==expected
        self.wbc.quit()