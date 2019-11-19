import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email.header import Header
import os



class SendEmail():
    def __init__(self):
        self.sender = '443135581@qq.com'
        self.sender_name = "Dr"
        self.receivers = ['443135581@qq.com']
        self.sender_pass = 'vnaqbnbjmafpbijg'
        self.smtpObj = smtplib.SMTP('smtp.qq.com',25)
        self.email_content = ""
        self.subject = "无主题"
        self.message = None
    def login(self):
        ''' 登陆 '''
        self.smtpObj.login(self.sender,self.sender_pass)
    def sendmail(self):
        ''' 发送 '''
        try:
            self.smtpObj.sendmail(self.sender, self.receivers,self.message.as_string())
            return (0,"发送成功","")
        except smtplib.SMTPException as e:
            return (1,"发送失败",e)
    def set_email_content(self,email_content):
        ''' 设置邮件内容 '''
        self.email_content = email_content
    def set_emial_subject(self,subject):
        ''' 设置邮件主题 '''
        self.subject = subject
    def quit(self):
        self.smtpObj.quit()
    def add_message(self):
        # self.message = MIMEText(self.email_content, 'plain', 'utf-8')
        self.message = MIMEMultipart('related')

        self.message['From'] = Header(self.sender_name, 'utf-8')
        self.message['To'] =  Header("接收者", 'utf-8')
        self.message['Subject'] = Header(self.subject, 'utf-8')

        msgAlternative = MIMEMultipart('alternative')
        self.message.attach(msgAlternative)
        msgAlternative.attach(MIMEText(self.email_content, 'html', 'utf-8'))
    def add_image(self,image_file,name="default.png"):
        if not self.message:
            return (1,"还没添加正文")
        image = MIMEImage(image_file)
        image.add_header('Content-Id','<image1>')
        image['Content-Disposition'] = 'attachment;filename="{}"'.format(name)
        self.message.attach(image)
    def add_text_file(self,file):
        text_file = MIMEText(file, 'base64', 'utf-8')
        text_file["Content-Type"] = 'application/octet-stream'
        text_file["Content-Disposition"] = 'attachment; filename="runoob.txt"'
        self.message.attach(text_file)







test_mail = SendEmail()
test_mail.login()
test_mail.set_emial_subject("邮件主题")
test_mail.set_email_content("邮件内容")
test_mail.add_message()
image_file = open("test/image.png","rb").read()
test_py = open("test/test.py","rb").read()
test_mail.add_image(image_file,"image.png")
test_mail.add_text_file(test_py)
(status,msg,e) = test_mail.sendmail()
print(msg)
test_mail.quit()


















