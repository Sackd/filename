#电子邮件


# #SMTP发送邮件
# #先构造邮件
# from email.mime.text import MIMEText#email负责构造邮件
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')#'plain'表示纯文本
# #然后，通过SMTP发出去
# # 输入Email地址和口令:
# from_addr = input('From:2955308485@qq.com  ')
# password = input('Password:xjmkhfnxlxaiddjd')
# # 输入收件人地址:
# to_addr = input('To:m18234067931@163.com ')
# # 输入SMTP服务器地址:
# smtp_server = input('SMTP server:  smtp.qq.com')

# import smtplib
# server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
# server.set_debuglevel(1)
# server.connect(smtp_server )
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr

# import smtplib
    
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))

# from_addr ='2955308485@qq.com'
# password = 'xjmkhfnxlxaiddjd'
# to_addr = 'm18234067931@163.com'
# smtp_server = 'smtp.qq.com'

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
    
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# #server.connect(smtp_server)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

