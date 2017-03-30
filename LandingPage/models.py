from django.db import models

# Create your models here.
from django.db import models
from django import forms
from django.core.validators import URLValidator
from django.contrib.auth.models import User
# Create your models here.
#
class Record (models.Model):
    direction               = models.CharField(max_length=50)
    shipper_name            = models.CharField(max_length=50)
    kg_available            = models.CharField(max_length=200, null=True, default="None")
    date                    = models.DateField(null=True)
    price                   = models.CharField(max_length=200, null=True, default="None")
    contact                 = models.CharField(max_length=200, null=True)
    pick_up_destination     = models.CharField(max_length=100, null=True, default="None")
    release_destination     = models.CharField(max_length=100, null=True, default="None")
    note                    = models.CharField(max_length=1000, null=True)
    url                     = models.TextField(validators=[URLValidator()], null=True, max_length=500)
    code                    = models.CharField(max_length=50, null=True, default="None", unique=True)
    is_checked              = models.BooleanField(null=False, default=False)

    def __unicode__(self):
        return self.shipper_name + " " + self.direction + " " + str(self.date)

class Email(models.Model):
    email = models.CharField(max_length=100)

    def __unicode__(self):
        return self.email or u''

#
# class ShipperRecord(Record):
#     user = models.ForeignKey(User)

