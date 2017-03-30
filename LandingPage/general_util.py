__author__ = 'vanvo'

from models import Record

def format_string(s):
    temp = s.split("/")
    return temp[2] + "-" + temp[0] + "-" + temp[1]


def wipe_data():
    Record.objects.all().delete()

def check_all():
    for e in Record.objects.all():
        e.is_checked = 'True'
        e.save()

def validate_register_email(email):
    white_list = ["yahoo.com", "yahoo.com.vn", "e.ntu.edu.sg", "ntu.edu.sg", "gmail.com",]
    temp = email.index("@")
    email = email[temp+1:len(email)]
    if email in white_list:
        return True
    else:
        return False
    return True;
