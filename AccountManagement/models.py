from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

class Account(models.Model):
    id = models.AutoField(primary_key=True) #account id, not usernam
    user = models.ForeignKey(User, null=True, blank=True, default = None)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=datetime.datetime.now())  #when request is created
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=50,null=True)
    extra_phone = models.CharField(max_length=50,null=True)
    address = models.TextField(null=True)
    photo_link = models.TextField(null=True)
    thumb_link = models.TextField(null=True)
    facebook_link = models.URLField(null=True)
    view_num = models.IntegerField(default=0)
    description = models.TextField(null=True) #reserve
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    # def __init__(self,    username = None, last_name = None, first_name = None, created_date = None, email = None,
    #              first_phone = None, second_phone = None, address = None, photo_link = None, facebook_link = None,
    #              view_num = None, description = None):
    #     self.user = User.objects.get(username=username)
    #     self.last_name = last_name
    #     self.first_name = first_name
    #     self.created_date = created_date
    #     self.email = email
    #     self.first_phone = first_phone
    #     self.second_phone = second_phone
    #     self.address = address
    #     self.photo_link = photo_link
    #     self.facebook_link = facebook_link
    #     self.view_num = view_num
    #     self.description = description



# class UserProfile(models.Model):
#     # This line is required. Links UserProfile to a User model instance.
#     user = models.OneToOneField(User)
#
#     # The additional attributes we wish to include.
#     website = models.URLField(blank=True)
#     picture = models.ImageField(upload_to='profile_images', blank=True)
#
#     # Override the __unicode__() method to return out something meaningful!
#     def __unicode__(self):
#         return self.user.username

