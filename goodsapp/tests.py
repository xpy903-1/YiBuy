
# from django.test import TestCase


# Create your tests here.
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_message(title, message, receivers):
    client = smtplib.SMTP('smtp.qq.com', port=587)

    client.debuglevel = 1

    client.ehlo()
    client.starttls()

    client.login('673469226@qq.com', 'sqqqpbenatlfbdge')

    message = MIMEText(message, 'text', 'utf-8')

    message['Subject'] = Header(title, 'utf-8')

    message['From'] = '673469226@qq.com'

    message['To'] = ','.join(receivers)

    client.send_message(
        message,
        from_addr='673469226@qq.com',
        to_addrs=receivers
    )

    print('ok')

if __name__ == '__main__':

    send_message('早上好', '你好，润豪兄', '260440910@qq.com')

