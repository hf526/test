#coding=utf-8
import smtplib,HTMLTestRunner,time
from email.mime.text import MIMEText
def set_email(file):    # 发送html格式的邮件
    sender = "529690699@qq.com"     # 发送邮件
    receiver = "x13155916315@qq.com"# 接收邮箱
    subject = "自动化测试报告"# 邮件主题
    smtpserver = "smtp.qq.com"# 发送邮箱服务器
    username = "529690699@qq.com"# 发送邮箱的账号密码
    password = "uwfbeyutitmmbgjd"
    f = open(file, 'rb')
    fp.close()
    body = f.read()
    try:
        msg = MIMEText(body, "html", "utf-8")  # HTML形式邮件
        msg['Subject'] = Header(subject, 'utf-8')
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        print "发送成功"
    except smtp.SMTPException, e:
        print "发送失败"
    finally:
        smtp.quit()
def html():
    now = time.strftime('%Y-%m-%d_%H_%M_%S_')
    filename='F:\hf/report//'+now+'result.html'   #地址
    file=open(filename,'wb')# 打开文件
    runner=HTMLTestRunner.HTMLTestRunner(stream=file,
    title=u'搜索功能测试报告',
    description=u'用例执行情况：')
    file.close()




