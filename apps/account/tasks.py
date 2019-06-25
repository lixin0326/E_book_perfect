from celery import shared_task, task
from account.userhelper import send_mail_to


@task
def delay_send_mail(username, active_url, receive_mail, title):
    send_mail_to(username, active_url, receive_mail, title)
