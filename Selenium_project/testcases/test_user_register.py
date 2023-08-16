from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util
import pyautogui

class TestUserRegister(object):
    def __init__(self):
        self.wbc=webdriver.Chrome()
        self.wbc.get('http://localhost:8080/jpress/user/register')
        self.wbc.maximize_window()

        #测试登录验证码错误
    def test_register_code_error(self):
        username='test001'
        email='test001@qq.com'
        pwd='123456'
        confirmPwd='123456'
        captcha='666'
        expected='验证码不正确'
        self.wbc.find_element(By.NAME,'username').send_keys(username)
        self.wbc.find_element(By.NAME,'email').send_keys(email)
        self.wbc.find_element(By.NAME,'pwd').send_keys(pwd)
        self.wbc.find_element(By.NAME,'confirmPwd').send_keys(confirmPwd)
        self.wbc.find_element(By.NAME,'captcha').send_keys(captcha)
        elem =self.wbc.find_element(By.ID, 'agree')
        rect = elem.rect
        pyautogui.click(rect['x'] + 10, rect['y'] + 130)
        self.wbc.find_element(By.XPATH,'/html/body/main/div/div/form/div[7]/button').click()

        WebDriverWait(self.wbc,5).until(EC.alert_is_present())
        alert=self.wbc.switch_to.alert

        assert alert.text==expected
        alert.accept()

        sleep(5)

        #注册成功
    def test_register_ok(self):
        username=util.get_random_str()
        email=username+'@qq.com'
        pwd='123456'
        confirmPwd='123456'
        captcha=''
        expected='注册成功，点击确认并登录'

        self.wbc.find_element(By.NAME, 'username').clear()
        self.wbc.find_element(By.NAME,'username').send_keys(username)
        self.wbc.find_element(By.NAME, 'email').clear()
        self.wbc.find_element(By.NAME,'email').send_keys(email)
        self.wbc.find_element(By.NAME, 'pwd').clear()
        self.wbc.find_element(By.NAME,'pwd').send_keys(pwd)
        self.wbc.find_element(By.NAME, 'confirmPwd').clear()
        self.wbc.find_element(By.NAME,'confirmPwd').send_keys(confirmPwd)
        captcha=util.get_code(self.wbc,'//*[@id="captchaimg"]')
        self.wbc.find_element(By.ID, 'captcha').clear()
        self.wbc.find_element(By.ID,'captcha').send_keys(captcha.upper())
        elem = self.wbc.find_element(By.ID, 'agree')
        rect = elem.rect
        pyautogui.click(rect['x'] + 10, rect['y'] + 130)
        self.wbc.find_element(By.XPATH,'/html/body/main/div/div/form/div[7]/button').click()

        #等等alert出现
        WebDriverWait(self.wbc, 5).until(EC.alert_is_present())
        alert = self.wbc.switch_to.alert
        sleep(999)
        #验证
        assert alert.text == expected
        alert.accept()

