import pytest



class TestCase02(object):
    def test01(self):
        print('test01')
        self.add()

    def add(self):
        print('add')

    def test02(self):
        print('test02')
    @pytest.mark.do
    def test03(self):
        print('test03')

    @pytest.mark.undo
    def test04(self):
        print('test04')



if __name__ == '__main__':
    pytest.main('test_02.py::test01')