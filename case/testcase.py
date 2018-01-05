#coding=utf-8
import requests,unittest,json
from public import public
from data import data

class jiekou(unittest.TestCase):
    def setUp(self):
        print "start_____________"
    def tearDown(self):
        print "end_____________"
    def test_login(self):
       login=public.api("post",data.url,data.data,data.headers)
       print  login.text






if __name__=="__mian__":
    run.main()