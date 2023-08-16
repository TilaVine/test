from style import Style
from selenium import webdriver
from time import sleep


class SearchPage(Style):
    url='http://www.baidu.com'
    input_el=('id','kw')
    click_el=('id','su')

    def search(self,txt):
        self.open(self.url)
        self.input(*self.input_el,txt=txt)
        self.click(*self.click_el)
        sleep(3)


if __name__ == '__main__':
    sp=SearchPage(webdriver.Chrome())
    sp.search('美秀集团')