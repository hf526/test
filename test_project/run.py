#coding=utf-8
import unittest

suite = unittest.TestLoader().discover("case")

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)  