from django.shortcuts import render
from django.http import HttpResponse
from .task import sendMail

def email(request):
    sendMail.delay()
    return HttpResponse("we sendend and email to you inbox")

