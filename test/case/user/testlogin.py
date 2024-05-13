import unittest
from lib import xzs_login2


class MyTestCase(unittest.TestCase):
    xzs= xzs_login2.login()
    def test_login_01(self):
        t=self.xzs.login("student","123456")
        self.assertIn("成功",t.text)

    def test_login_02(self):
        t=self.xzs.login("student","")
        self.assertIn("用户名或密码错误",t.text)
    def test_login_03(self):
        t=self.xzs.login("","123456")
        self.assertIn("用户名或密码错误",t.text)
    def test_login_04(self):
        t=self.xzs.login("","")
        self.assertIn("用户名或密码错误",t.text)

if __name__ == '__main__':
    unittest.main()