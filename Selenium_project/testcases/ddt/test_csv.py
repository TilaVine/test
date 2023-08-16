import pytest
import csv
import os.path


def get_data():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../ddt/test.csv")
    with open(path,encoding='utf-8') as f:
        lst=csv.reader(f)
        my_data=[]
        for row in lst:
            my_data.extend(row)
        return my_data

@pytest.mark.parametrize('name',get_data())
def test01(name):
    print(name)

if __name__ == '__main__':
    pytest.main(['-sv','test_csv.py'])


