import pytest
from py_code import cacl
# -*- coding： utf-8 -*-
import yaml


class Test_Demo:
    res = cacl.Cacl()

    @pytest.mark.parametrize(('a', 'b', 'c'), yaml.safe_load(open(r'../data/data.yaml'))['add'])
    def test_add(self, cacl_up_down, a, b, c):
        """
        加法
        :param a:
        :param b:
        :return:
        """
        res = cacl.Cacl()
        print(f'加法{a} + {b}=={c}')
        assert c == self.res.add(a, b)

    @pytest.mark.parametrize(('a', 'b', 'c'), yaml.safe_load(open(r'../data/data.yaml'))['minus'])
    def test_minus(self, cacl_up_down, a, b, c):
        """
        加法
        :param a:
        :param b:
        :return:
        """
        print(f'减法{a} - {b}=={c}')
        assert c == self.res.minus(a, b)

    @pytest.mark.parametrize(('a', 'b', 'c'), yaml.safe_load(open(r'../data/data.yaml'))['product'])
    def test_product(self, cacl_up_down, a, b, c):
        """
        加法
        :param a:
        :param b:
        :return:
        """
        print(f'乘法{a} * {b}=={c}')
        assert c == self.res.product(a, b)

    @pytest.mark.parametrize(('a', 'b', 'c'), yaml.safe_load(open(r'../data/data.yaml'))['div'])
    def test_div(self, cacl_up_down, a, b, c):
        """
        加法
        :param a:
        :param b:
        :return:
        """
        print(f'除法{a} / {b}=={c}')
        assert c == self.res.div(a, b)


if __name__ == '__main__':
    pytest.main(['test_demo.py'])
    # print(yaml.safe_load(open(r'../data/data.yaml'))['add'])
