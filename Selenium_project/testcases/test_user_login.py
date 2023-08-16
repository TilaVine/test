from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util
import logging

class TestUserLogin(object):
    def __init__(self):
        self.wbc=webdriver.Chrome()
        # self.wbc.get('http://www.jpress.cn/user/login')
        self.wbc.get('http://localhost:8080/jpress/user/login')
        self.wbc.maximize_window()
        self.logger=util.get_logger()
        self.logger.info('测试用户登录')

    def test_user_login_username_error(self):
        username=''
        pwd='123456'
        expected='账号不能为空'

        self.wbc.find_element(By.NAME,'user').send_keys(username)
        self.logger.debug('输入用户名称:%s',username)
        self.wbc.find_element(By.NAME,'pwd').send_keys(pwd)
        self.logger.debug('输入用户密码:%s', pwd)
        self.wbc.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/div/form/div[4]/div/button').click()
        self.logger.debug('点击登录')

        WebDriverWait(self.wbc,5).until(EC.alert_is_present())
        alert=self.wbc.switch_to.alert
        sleep(3)
        try:
            assert alert.text==expected
        except AssertionError as ae:
            self.logger.error('报错啦:%s',exc_info=1)
        alert.accept()

        self.wbc.quit()


    def test_user_login_ok(self):
        username='admin'
        pwd='123456'
        captcha = ''
        expected='用户中心'
        self.wbc.find_element(By.NAME, 'user').clear()
        self.wbc.find_element(By.NAME,'user').send_keys(username)
        self.logger.debug('输入用户名称:%s', username)
        self.wbc.find_element(By.NAME, 'pwd').clear()
        self.wbc.find_element(By.NAME,'pwd').send_keys(pwd)
        self.logger.debug('输入用户密码:%s', pwd)
        captcha = util.get_code(self.wbc, '//*[@id="captcha-img"]')
        self.wbc.find_element(By.ID, 'captcha').send_keys(captcha.upper())
        self.wbc.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/div/form/div[4]/div/button').click()

        WebDriverWait(self.wbc, 5).until(EC.alert_is_present())
        sleep(3)
        assert self.wbc.title==expected
        self.wbc.quit()