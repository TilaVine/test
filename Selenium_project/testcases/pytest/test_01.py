import pytest



class TestLoginCase(object):
    def test01(self):
        assert 1==1

    def test02(self):
        assert 1==1


if __name__ == '__main__':
    pytest.main('-v','test_01.py')