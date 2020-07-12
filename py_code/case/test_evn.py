import pytest
import sys
import os

sys.path.append(os.path.abspath('../..'))
from py_code import cacl
# -*- coding： utf-8 -*-
import yaml


class Test_evn:

    def test_get_evn(self, cmdopt):
        """
        :param cmdopt: 取到的命令行参数
        :return:
        """
        with open(r'../data/evn.yaml') as f:
            yaml_file = yaml.safe_load(f)
        try:
            evn = yaml_file[cmdopt]
            print(f'命令行参数:{cmdopt}，对应环境地址：{evn}')
            assert 1
        except Exception as e:
            print(f'命令行参数:{cmdopt}，找不到应环境，请传入正确的参数：test or dev or st')
            assert 0
