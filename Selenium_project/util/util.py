import pickle
import random
import string
import time
from PIL import Image
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
import logging
import logging.handlers
import datetime


def get_code(wbc,xpath):
    # wbc=webdriver.Chrome()
    # wbc.get('')
    # t=time.time()
    # path=os.path.dirname(os.path.dirname(__file__))+'\\screenshots'
    # picture_name1=path+'\\'+str(t)+'.png'
    #
    # wbc.save_screenshot(picture_name1)
    # ce=wbc.find_element(By.ID,id)
    # left=ce.location['x']
    # top=ce.location['y']
    # right=ce.size['width']+left
    # height=ce.size['height']+top
    #
    # im=Image.open(picture_name1)
    # img=im.crop(left,top,right,height)
    #
    # t = time.time()
    # picture_name2 = path+'\\'+str(t) + '.png'
    # img.save(picture_name2)

    # driver = webdriver.Chrome()
    # driver.get('http://www.jpress.cn/user/register')k
    # driver.implicitly_wait(5)

    # 获取验证码元素
    pic_ele = wbc.find_element(By.XPATH,xpath)

    # 使用DdddOcr识别验证码
    ocr = ddddocr.DdddOcr()
    text = ocr.classification(pic_ele.screenshot_as_png)
    return text

def get_random_str():
    rand_str=''.join(random.sample(string.ascii_letters+string.digits,8))
    return rand_str

def save_cookie(wbc,path):
    with open(path,'wb') as filehandler:
        cookies=wbc.get_cookies()
        print(cookies)
        pickle.dump(cookies,filehandler)

def load_cookies(wbc,path):
    with open(path,'rb') as cookiesfile:
        cookies=pickle.load(cookiesfile)
        for cookie in cookies:
            wbc.add_cookie(cookie)

def get_logger():
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0, ))
    rf_handler.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(message)s'))

    f_handler = logging.FileHandler('error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s[:(lineno)d]-%(message)s'))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger