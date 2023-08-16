from selenium import webdriver
from style import Style
from  time import sleep

class LoginWyy(Style):
    url='https://graph.qq.com/oauth2.0/show?which=Login&display=pc&client_id=100495085&response_type=code&redirect_uri=https://music.163.com/back/qq&X-loginMethod=QQ&forcelogin=true&state=qdtzcNmLRu&checkToken=9ca17ae2e6ffcda170e2e6eea8e8538db2a3dab567a2ac8ab3d14a928a9f86c43cb6eb858ce75ef8afe5a8ed2af0feaec3b92ab2a8a3afe642baf1bcccdc4f928b9aa3c54f899fffd0b75cb5879db9d67da3efee9e'
    usr=('id','u')
    pwd=('id','p')
    click_el=('id','login_button')
    click_ell=('id','switcher_plogin')
    frame='ptlogin_iframe'


    def login(self,txt1,txt2):
        self.open(self.url)
        self.swichto_frame(self.frame)
        self.click(*self.click_ell)
        self.input(*self.usr,txt=txt1)
        self.input(*self.pwd,txt=txt2)
        self.click(*self.click_el)
        sleep(10)


if __name__ == '__main__':
    lw=LoginWyy(webdriver.Chrome())
    lw.login('1602122538','z326gd...')

