import pytest


@pytest.fixture(scope='function', )
def cacl_up_down():
    print('【开始计算】')
    yield
    print("【结束计算】")
