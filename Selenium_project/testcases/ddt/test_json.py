import pytest
import json
import os.path


def get_data():
    my_path=os.path.abspath(os.path.dirname(__file__))
    path=os.path.join(my_path,"../ddt/test.json")
    with open(path,encoding='utf-8') as f:
        lst=[]
        data=json.load(f)
        lst.extend(data['keys'])
        return lst

@pytest.mark.parametrize('name',get_data())
def test01(name):
    print(name)


if __name__ == '__main__':
    print(get_data())
    pytest.main(['-sv','test_json.py'])