import time


def test1():
    print('test1')

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui
from PIL import Image
import pytesseract

def test2():
    wbc=webdriver.Chrome()
    wbc.get('http://www.jpress.cn/user/register')
    wbc.maximize_window()
    elem=wbc.find_element(By.ID,'agree')
    rect=elem.rect
    pyautogui.click(rect['x']+10,rect['y']+130)
    sleep(2)

#测试验证码
def test3():
    wbc=webdriver.Chrome()
    wbc.get('http://www.jpress.cn/user/register')
    wbc.maximize_window()
    t=time.time() #获取当前时间
    picture_name1=str(t)+'.png'
    wbc.save_screenshot(picture_name1)

    ce=wbc.find_element(By.XPATH,'//*[@id="captchaimg"]')
    print(ce.location)
    left=ce.location['x']
    top=ce.location['y']
    right=ce.size['width']+left
    height=ce.size['height']+top

    im=Image.open(picture_name1)
    img=im.crop((left,top,right,height)) #抠图

    t=time.time()
    picture_name2=str(t)+'.png'
    img.save(picture_name2)

    sleep(2)
    wbc.close()

def test4():
    image1 = Image.open(1690378068.0561743.png)
    text = pytesseract.image_to_string(image1)
    print(text)