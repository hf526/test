#coding=utf-8
import requests,unittest,json,time,ConfigParser,os
from public.browser import browser
from public import public
from data import data

class Imcloud_Flow(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_login(self):
        cf = ConfigParser.ConfigParser()
        cf.read(os.path.dirname(os.path.dirname(os.getcwd()))+'/config/config.ini')
        data.get_case()
        URL=cf.get("interface", "URL")
        #isinstance(url+data.url[0],str)
        for i in range(data.number-1):
            a = public.api_test(data.method[i],data.URL[i], data.data[i], data.harder[i])
            chick=data.chick[i].split('=>', 1)
            print chick[0],chick[1]
            print a.text
            if a.status_code == 200:
                b = json.loads(a.text)
                self.assertEqual(b[chick[0]], chick[1])
                print 'success'

if __name__ == '__main__':
    unittest.main()