__author__ = 'Dan'

import re
from Common.Entity import Enum
from django.core import mail
from ConvePlatform import settings
from datetime import tzinfo, timedelta, datetime

ZERO = timedelta(0)

class UTC(tzinfo):
  def utcoffset(self, dt):
    return ZERO
  def tzname(self, dt):
    return "UTC"
  def dst(self, dt):
    return ZERO

utc = UTC()

def send_email(subject, message,recipient_list):
    mail.send_mail(subject, message, settings.EMAIL_HOST_USER,
    recipient_list, fail_silently=True)

def convert_list_enum_to_string(list):
    result = ""
    try:
        if list == None:
            return
        if len(list) ==0:
            return
        if len(list) ==1:
            result=list[0].value
            return
        if isinstance(list,basestring):
            result = list
            return
        for item in list:

            result = result +str(item.value)+ ";"
    except Exception as e:
        print str(e)
    finally:
        return result

def convert_list_to_string(list):
    result = ""
    try:
        if list == None:
            return
        if len(list) ==0:
            return
        if len(list) ==1:
            result=list[0]
            return
        if isinstance(list,basestring):
            result = list
            return
        for item in list:

            result = result +str(item)+ ";"
    except Exception as e:
        print str(e)
    finally:
        return result
def convert_string_list_to_enum_category_list(list):
    result = []
    try:
        for item in list:
            result.append(Enum.CATEGORY(int(item)))
    except Exception as e:
        print str(e)
    finally:
        return result

def convert_string_to_list(string):
    """
    return a list of string if input is None, "", string or list
    :param string:
    :return:
    """
    result = []
    try:
        if string == None:
            pass
        elif string == "":
            pass
        elif string.__class__.__name__ in ('list', 'tuple'):
            result = string
        else:
            result = filter(None, re.split('[;]',string))
    except Exception as e:
        print str(e)
    finally:
        return result

def set(input,output):
    if input == None:
        return output
    else:
        return input
def convert_category_str_to_enum_list(string):
    result = []
    try:
        str_list = convert_string_to_list(string)
        if(len(str_list)==0):
            return
        for item in str_list:
            result.append(Enum.CATEGORY(int(item)))
    except Exception as e:
        print str(e)
    finally:
        return result

def convert_string_to_number(str):
    result = 0
    try:
        if str == None | str == "":
            return
        result = float(str)
    except Exception as e:
        print str(e)
    finally:
        return result


import calendar
from datetime import datetime, timedelta

def utc_to_local(utc_dt):
    # get integer timestamp to avoid precision lost
    timestamp = calendar.timegm(utc_dt.timetuple())
    local_dt = datetime.fromtimestamp(timestamp)
    assert utc_dt.resolution >= timedelta(microseconds=1)
    return local_dt.replace(microsecond=utc_dt.microsecond)


