# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
from Common.Entity.Entity import ResponseEntity, RequestEntity, AccountEntity
from AccountManagement.models import Account
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Q
import string, random
from django.utils.timezone import activate, localtime
from django.conf import settings

from Common.etc import utils

activate(settings.TIME_ZONE)
##
# For internal usage


def email_is_exist_in_other_account(email, username):
    result=False
    try:
        account = Account.objects.get(email=email)

        if account is not None and username != account.user.username:
            result = True
            return
    except Exception as e:
        print str(e)
    finally:
        return result


def email_is_exist(email):
    result = False
    try:
        account = Account.objects.get(email=email)
        if account is not None:
            result = True
            return
    except Exception as e:
        print str(e)
    finally:
        return result


def generate_password():
    """

    :return: a random string of 6 characters
    """
    return ''.join(random.sample((string.ascii_uppercase+string.digits)*6,6))

def verify_account(account_entity, username):
    result = ResponseEntity()
    try:
        if (account_entity.username == username):
            result.message = "Success"
            result.success = True
        else:
            result.message = "Session username " + str(username) + " is different from account_entity username " + str(
                account_entity.username)
            result.success = False
    except Exception as e:
        print str(e)
        result.success = False
        result.message = str(e)
        result.data = None
    finally:
        return result


def add_user(username, password, email=None):
    result = ResponseEntity()
    try:
        user = User.objects.create_user(username, email, password)
        user.save()
        result.success = True
        result.data = user
    except Exception as e:
        print str(e)
        result.message = str(e)
        result.success = False
    finally:
        return result


def convert_Account_to_AccountEntity(account):
    account_entity = AccountEntity()
    account_entity.username = account.user.username
    account_entity.last_name = account.last_name
    account_entity.first_name = account.first_name
    account_entity.created_date = account.created_date # naive time object. Need to convert to aware time zone if updatable via UI
    account_entity.email = account.email
    account_entity.first_phone = account.phone
    account_entity.second_phone = account.extra_phone
    account_entity.address = account.address
    account_entity.photo_link = account.photo_link
    account_entity.thumb_link = account.thumb_link
    account_entity.facebook_link = account.facebook_link
    account_entity.view_num = account.view_num
    account_entity.description = account.description
    return account_entity


def copy_AccountEntity_to_Account(account_entity):
    result = ResponseEntity()
    try:
        user = User.objects.get(username=account_entity.username)

        account = Account.objects.get(user=user)
        account.last_name = account_entity.last_name
        account.first_name = account_entity.first_name
        account.created_date = account_entity.created_date if account_entity.created_date is not None else account.created_date
        account.email = account_entity.email
        account.phone = account_entity.first_phone
        account.extra_phone=account_entity.second_phone
        account.address = account_entity.address
        account.photo_link = account_entity.photo_link
        account.thumb_link = account_entity.thumb_link
        account.facebook_link = account_entity.facebook_link
        account.view_num = account_entity.view_num if account_entity.view_num is not None else account.view_num
        account.description = account_entity.description
        result.success = True
        result.data = account
    except Exception as e:
        print str(e)
        result.success = False
        result.message = str(e)
    finally:
        return result





# end of internal usage
##


##
# For external usage
@transaction.atomic
def register(account_entity, password):
    """
    create one record in user table and one record in account table
    :param account_entity: AccountEntity
    :param password:
    :return: Account
    """
    result = ResponseEntity()
    try:
        user = User.objects.filter(username=account_entity.username).first()
        if user is not None:
            raise ValueError(u"Tên đăng nhập này đã tồn tại trong hệ thống!")

        user = User.objects.filter(email=account_entity.email).first()
        if user is not None:
            raise ValueError(u"Email này đã tồn tại trong hệ thống!")

        user_result = add_user(account_entity.username, password, email=account_entity.email)
        if (user_result.success == False):
            result = user_result
            return
        account = Account(last_name=account_entity.last_name, first_name=account_entity.first_name,
                          user=user_result.data, email=account_entity.email,
                          phone=account_entity.first_phone, extra_phone=account_entity.second_phone,
                          address=account_entity.address, photo_link=account_entity.photo_link,
                          facebook_link=account_entity.facebook_link,
                          description=account_entity.description)
        account.save()
        result.success = True
        result.data = convert_Account_to_AccountEntity(account)
    except ValueError as e:
        result.success = False
        result.message = e.message
    except Exception as e:
        print str(e)
        result.success = False
        # do not throw error message to top layer, to distinguish with valid message
        # result.message = str(e)
    finally:
        return result


@transaction.atomic
def update_account(account_entity):
    result = ResponseEntity()
    try:
        account_result = copy_AccountEntity_to_Account(account_entity)

        account_result.data.save()

        result.message = "Success"
        result.success = True
        result.data = account_result.data
    except Exception as e:
        print str(e)
        result.success = False
        result.message = str(e)
        result.data = None
    finally:
        return result


def get_account(username):
    result = ResponseEntity()
    try:
        user = User.objects.get(username=username)
        account = Account.objects.get(user=user)
        account_entity = convert_Account_to_AccountEntity(account)
        result.message = "Success"
        result.success = True
        result.data = account_entity
    except Exception as e:
        print str(e)
        result.success = False
        result.message = str(e)
    finally:
        return result


def get_AccountEntity_by_username(username):
    result = ResponseEntity()
    try:
        user = User.objects.get(username=username)
        account = Account.objects.get(user=user)
        account_entity = convert_Account_to_AccountEntity(account)
        result.success = True
        result.data = account_entity
    except Exception as e:
        print str(e)
        result.success = False
        result.message = str(e)
    finally:
        return result


@transaction.atomic
def reset_password(username_or_email):
    """
    system will generate a random password and send to account email
    :param username:
    :param email:
    :return:
    """
    result = ResponseEntity()
    try:
        user = None
        try:
            user = User.objects.get(username=username_or_email)
            account = Account.objects.get(user=user)
        except Exception as e:
            pass
        if user is None:
            try:
                account=Account.objects.get(email=username_or_email)
            except Exception as e:
                pass
        if account is None:
            result.success = False
            result.message = "There is no username or email match"
            return

        email = account.email
        password = generate_password()
        user.set_password(password)
        subject = "Thay đổi mật khẩu ở Conve!"
        message = "Tên đăng nhập: "+str(user.username)+". Mật khẩu: "+str(password)+". Vì lí do an toàn, bạn hãy đăng nhập và thay đổi mật khẩu."
        recipient_list=[email]
        utils.send_email(subject,message,recipient_list)
        user.save()
        result.success = True
        result.data = {"email":email,"username":user.username}
    except Exception as e:
        print str(e)
        result.success = False
        result.message = str(e)
    finally:
        return result


@transaction.atomic
def change_password_by_username(username=None,email=None, password=None):
    """
    system change password according to user input
    :param username:
    :param email:
    :param password:
    :return:
    """
    # TODO: refactor checking and sending email to different system
    result = ResponseEntity()
    try:
        if username is not None:
            user = User.objects.get(username=username)
            account = Account.objects.get(user=user)
            email = account.email
        user.set_password(password)
        subject = "Change Password in Conve!"
        message = "Your password has been change recently. Please report if this is not done by you."
        recipient_list=[email]
        utils.send_email(subject,message,recipient_list)
        user.save()
        result.success = True
    except Exception as e:
        print str(e)
        result.success = False
        result.message = str(e)
    finally:
        return result
