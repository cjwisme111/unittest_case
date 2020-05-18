# -*- coding: utf-8 -*-
import unittest

suite = unittest.TestSuite()

# 方式一
# suite.addTest(ForTest("test_1"))
# suite.addTest(ForTest("test_2"))
# 方式二
# lists = [ForTest("test_1"),ForTest("test_2")]
# suite.addTests(lists)
# 方式三
# 加载测试类
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ForTest))

# 方式四
# 文件名.测试类
suite.addTests(unittest.TestLoader().loadTestsFromName('forTest.ForTest'))

# 方式五
suite.addTests(unittest.TestLoader().loadTestsFromNames(['forTest.ForTest']))

runner = unittest.TextTestRunner()
runner.run(suite)
