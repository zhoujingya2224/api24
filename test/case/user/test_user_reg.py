from test.case.BaseCase import BaseCase
from lib.db import *
import json

class test_user_reg(BaseCase):
    def test_user_reg(self):
        case_data = self.get_case_data("reg_ok")
        userName = json.loads(case_data.get("args")).get('userName')
        if check_user(userName):
            del_user(userName)
        print(case_data)
        self.send_request(case_data)
        self.assertTrue(check_user(userName))
        del_user(userName)
    def test_user_reg_exist(self):
        case_data = self.get_case_data("reg_err")
        userName = json.loads(case_data.get("args")).get('userName')
        if not check_user(userName):
            add_user(userName, '123456')
        self.send_request(case_data)
