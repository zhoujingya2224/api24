import logging
import os
from optparse import OptionParser
import time


now=time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
today=time.strftime('%Y-%m-%d',time.localtime(time.time()))

#项目路径
#当前绝对路径
prj_path =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#数据目录
data_path=os.path.join(prj_path,'data')
#用例目录
test_path=os.path.join(prj_path,'test')
#测试用例的目录
test_case_path=os.path.join(prj_path,'test','case')
#日志目录
log_file=os.path.join(prj_path,'log', 'log_{}.txt'.format(today))
last_fails_file = os.path.join(prj_path,'last_fails.pickle')

#报告路径
report_file=os.path.join(prj_path,'report', 'report_{}.html'.format(now))
data_file = os.path.join(prj_path,'data','test_user_data.xlsx')
test_list_file=os.path.join(prj_path,"test","test_list.txt")
#log配置
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s:%(name)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log.txt',
                    filemode='a')
#数据库配置
db_host='127.0.0.1'
db_port=3306
db_user='root'
db_password='root'
db='xzs'
#邮件配置
smtp_server='smtp.qq.com'
smtp_user='3294547209@qq.com'
smtp_ps='epvrvaeizlcsciii'
sender=smtp_user
receiver='3294547209@qq.com'
subject='接口测试报告'
send_email_enable=True
#命令行参数解析
parser=OptionParser()
parser.add_option("--collect_only",dest="collect_only",action="store_true",help="仅收集测试用例，不执行测试用例")
parser.add_option("--rerun-fails",dest="rerun-fails",action="store_true",help="重跑失败用例")
parser.add_option("--tag",dest="tag",action="store",default='leve1',help="指定测试用例标签")
(options,args)=parser.parse_args()


