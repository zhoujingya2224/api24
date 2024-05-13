#连接邮箱
import smtplib
#发邮件
from email.mime.text import MIMEText
#发送的对象
msg=MIMEText('想你了','plain','utf-8')
#发件人
msg['From']='3294547209@qq.com'
msg['To']='3294547209@qq.com'
#邮件主题
msg['Subject']='周六的邮件'
#创建一个smtp的链接
smtp=smtplib.SMTP_SSL('smtp.qq.com')
#登录发件箱
smtp.login('3294547209@qq.com','epvrvaeizlcsciii')
#发送邮件
smtp.sendmail('3294547209@qq.com','3294547209@qq.com',msg.as_string())
#退出
smtp.quit()