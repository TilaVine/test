from ddt import data,ddt,file_data
from time import sleep
import unittest
from style import Style

@ddt()
class Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.k=Style('Chrome')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.k.quit()
    # def setUp(self) -> None:
    #     self.k=Style('Chrome')
    #
    # def tearDown(self) -> None:
    #     self.k.quit()

    @file_data(r'./data/datatest.yaml')
    def test_01(self,**kwargs):
        data=kwargs['common']
        self.k.open(data['url'])
        self.k.input(**data['input'],txt=data['txt'])
        self.k.click(**data['click'])
        sleep(3)

    # @file_data('../data/datatest.yaml')
    # def test_02(self,**kwargs):
    #     print(**kwargs['input'])

if __name__ == '__main__':
    unittest.main()