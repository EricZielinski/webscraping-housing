import smtplib
from utilities.yaml_methods import get_email_config


def sendEmail(**msg):
    USER, PASSWORD, HOST = get_email_config()
    s = smtplib.SMTP(HOST)
    s.starttls()
    msg = f'Subject: {msg["subject"]}\n\n{msg["body"]}'
    s.login(USER, PASSWORD)
    s.sendmail(USER, USER, msg)
    s.quit()

