__author__ = 'Dan'

from django.conf.urls import patterns, include, url
from BackendDevTest.views import registeraction,post_request_action,get_active_requests,getaccount,updateaccount

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    #http://127.0.0.1:8000/backenddevtest/registeraction/dan/123/dan/
    url(r'^registeraction/(?P<username>[0-9a-z]+)/(?P<password>[0-9a-z]+)/(?P<first_name>[0-9a-z]+)/$', registeraction),

    #http://127.0.0.1:8000/backenddevtest/getaccount/hoa/
    url(r'^getaccount/(?P<username>[0-9a-z]+)/$', getaccount),

    #http://127.0.0.1:8000/backenddevtest/updateaccount/dan/dannewname/
    url(r'^updateaccount/(?P<username>[0-9a-z]+)/(?P<first_name>[0-9a-z]+)/$', updateaccount),

    #http://127.0.0.1:8000/backenddevtest/postrequest/dan/posttitle5/
    url(r'^postrequest/(?P<username>[0-9a-z]+)/(?P<title>[0-9a-z]+)/$', post_request_action),

    #http://127.0.0.1:8000/backenddevtest/getactiverequests/
    url(r'^getactiverequests/$', get_active_requests),





)
