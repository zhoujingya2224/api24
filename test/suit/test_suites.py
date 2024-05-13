import unittest
import sys
sys.path.append("../..")
from test.case.user.test_user_reg import test_user_reg
from test.case.user.test_user_login import test_user_login

smoke_suit=unittest.TestSuite()
smoke_suit.addTests([test_user_login("test_login_success"),test_user_reg("test_user_reg")])

def get_suit(suit_name):
    smoke_suit = unittest.TestSuite()
    smoke_suit.addTests([test_user_login("test_login_success"), test_user_reg("test_user_reg")])
    return suit_name

unittest.TextTestRunner(verbosity=2).run(smoke_suit)