import unittest
from test.case.user.testlogin import MyTestCase


class MyTestCase1(unittest.TestCase):
    def test_something(self):
        suit=unittest.TestCase()
        suit.addTest(MyTestCase("test_login_01"))
        suit.addTest2([m("test_reg_ok"),m("test_reg_err")])
        unittest.TextTestRunner(verbosity=2).run(suit)
    def test_makesuit(self):
        suit1=unittest.makeSuite(MyTestCase)
        unittest.TextTestRunner(verbosity=2).run(suit1)
    def test_loader(self):
        suit2=unittest.TestLoader().loadTestsFromTestCase(m)
        unittest.TextTestRunner(verbosity=2).run(suit2)
    # def test_discover(self):
    #     suit3=unittest.defaultTestLoader.discover("./")
    #     unittest.TextTestRunner(verbosity=2).run(suit3)
if __name__ == '__main__':
    unittest.main()

