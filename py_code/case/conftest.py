import pytest
import parser


# 取cmd参数
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="test",
                     help="test or dev or st")


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--env", default="test")


@pytest.fixture(scope='function', )
def cacl_up_down(request):
    print('【开始计算】')
    yield
    print("【结束计算】")
