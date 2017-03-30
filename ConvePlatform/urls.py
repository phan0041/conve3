from django.conf.urls import url, patterns, include

# from django.contrib import admin

urlpatterns = patterns('ConvePlatform.views',
    url(r'^$', 'index', name='index'),
    url(r'^request/create$', 'create', name='create-request'),
    url(r'^request/edit/(?P<request_id>\d+)$', 'edit_request', name='edit-request'),
    url(r'^request/edit/close', 'update_status_request', kwargs={"set_active": False}, name='close-request'), #TODO: remove this, temp solution
    url(r'^request/edit/open', 'update_status_request', kwargs={"set_active": True}, name='open-request'), #TODO: remove this, temp solution
    url(r'^request/delete$', 'delete_request', name='delete-request'),
    url(r'^request/(?P<request_id>\d+)$', 'detail', name='detail-request'),
    url(r'^browse$', 'browse', name='browse-request'),
    url(r'^login$', 'login', name='login'),
    url(r'^logout$', 'logout', name='logout'),
    url(r'^password/reset$', 'reset_password', name='reset-password'),
    url(r'^howitwork$', 'howitwork', name='howitwork'),
    url(r'^account$', 'profile_owner', name='profile-owner'),
    url(r'^account/edit$', 'edit_profile', kwargs={'mode': 1}, name='edit-profile'),
    url(r'^account/edit/password$', 'edit_profile', kwargs={'mode': 2}, name='edit-password'),
    url(r'^account/(?P<username>.+)', 'profile_guest', name='profile-guest'),
    url(r'^register', 'registration', name='registration'),
    url(r'^comment/post/(?P<request_id>\w+)', 'post_comment', name='post-comment'),

    url(r'^backenddevtest/', include('BackendDevTest.urls')),
)
# url /homepage, --> view homepage (lay tu conveplatform)

    # # url(r'^shipper/$', views.ShipperView, name='Shipper'),
    # url(r'^contact/$', views.ContactView, name='Contact'),
    # # url(r'^signup/$', views.SignupView, name='Signup'),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^submit/$', views.submit, name='submit'),

    # url(r'^contact/(?P<question_id>[0-9]+)/$', views.ContactView, name='ContactView'),
    # ex: /polls/5/results/
    # url(r'^test/$', views.TestView, name='Test'),
    # url('', include('social.apps.django_app.urls', namespace='social')),
    # url(r'^login/$','conve_facebook_app.views.login'),
    # url(r'^home/$', 'conve_facebook_app.views.home', name='Home'),
    # url(r'^logout/$', 'conve_facebook_app.views.logout'),
    # url(r'^submit/$', views.GetRecord, name='SubmitForm'),
    # url(r'^edit/(?P<id>\d+)/$', views.GetRecord,  name='EditRecord'),
    # url(r'^delete/(?P<id>\d+)/$', views.DeleteRecord, name='DeleteRecord'),
