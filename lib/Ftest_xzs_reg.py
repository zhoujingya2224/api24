import unittest
import requests

name="student"
noname="peter"

class MyTestCase(unittest.TestCase):
    url = "http://192.168.55.48:8000/api/student/user/message/register"
    def test_reg_ok(self):
        if del_user(name=noname):
            del_user(noname)
        data={"username":noname,"password":"123456","userlevel":1}
        r = requests.post(url=self.url,json=data)
        result = {"code":1,"message":"成功","response":None}
        self.assertDictEqual(r.json(),result)
        self.assertTrue(check_user(noname))
        del_user(noname)

    def test_reg_err(self):
        if not check_user(name):
            add_user(name,"123456")
        data = {"userName":name,"password":"123456","userlevel":1}
        r = requests.post(url=self.url,json=data)

        result = {"code":1,"message":"成功","response":None}

        self.assertDictEqual(r.json(),result)

        self.assertTrue(check_user(noname))

        del_user(noname)

    def test_reg_err(self):
        if not check_user(name):
            add_user(name,"123456")
        data = {"code":2,"message":"用户已存在","response":None}
        self.assertDictEqual(r.json(),result)


if __name__ == '__main__':
    unittest.main()
