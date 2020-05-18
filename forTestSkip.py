# -*- coding: utf-8 -*-
import unittest

class ForTestSkip(unittest.TestCase):

    # 跳过测试用例
    @unittest.skip
    def test_1(self):
        print(1)

    # 条件判断，true则跳过,false则执行用例
    @unittest.skipIf(1<2,reason="skipif test")
    def test_2(self):
        print(2)

    # 条件判断，expr : true则执行,false则跳过
    @unittest.skipUnless(1<2,reason="skipUnless test")
    def test_3(self):
        print(3)

    #标记该测试预期为失败 ，如果该测试方法运行失败，则该测试不算做失败
    @unittest.expectedFailure
    def test_4(self):
        self.assertEqual(3, 4 ,"equal 测试")

    def test_5(self):
        print(5)

if __name__ == "__main__":
    unittest.main()