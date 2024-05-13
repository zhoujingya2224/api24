import json
import unittest,requests
from lib.read_excel import *
from lib.db import *
from lib.case_log import log_case_info

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.li=read_excel().excel_to_list(data_file, "test_user_reg")
    def test_reg_ok(self):
        case_data=read_excel().get_test_data(self.li,'reg_ok')
        url=case_data.get('url')
        args=case_data.get('args')
        expect_res=case_data.get('expect_res')
        a=json.loads(args).get("userName")
        if check_user(name=a):
            del_user(a)
        res=requests.post(url=url,json=json.loads(args))
        log_case_info("test_reg_ok",url,args,expect_res,res.text)
        self.assertIn(expect_res,res.text)
        del_user(a)
    def test_reg_err(self):
        case_data=read_excel().get_test_data(self.li,'reg_err')
        url=case_data.get('url')
        args=case_data.get('args')
        expect_res=case_data.get('expect_res')
        res=requests.post(url=url,json=json.loads(args))
        logging.info("测试用例：{}".format('test_reg_err'))
        log_case_info("test_reg_err", url, args, expect_res, res.text)
        self.assertIn(expect_res,res.text)
if __name__=='__main__':
    unittest.main()
