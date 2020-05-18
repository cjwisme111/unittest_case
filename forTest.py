# -*- coding: utf-8 -*-
import unittest

class ForTest(unittest.TestCase):

    # 类初始化调用
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    #类销毁调用
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    # 每个案例前初始化
    def setUp(self) -> None:
        print("setup")

    # 每个案例后清理
    def tearDown(self) -> None:
        print("tearDown")

    def test_1(self):
        self.assertEqual(3,4)

    def test_2(self):
        print("2")


if __name__ == "__main__":
    unittest.main()