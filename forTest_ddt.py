# -*- coding: utf-8 -*-
import unittest
from ddt import ddt,data,unpack,file_data
from selenium import webdriver
import time

def read_file():
    data = []
    with open("params.txt","r", encoding="utf-8") as f:
        for line in f.readlines():
            data.append(line.strip("\n").split(","))
    return data

# ddt的使用


try:
    import yaml
except ImportError:  # pragma: no cover
    have_yaml_support = False
else:
    have_yaml_support = True

# A good-looking decorator
needs_yaml = unittest.skipUnless(
    have_yaml_support, "Need YAML to run this test"
)


@ddt
class ForTestDdt(unittest.TestCase):

    @data("无极", "和尚")
    def test_1(self, txt):
        print(txt)

    # 传入多个参数需要解包
    @data(("无极", "http://www.baidu.com"),("小龙女","http://www.baidu.com"))
    @unpack
    def test_2(self, txt,url):
        print(txt)
        print(url)

    @data(*read_file())
    @unpack
    def test_3(self, txt, url):
        print(txt)
        print(url)

    # 需要配合pypaml包 yaml使用
    @needs_yaml
    @file_data("./content.yaml",yaml.FullLoader)
    def test_4(self, *args, **kwargs):
        print(kwargs)
        print(args)


if __name__ == "__main__":
    unittest.main()