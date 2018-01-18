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
        print data.method[0], URL+data.URL[0], data.data[0], data.harder[0]
        #isinstance(url+data.url[0],str)
        for i in range(data.number-1):
            # a = public.api_test("%s"%data.method[i],"%s"%url+data.url[i],"%s"%data.data[i],"%s"%data.harder[i])
            a = public.api_test(data.method[i], URL + data.URL[i], data.data[i], data.harder[i])
            print a
            if a.status_code == 200:
                b = json.loads(a.text)
                self.assertEqual(b['msg'], 'OK')

if __name__ == '__main__':
    unittest.main()