#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from email.utils import parseaddr

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

import smtplib

# from_addr = "631068264@qq.com"
# password = "jvirjvjmsarlbefi"
# smtp_server = "smtp.qq.com"
# to_addr = "l631068264@gmail.com"


from_addr = "l631068264@gmail.com"
password = "!QAZXSW@3edc"
smtp_server = "smtp.gmail.com"
to_addr = "631068264@qq.com"
subject = "哈哈大傻逼"
text = "hello, send by Python..."


# message = """From: %s\nTo: %s\nSubject: %s\n\n%s
#         """ % (from_addr, to_addr, subject, text)


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


#
# msg = MIMEMultipart("alternative")
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
msg.attach(MIMEText('hello, send by Python...', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
                    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
                    '</body></html>', 'html', 'utf-8'))

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
