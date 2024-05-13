#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/3/22 9:51
# Author    : smart
# @File     : run_all.py
# @Software :{PRODUCT_NAME}
import logging
import pickle,time
import sys
import unittest
from lib.HTMLTestRunner import HTMLTestRunner
from lib.send_email import send_email
from config.config import *
from test.suit.test_suites import get_suit


def discover():
    return unittest.defaultTestLoader.discover(test_case_path)

def run(suit):
    logging.info("==============开始测试==============")
    with open(report_file,"wb") as f:
        result=HTMLTestRunner(
            stream=f,
            title='接口测试用例',
            description='接口的登录和注册',
            verbosity=2
            ).run(suit)
        if result.failures:
            save_failures(result,last_fails_file)
    logging.info("==============测试结束==============")
    if send_email_enable:
            # 发送邮件
            send_email(report_file)
            logging.info("**************发送邮件**************")

def run_suite(suite_name):  # 运行自定义的TestSuite
    suite = get_suit(suite_name) # 通过套件名称返回套件实例
    print(suite)
    if isinstance(suite,unittest.TestSuite):
        run(suite) # 运行套件
    else:
        print("TestSuite不存在")
def run_all():
    run(discover())

def collect():
    suite = unittest.TestSuite()
    def _collect(tests):
        if isinstance(tests,unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)
    _collect(discover())
    return suite
def collect_only():
    t0 = time.time()
    i = 0
    for case in collect():
        i += 1
        print("{}.{}".format(str(i),case.id()))
    print("-----------------------------------------")
    print("Collect {} tests is {:.3f}s.".format(str(i), time.time() - t0))

def make_suit_list(list_file):
    with open(list_file,'r') as f:
        suit_list = f.readlines()
    suit_list=[x.strip() for x in suit_list if not x.startswith("#")]
    suit=unittest.TestSuite()
    all_suit=collect()
    for case in all_suit:
        if case.id().split('.')[-1] in suit_list:
            suit.addTest(case)
    return suit


def makesuite_by_testlist(test_list_file):
    with open(test_list_file,encoding='utf-8') as f:
        testlist =f.readlines()
    # print(testlist)
    # for i in testlist:
    #     print(i.strip())
    #     print(i.startswith("#"))
    testlist=[i.strip() for i in testlist if not i.startswith("#")]
    print(testlist)
    suite=unittest.TestSuite()
    all_cases=collect()
    for case in all_cases:
        case_name=case.id().split('.')[-1]
        if case_name in testlist:
            suite.addTest(case)
    return suite

def makesuit_by_tag(tag):
    suit=unittest.TestSuite()
    for case in collect():
        if case._testMethodDoc and tag in case._testMethodDoc:
            suit.addTest(case)
    return suit

def save_failures(result,file):
    suite = unittest.TestSuite()
    for case_result in result.failures:
        suite.addTest(case_result[0])
    with open(file,'wb')as f:
        pickle.dump(suite,f)


def rerun_fails():
    sys.path.append(test_case_path)
    with open(last_fails_file,'rb') as f:
        suite =pickle.load(f)
    run(suite)
def main():
    if options.collect_only:
        collect_only()
    elif options.rerun_fails:
        rerun_fails()
    elif options.tag:
        run(makesuit_by_tag(options.tag))
    else:
        run_all()

if __name__ == '__main__':
    # makesuite_by_testlist(test_list_file)
    # run(suit)
    # suit=makesuit_by_tag("level1")
    # run(suit)
    # suit = make_suit_list(test_list_file)
    # r =run(suit)
    # save_failures(r,last_fails_file)
    # rerun_fails()
    # main()
    run_all()
# if __name__ == '__main__':
#     logging.info("=============run_all开始测试================")
#     fp=open(report_file,'wb')
#     runner = HTMLTestRunner(
#         stream=fp,
#         title='测试用例',
#         description='xzs的登录和注册',
#         verbosity=2
#     )
#     suit = unittest.defaultTestLoader.discover(prj_path,'test*.py')
#     runner.run(suit)
#     fp.close()
#     send_email(report_file='report/report.html')
#     logging.info("=============run_all结束测试================")