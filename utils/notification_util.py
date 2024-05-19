# _*_ coding : utf-8 _*_
# @Time : 2024/4/20 0:39
# @Author : aiqinghua
# @File : notification_util
# @Project : prs_v5
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from utils.read_ini_util import HandleConf


class HandlerNotification:
    """
    该类用于发送通知
    """
    def __init__(self):
        self.conf = HandleConf("/config/config.ini")
        self.host = self.conf.get_str(section="qq_email", option="host")
        self.port = int(self.conf.get_str(section="qq_email", option="port"))
        self.from_email = self.conf.get_str(section="qq_email", option="from_email")
        self.to_email = self.conf.get_str(section="qq_email", option="to_email")
        self.password = self.conf.get_str(section="qq_email", option="from_Authorization_code")
        self.subject = self.conf.get_str(section="qq_email", option="subject")
    def send_email(self, report_data):
        msg = MIMEMultipart()
        msg["From"] = self.from_email
        msg["To"] = self.to_email
        msg["Subject"] = self.subject
        body = report_data
        text = MIMEText(body, "html", "utf-8")
        msg.attach(text)

        # 添加附件
        # with open(file=filename, mode="rb") as fp:
        #     attachment = MIMEApplication(fp.read(), _subtype="txt")
        #     attachment.add_header("Content-Disposition", "attachment", filename=filename)
        #     msg.attach(attachment)

        try:
            smtp = smtplib.SMTP_SSL(self.host, self.port)
            smtp.login(self.from_email, self.password)
            smtp.sendmail(self.from_email, self.to_email, msg.as_string())
            logging.info("邮件发送成功")
        except Exception as e:
            logging.info("邮件发送失败:{}".format(e))
        finally:
            smtp.quit()
        logging.info("邮件发送成功")
    def dingding_notification(self):
        pass


if __name__ == '__main__':
    test = HandlerNotification()
    test.send_email()