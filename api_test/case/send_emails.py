import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import zmail
import os

# from HttpRunnerManager.settings import EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD, EMAIL_HOST, EMAIL_PORT
# EMAIL_SEND_USERNAME = '283340479@qq.com'  # 定时任务报告发送邮箱，支持163,qq,sina,企业qq邮箱等，注意需要开通smtp服务
# EMAIL_SEND_PASSWORD = '*************'     # qq邮箱授权密码


# def send_email_reports(sender,receiver, html_report_path):
#     if '@sina.com' in receiver:
#         smtp_server = 'smtp.sina.com'
#     elif '@163.com' in receiver:
#         smtp_server = 'smtp.163.com'
#     elif '@qq.com' in receiver:
#         smtp_server = 'smtp.qq.com'
#     else:
#         smtp_server = EMAIL_HOST
#
#     subject = "接口自动化测试报告"
#
#     with io.open(html_report_path, 'r', encoding='utf-8') as stream:
#         send_file = stream.read()
#
#     att = MIMEText(send_file, "base64", "utf-8")
#     att["Content-Type"] = "application/octet-stream"
#     att["Content-Disposition"] = "attachment;filename = TestReports.html"
#
#     body = MIMEText("附件为定时任务生成的接口测试报告，请查收，谢谢！", _subtype='html', _charset='gb2312')
#
#     msg = MIMEMultipart('related')
#     msg['Subject'] = subject
#     msg['from'] = sender
#     msg['to'] = receiver
#     msg.attach(att)
#     msg.attach(body)
#
#     # smtp = smtplib.SMTP(port=EMAIL_PORT)
#     # smtp.connect(smtp_server, port=EMAIL_PORT)
#     # smtp.starttls()
#     # smtp.login(EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD)
#     #
#     #
#     # smtp.sendmail(EMAIL_SEND_USERNAME, receiver.split(','), msg.as_string())
#     # smtp.quit()
#
#     try:
#         smtp = smtplib.SMTP()
#         smtp.connect(smtp_server)                      # 连服务器
#         smtp.login(EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD)
#     except:
#         smtp = smtplib.SMTP_SSL(smtp_server, EMAIL_PORT)
#         smtp.login(EMAIL_SEND_USERNAME, EMAIL_SEND_PASSWORD)                       # 登录
#     smtp.sendmail(EMAIL_SEND_USERNAME, receiver.split(','), msg.as_string())
#     smtp.quit()
# def send_email():
#     server = zmail.server('807737661@qq.com',"hciwptgmehzzbdeh")
#
#     server.send_mail('wesley.wang@feisu.com',{'subject':'hello!',"content_text":'nothing'})

# server = zmail.server('807737661@qq.com',"hciwptgmehzzbdeh")
# if server.smtp_able():
#     pass
# if server.pop_able():
#     pass
# with open('D:\BaiduNetdiskDownload\\api_test\\report\html\index.html','r',encoding='utf-8') as f:
#     content_html=f.read()
# mail = {
#     'subject': 'Success!',  # Anything you want.
#     'content_text': content_html,  # Anything you want.
#     'attachments': ['D:\BaiduNetdiskDownload\\api_test\case\ddm.png',],  # Absolute path will be better.
# }
#
# server = zmail.server('807737661@qq.com',"hciwptgmehzzbdeh")
# #自定义您的邮件服务器
# #server = zmail.server('username','password',smtp_host='smtp.163.com',smtp_port=994,smtp_ssl=True,pop_host='pop.163.com',pop_port=995,pop_tls=True)
# server.send_mail([('master',"wesley.wang@feisu.com"),], mail,cc=[('leader','lin799891@163.com')])
# mails = server.get_latest()
# zmail.show(mails)
# for k,v in mail.items():
#     print(k,v)

# if __name__ == '__main__':
#     send_email()
# ----------1.跟发件相关的参数------
# # smtpserver = "smtp.163.com"            # 发件服务器
# smtpserver = "smtp.qq.com"            # 发件服务器
# # port = 0                                            # 端口
# port = 465                                           # 端口
# sender = '807737661@qq.com'               # 账号
# psw = "hciwptgmehzzbdeh"                         # 密码
# receiver = ["lin799891@163.com","wesley.wang@feisu.com"]        # 接收人
#
#
# # ----------2.编辑邮件的内容------
# with open("D:\\BaiduNetdiskDownload\\api_test\\report.html",'r',encoding='utf-8') as f:
#     content_html = f.read()
# subject = "就这样凑合下吧"
# # body = content_html  # 定义邮件正文为html格式
# # msg = MIMEText(body, "html", "utf-8")
# msg = MIMEMultipart()
# msg['from'] = sender
# msg['to'] = ";".join(receiver)
# msg['subject'] = subject
#
# # 正文
# body = MIMEText(content_html, "html", "utf-8")
# msg.attach(body)
#
# # 附件
# att = MIMEText(content_html, "base64", "utf-8")
# att["Content-Type"] = "application/octet-stream"
# att["Content-Disposition"] = 'attachment; filename="test_report.html"'
# msg.attach(att)
#
# # ----------3.发送邮件------
# try:
#     smtp = smtplib.SMTP()
#     smtp.connect(smtpserver)                      # 连服务器
#     smtp.login(sender, psw)
# except:
#     smtp = smtplib.SMTP_SSL(smtpserver, port)
#     smtp.login(sender, psw)                       # 登录
# smtp.sendmail(sender, receiver, msg.as_string())  # 发送
# smtp.quit()
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from case.record_log import *
from common.readconfig import *
class SendEmail(object):
    '''
    发送邮件模块封装，属性均从config.ini文件获得
    '''

    def __init__(self, smtpServer, mailPort, mailSender, mailPwd, mailtoList, mailSubject):
        self.mail_smtpserver = smtpServer
        self.mail_port = mailPort
        self.mail_sender = mailSender
        self.mail_pwd = mailPwd
        # 接收邮件列表
        self.mail_receiverList = mailtoList
        self.mail_subject = mailSubject
        # self.mail_content = mailContent

    def sendFile(self, reportFile):
        '''
        发送各种类型的附件
        '''
        # 构建根容器
        msg = MIMEMultipart()

        # 邮件正文部分body，1、可以用HTML自己自定义body内容；2、读取其他文件的内容为body
        # body = "您好，<p>这里是使用Python登录邮箱，并发送附件的测试<\p>"
        with open(reportFile, 'r', encoding='UTF-8') as f:
            body = f.read()

        # _charset 是指Content_type的类型
        msg.attach(MIMEText(_text=body, _subtype='html', _charset='utf-8'))

        # 邮件主题、发送人、收件人、内容
        msg['Subject'] = self.mail_subject  # u'自动化测试报告'
        msg['from'] = self.mail_sender
        # msg['to'] = self.mail_pwd
        msg['to'] = ";".join(self.mail_receiverList)

        # 添加附件
        attachment = MIMEText(_text=open(reportFile, 'rb').read(), _subtype='base64', _charset='utf-8')
        attachment['Content-Type'] = 'application/octet-stream'
        attachment['Content-Disposition'] = 'attachment;filename = "result.html"'
        msg.attach(attachment)

        try:
            smtp = smtplib.SMTP_SSL(host=self.mail_smtpserver, port=self.mail_port)  # 继承自SMTP
        except:
            smtp = smtplib.SMTP()
            smtp.connect(self.mail_smtpserver, self.mail_port)

        # smtp.set_debuglevel(1)#控制台输出打印邮件发送打印信息
        # 创建安全连接，加密SMTP
        # smtp.starttls()  # Puts the connection to the SMTP server into TLS mode.加上可能报STARTTLS extension not supported by server.不支持
        # 用户名和密码
        smtp.login(user=self.mail_sender, password=self.mail_pwd)

        # 函数：sendmail(self, from_addr, to_addrs, msg, mail_options=[],rcpt_options=[]):
        smtp.sendmail(self.mail_sender, self.mail_receiverList, msg.as_string())
        smtp.quit()


# 调试代码
if __name__ == "__main__":
    # mail_smtpserver = 'smtp.qq.com'
    # mail_port = 465#端口465也行，587
    # mail_sender = '807737661@qq.com'
    # mail_pwd = 'hciwptgmehzzbdeh'
    # mail_receiverList = ['wesley.wang@feisu.com', 'lin799891@163.com']
    # mail_subject = u'继续'
    # s = SendEmail(mail_smtpserver, mail_port, mail_sender, mail_pwd, mail_receiverList, mail_subject)

    # s = SendEmail(",".join(email_info))#该方式不行呢
    email_info =get_emailinfo("smtp_server","port","sender","pwd","receiver","subject")
    s = SendEmail(email_info[0],email_info[1],email_info[2],email_info[3],email_info[4:-1],email_info[5])
    s.sendFile(r"D:\BaiduNetdiskDownload\api_test\report.html")
    logger = Log()
    logger.debug('邮件发送成功！')


