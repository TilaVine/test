from  testcases import testcase1
from util import util
from selenium import webdriver
from testcases.test_user_register import TestUserRegister
from testcases.test_user_login import TestUserLogin
from wyy_music_login import WyyLogin


if __name__ =='__main__':
    # wbc=webdriver.Chrome()
    # wbc.get('http://www.jpress.cn/user/register')
    # util.get_code(wbc,'//*[@id="captchaimg"]')
    # case=TestUserRegister()
    # case.test_register_code_error()
    # case.test_register_ok()
    # case=testcase1
    # case.test2()
    # case=TestUserLogin()
    # case.test_user_login_ok()
    # case1=TestUserLogin()
    # case1.test_user_login_ok()
    case=WyyLogin()
    case.get_url('https://music.163.com/')
