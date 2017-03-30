from django.conf.urls import url, patterns, include
from LandingPage import views
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', views.IndexView, name='Index'),
    url(r'^contact/$', views.ContactView, name='Contact'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^contact/(?P<question_id>[0-9]+)/$', views.ContactView, name='ContactView')
)