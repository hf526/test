#coding=utf-8
import unittest
import testsuits
from case.testcase import Imcloud_Flow

suite=unittest.TestSuite(unittest.makeSuite(Imcloud_Flow))


if __name__=='__main__':
    #执行用例
    runner=unittest.TextTestRunner()
    runner.run(suite)
