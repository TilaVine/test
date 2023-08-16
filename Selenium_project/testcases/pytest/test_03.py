import pytest
import allure_pytest



data=['123',456]

@pytest.mark.parametrize('pwd',data)
def test1(pwd):
    print(pwd)

#元组
data2=[(1,2,3),(4,5,6)]

@pytest.mark.parametrize('a,b,c',data2)
def test2(a,b,c):
    print(a,b,c)

#字典
data3=({'user':1,'pwd':2},{'age':3,'email':'zk@qq.com'})
@pytest.mark.parametrize('dic',data3)
def test3(dic):
    print(dic)75 82 187

#id的值可以自定义，只要方便理解每个用例是干什么的即可
data4=[
    pytest.param(1,2,3,id="(a+b):pass"),
    pytest.param(4,5,10,id="(a+b):fail")
]
def add(a,b):
    return a+b

class TestParametrize(object):
    @pytest.mark.parametrize('a,b,expect',data4)
    def test_parametrize_1(self,a,b,expect):
        assert add(a,b)==expect


@pytest.fixture()
def init():
    a=1
    assert a==4
    print('init...')
    return 1

def test5(init):
    print('test5...')

def test6(init):
    print('test6...')


if __name__ == '__main__':
    pytest.main(['-sv','test03.py'])