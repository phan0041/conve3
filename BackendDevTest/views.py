from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from AccountManagement.views import get_account, update_account
# Create your views here.

from RequestManagement.views import  get_requests
from AccountManagement.views import register
from django.contrib.auth.decorators import login_required
from Common.Entity import Entity

@login_required(login_url='/accounts/login/')
def getaccount(request,username):
    result = get_account(username)
    t = get_template('result.html')
    html = t.render(Context({'result':result}))
    return HttpResponse(html)

def registeraction(request,username,password,first_name):
    acc = Entity.AccountEntity()
    acc.last_name="default"
    acc.email = "hoaton.dev@gmail.com"
    acc.first_phone = "85368689"
    acc.second_phone = "+8485368689"
    acc.photo_link = None
    acc.facebook_link=None
    acc.description=None
    acc.username = username
    acc.first_name = first_name
    acc.address = "default"

    print "password: "+password
    result = register(acc, password)
    t = get_template('result.html')
    html = t.render(Context({'result':result}))
    return HttpResponse(html)

@login_required(login_url='/accounts/login/')
def updateaccount(request,username,first_name):
    last_name="default"
    email = "default@gmail.com"
    phone = "85368689"
    photo_link = None
    facebook_link=None
    description=None
    result = update_account(username,last_name,first_name,email,phone,photo_link,facebook_link,description)
    t = get_template('result.html')
    html = t.render(Context({'result':result}))
    return HttpResponse(html)

@login_required(login_url='/accounts/login/')
def post_request_action(request,username,title):
    description = "t"
    price = "25"
    s_type = "101"
    source_city = "Singapore"
    source_address = "Singapore"
    destination_city = "HCM"
    destination_address = "HCM"
    photo_link = None
    result = 1
    t = get_template('result.html')
    html = t.render(Context({'result':result}))
    return HttpResponse(html)

def get_active_requests(request):

    result = get_requests()
    t = get_template('result.html')
    html = t.render(Context({'result':result}))
    return HttpResponse(html)
