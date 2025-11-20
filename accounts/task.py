from celery import shared_task
from time import sleep

@shared_task
def sendMail():
    sleep(5)
    print("done sending email!")

