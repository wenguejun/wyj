import pytest
import sys
import os

sys.path.append(os.path.abspath('../..'))
from py_code import cacl
# -*- coding： utf-8 -*-
import yaml


class Check_Demo:
    res = cacl.Cacl()

    @pytest.mark.parametrize(('a', 'b', 'c'), yaml.safe_load(open(r'../data/data.yaml'))['add'])
    def check_add(self, cacl_up_down, cmdopt, a, b, c):
        """
        加法
        :param a:
        :param b:
        :return:
        """

        print(f'加法{a} + {b}=={c}')
        assert c == self.res.add(a, b)

    @pytest.mark.parametrize(('a', 'b', 'c'), yaml.safe_load(open(r'../data/data.yaml'))['minus'])
    def check_minus(self, cacl_up_down, a, b, c):
        """
        加法
        :param a:
        :param b:
        :return:
        """
        print(f'减法{a} - {b}=={c}')
        assert c == self.res.minus(a, b)

    @pytest.mark.parametrize(('a', 'b', 'c'), yaml.safe_load(open(r'../data/data.yaml'))['product'])
    def check_product(self, cacl_up_down, a, b, c):
        """
        加法
        :param a:
        :param b:
        :return:
        """
        print(f'乘法{a} * {b}=={c}')
        assert c == self.res.product(a, b)

    @pytest.mark.parametrize(('a', 'b', 'c'), yaml.safe_load(open(r'../data/data.yaml'))['div'])
    def check_div(self, cacl_up_down, a, b, c):
        """
        加法
        :param a:
        :param b:
        :return:
        """
        print(f'除法{a} / {b}=={c}')
        assert c == self.res.div(a, b)


if __name__ == '__main__':
    pass
    # pytest.main(['test_demo.py'])
    # print(yaml.safe_load(open(r'../data/data.yaml'))['add'])
    # a = yaml.safe_load(open(r'../data/data.yaml'))['minus']
    # print(a)
    # print([pytest.param(2,2,4,marks=pytest.mark.dependency(name='add1')),
    #        pytest.param(2,2,4,marks=pytest.mark.dependency(name='add2')),
    #        pytest.param(2,2,4,marks=pytest.mark.dependency(name='add3'))])
