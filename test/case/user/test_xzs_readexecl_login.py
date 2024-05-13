import unittest,requests,json
import ddt
from lib import read_excel
from lib.case_log import log_case_info
import os,sys
from config.config import *

def read():
    r = read_excel.read_excel()
    l = r.excel_to_list(data_file,"test_user_login")
    t = []
    for i in range(len(l)):
        t.append(l[i]["case_name"])
    return t
@ddt.ddt()
class MyTestCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     cls.r=read_excel.read_excel()
    #     cls.l=cls.r.excel_to_list("test_user_data.xlsx","test_user_login")

    @ddt.data(*read())
    def test_login(self,name):
        r= read_excel.read_excel()
        l = r.excel_to_list(data_file,"test_user_login")
        t=r.get_test_data(l,name)
        url=t.get("url")
        args=t.get("args")
        exp=t.get("expect_res")
        data=json.loads(args)
        r=requests.post(url,json=data)
        log_case_info(name, url, args, exp, r.text)
        self.assertIn(exp,r.text)
    # def test_login_err1(self):
    #     t=self.r.get_test_data(self.l,"login_err1")
    #     url=t.get("url")
    #     args=t.get("args")
    #     exp=t.get("expect_res")
    #     data=json.loads(args)
    #     r=requests.post(url,json=data)
    #     self.assertIn(exp,r.text)

if __name__ == '__main__':
    unittest.main()
