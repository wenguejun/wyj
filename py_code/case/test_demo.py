import pytest
import sys
import os

sys.path.append(os.path.abspath('../..'))
from py_code import cacl
# -*- coding： utf-8 -*-
import yaml


class Test_Demo:
    res = cacl.Cacl()

    @pytest.mark.first
    @pytest.mark.dependency(name="add")
    @pytest.mark.parametrize(('a', 'b', 'c'), yaml.safe_load(open(r'../data/data.yaml'))['add'])
    def test_add(self, cacl_up_down, cmdopt, a, b, c):
        """
        加法
        :param a:
        :param b:
        :return:
        """

        print(f'加法{a} + {b}=={c}')
        assert c == self.res.add(a, b)

    @pytest.mark.second
    @pytest.mark.dependency(name='minus', depends=['add'])
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

    @pytest.mark.third
    @pytest.mark.dependency(name="product")
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

    @pytest.mark.fouth
    @pytest.mark.dependency(name='div', depends=['product'])
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
    # a =yaml.safe_load(open(r'../data/data.yaml'))['minus']
    # print(a)
    pass
    # pytest.main(['test_demo.py'])
    # print(yaml.safe_load(open(r'../data/data.yaml'))['add'])
