from django.db import models
import datetime
from Common.Entity import Enum


# Create your models here.

class Request(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey('AccountManagement.Account')
    title = models.TextField()
    description = models.TextField(null=True)
    category = models.CharField(max_length=50,default="General")
    price = models.CharField(max_length=50,null=True)
    price_currency = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50, default=Enum.REQUEST_STATUS.Active.value)    #active | closed | expired
    created_date = models.DateTimeField(default=datetime.datetime.now())  #when request is created
    closed_date = models.DateTimeField(null=True)  #when request is actively close by user
    expired_date = models.DateTimeField(null=True)  #user set the expired date for shipper to see, could be extend by user
    asap = models.BooleanField(default=True)
    last_modified_date = models.DateTimeField(null=True)
    origin_city = models.CharField(max_length=225)
    origin_address = models.TextField(null=True)
    destination_city = models.CharField(max_length=225)
    destination_address = models.TextField(null=True)
    view_num = models.IntegerField(default=0)
    image_url = models.TextField(null=True)
    thumb_url = models.TextField(null=True)

    def __unicode__(self):
        return u'%id %s %s' % (self.id, self.title, self.category)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    username = models.CharField(max_length=50,null=False)
    created_date = models.DateTimeField()
    request_id = models.CharField(max_length=50,null=False)

    def __unicode__(self):
        return u'%id %s %s' % (self.id, self.content, self.username)

