#连接邮箱
import smtplib
#发邮件
from email.mime.text import MIMEText
#发带附件的邮件
from email.mime.multipart import MIMEMultipart
#用于使用中文邮件主题
from email.header import Header

with open('../report/report.html', encoding='utf-8')as f:
    email_body=f.read()
#发送的对象
msg=MIMEMultipart()
msg.attach(MIMEText(email_body,'html','utf-8'))
#发件人
msg['From']='329454720@qq.com'
msg['To']='329454720@qq.com'
#邮件主题
msg['Subject']=Header('接口测试报告','utf-8')
#添加附件
att1=MIMEText(
    open('../report/report.html', 'rb').read(), 'base64', 'utf-8'
)#二进制格式打开
att1['Content-Type'] = 'application/octet-stream'

att1['Content-Disposition'] = 'attachment; filename="report.html"'

msg.attach(att1)

#创建一个smtp的链接
smtp=smtplib.SMTP_SSL('smtp.qq.com')
#登录发件箱
smtp.login('3294547209@qq.com','epvrvaeizlcsciii')
#发送邮件
smtp.sendmail('3294547209@qq.com','3294547209@qq.com',msg.as_string())
#退出
smtp.quit()