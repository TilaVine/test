import ddddocr
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# 打开网页
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')

driver.maximize_window()
print(driver.find_element(By.XPATH, '//*[@id="login_pictures"]/div[2]/p[1]').text)
driver.switch_to.frame('login_frame')
driver.find_element(By.ID,'switcher_plogin').click()
sleep(3)
#
# class Solution:
#     def circularGameLosers(self, n: int, k: int):
#         v=[False]*n
#         m=[]
#         i=0
#         d=k
#         b=False
#         while not v[i]:
#             v[i]=True
#             i=(i+d)%n
#             d+=k
#         for x in range(len(v)):
#             if(v[x]!=True):
#                 m.append(x+1)
#         print(m)
#         return m
# if __name__ == '__main__':
#     S=Solution()
#     S.circularGameLosers(4,4)


