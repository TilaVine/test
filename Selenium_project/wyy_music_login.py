from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class WyyLogin(object):
    def __init__(self):
        self.wbc=webdriver.Chrome()

    def get_data(self):
        u = '1602122538'
        p = 'Z326gd...'
        return u,p
    def get_url(self,url):
        s=self.get_data()
        self.wbc.get(url)
        self.wbc.implicitly_wait(10)
        self.wbc.maximize_window()
        self.wbc.find_element(By.CSS_SELECTOR,'.link.s-fc3').click()
        self.wbc.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/div/div[2]/div/div/div/a').click()
        self.wbc.find_element(By.ID,'j-official-terms').click()
        self.wbc.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/div/div[2]/div/div/div/div[1]/div[2]/ul/li[2]/a').click()
        sleep(2)
        windows = self.wbc.window_handles
        self.wbc.switch_to.window(windows[1])
        self.wbc.switch_to.frame('ptlogin_iframe')
        self.wbc.find_element(By.XPATH,'//*[@id="switcher_plogin"]').click()
        self.wbc.find_element(By.ID,'u').send_keys(s[0])
        self.wbc.find_element(By.ID,'p').send_keys(s[1])
        self.wbc.find_element(By.ID,'login_button').click()
        sleep(5)
        # windowss=self.wbc.window_handles
        # self.wbc.switch_to.window(windowss[0])
        # self.wbc.switch_to.frame(3)
        # self.wbc.find_element(By.ID,'phoneipt').send_keys('13372627644')
        # self.wbc.find_element(By.CLASS_NAME,'j-power-btn tabfocus getsmscode ').click()
        sleep(20)
        self.wbc.quit()

