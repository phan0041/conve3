# -*- coding: utf-8 -*-

from django.shortcuts import render
from RequestManagement.models import Request, Comment
from AccountManagement.models import Account
from django.contrib.auth.models import User
from Common.Entity.Entity import ResponseEntity, RequestEntity, AccountEntity, CommentEntity
from Common.Entity import Enum
import re
from django.db.models import Q
from Common.etc import utils
from django.db import transaction
from datetime import datetime
from django.utils.timezone import activate, localtime
from django.conf import settings
import pytz

activate(settings.TIME_ZONE)
##
# For internal usage

def list_Request_to_RequestEntity(list):
    result = []
    try:
        for item in list:
            result.append(convert_Request_to_RequestEntity(item).data)
    except Exception as e:
        print str(e)
    finally:
        return result


def check_request_authentication(request_id, username):
    result = False
    try:
        request = Request.objects.get(id=request_id)
        if username == request.account.user.username:
            result=True
    except Exception as e:
        print str(e)
        print "Exception in check_request_authentication"
    finally:
        return result


def convert_comments_list_to_comment_entity_list(comments):
    comment_entity_list = []
    try:
        for comment in comments:
            comment_enity= CommentEntity(comment_id=comment.id, username=comment.username,
                                         content=comment.content, request_id=comment.request_id, created_date=localtime(comment.created_date))
            comment_entity_list.append(comment_enity)
    except Exception as e:
        print str(e)
    finally:
        return comment_entity_list


def convert_Request_to_RequestEntity(request):
    """
    copy attr values of Request to RequestEntity, not id
    :param request:
    :param request_entity:
    :return:
    """

    result = ResponseEntity()
    try:
        request_entity = RequestEntity()
        request_entity.request_id = request.id
        request_entity.username = request.account.user.username
        request_entity.title = request.title
        request_entity.description = request.description
        request_entity.category = utils.convert_category_str_to_enum_list(request.category)
        request_entity.price = request.price
        request_entity.price_currency = Enum.CURRENCY(int(request.price_currency))
        request_entity.origin_city = Enum.CITY(int(request.origin_city))
        request_entity.origin_address = request.origin_address
        request_entity.destination_city = Enum.CITY(int(request.destination_city))
        request_entity.destination_address = request.destination_address
        request_entity.image_url = utils.convert_string_to_list(request.image_url)  # list
        request_entity.thumb_url = utils.convert_string_to_list(request.thumb_url)
        request_entity.expired_date = localtime(request.expired_date)
        request_entity.status = Enum.REQUEST_STATUS(int(request.status))
        request_entity.created_date = localtime(request.created_date)
        request_entity.last_modified_date = request.last_modified_date
        result.success = True
        result.data = request_entity
    except Exception as e:
        print str(e)
        result.success = False
        result.message = str(e)
    finally:
        return result


def copy_field_RequestEntity_to_Request(request_entity, request):
    try:
        request.title = request_entity.title
        request.description = request_entity.description
        request.category = utils.convert_list_enum_to_string(request_entity.category)
        request.price = request_entity.price
        request.price_currency = str(request_entity.price_currency.value)
        request.origin_city = str(request_entity.origin_city.value)
        request.origin_address = request_entity.origin_address
        request.destination_city = str(request_entity.destination_city.value)
        request.destination_address = request_entity.destination_address
        request.image_url = utils.convert_list_to_string(request_entity.image_url)
        request.thumb_url = utils.convert_list_to_string(request_entity.thumb_url)
        request.expired_date = request_entity.expired_date
        request.last_modified_date = request_entity.last_modified_date
        request.status = request_entity.status.value if request_entity.status is not None else None
    finally:
        return request


def convert_RequestEntity_to_Request(request_entity):
    """
    copy attr values of RequestEntity to Request, not id
    ex: want to update request
    :param request:
    :param request_entity:
    :return:
    """
    result = ResponseEntity()
    try:
        user = User.objects.get(username=request_entity.username)
        account = Account.objects.get(user=user)
        request = Request.objects.get(id=request_entity.request_id)
        request = copy_field_RequestEntity_to_Request(request_entity, request)
        result.success = True
        result.data = request
    except Exception as e:
        print str(e)
        result.success = False
        result.message = str(e)
    finally:
        return result


## For external usage
@transaction.atomic
def create_request(request_entity):
    """
    from RequestEntity object (no id), create a request in database and update id to RequestEntity
    :param request_entity: RequestEntity
    :return: RequestEntity after update id
    """

    result = ResponseEntity()
    try:
        user = User.objects.get(username=request_entity.username)
        account = Account.objects.get(user=user)
        request = Request()
        request.account = account
        request.save()
        request_entity.request_id = request.id
        request_result = convert_RequestEntity_to_Request(request_entity)
        if request_result.success == True:
            request_result.data.status = Enum.REQUEST_STATUS.Active.value
            request_result.data.save()
            result = request_result
        else:
            request_result.data.delete()
            result = request_result
        result.data = request

        # send message
        # subject = "New request "+unicode(request_entity.title) + " has been sent!!"
        # message = "You have created a request " + unicode(request_entity.title)+ ". Please contact Conve if it is not done by you."
        # recipient_list = ['conve1008@gmail.com',request.account.email,'conve100893@gmail.com']
        # utils.send_email(subject,message,recipient_list)
    except Exception as e:
        print str(e)
        result.success = False
    finally:
        return result


def get_request(id):
    """
    from RequestEntity object (no id), create a request in database and update id to RequestEntity
    :param request_entity: request_entity
    :return: RequestEntity after update id
    """

    result = ResponseEntity()
    try:
        request = Request.objects.exclude(status=Enum.REQUEST_STATUS.Deleted.value).get(id=id)
        request_entity = convert_Request_to_RequestEntity(request)
        result.success = True
        # result.data= request_entity
        result.data = request_entity.data
    except Exception as e:
        print str(e)
        result.message = str(e)
        result.success = False
    finally:
        return result


@transaction.atomic
def update_request(request_entity, username):
    """
    update a request that already exists in DB
    from RequestEntity object (have id), update field in db
    :param request_entity: RequestEntity
    :return: RequestEntity after update id
    """
    result = ResponseEntity()
    try:
        if check_request_authentication(id, username):
            raise Exception, 'This request not belong to this user'
        request_result = convert_RequestEntity_to_Request(request_entity)
        if request_result.success == True:
            request_result.data.save()
        result = request_result
    except Exception as e:
        print str(e)
        result.success = False
    finally:
        return result


def get_requests(status=None, origin=None, destination=None):
    """
    if status == None then get all
    else get request list by status
    :param status: Enum.REQUEST_STATUS
    :return:
    """
    result = ResponseEntity()
    try:
        if status is None:
            request_list = Request.objects.exclude(status=Enum.REQUEST_STATUS.Deleted.value)
        else:
            request_list = Request.objects.filter(status=status.value).order_by("-created_date")

        if origin is not None:
            request_list = request_list.filter(origin_city=origin)
        if destination is not None:
            request_list = request_list.filter(destination_city=destination)

        request_entities = list_Request_to_RequestEntity(request_list)
        result.success = True
        result.data = request_entities
    except Exception as e:
        print str(e)
        result.message = str(e)
        result.success = False
    finally:
        return result


def get_all_by_user(username):
    result = ResponseEntity()
    try:
        user = User.objects.get(username=username)
        account = Account.objects.get(user=user)
        requests = Request.objects.filter(account=account).exclude(Enum.REQUEST_STATUS.Deleted.value)
        result.message = "Success"
        result.success = True
        result.data = requests
    except Exception as e:
        print str(e)
        result.success = False
        result.message = str(e)
        result.data = None
    finally:
        return result


def count_request(origin_city, destination_city):
    """

    :param origin_city: code of origin city
    :param destination_city: code of destination city
    :return: number of active request from origin city to destination city
    """
    result = 0
    try:
        requests = Request.objects.filter(origin_city=origin_city.value, destination_city=destination_city.value,
                                          status=Enum.REQUEST_STATUS.Active.value)
        result = len(requests)
    except Exception as e:
        print str(e)
    finally:
        return result


def get_highlight_request_from_vietnam(limit):
    """

    :param origin_city: code of origin city
    :param destination_city: code of destination city
    :return: number of active request from origin city to destination city
    """
    result = []
    try:
        requests = Request.objects.filter((Q(origin_city=Enum.CITY.HAN.value) | Q(origin_city=Enum.CITY.HCM.value))
                                          & Q(status=Enum.REQUEST_STATUS.Active.value))
        request_entities = list_Request_to_RequestEntity(requests)
        result = request_entities[:limit]
    except Exception as e:
        print str(e)
    finally:
        return result


def get_highlight_request_from_singapore(limit):
    """

    :param origin_city: code of origin city
    :param destination_city: code of destination city
    :return: number of active request from origin city to destination city
    """
    result = []
    try:
        requests = Request.objects.filter(origin_city=Enum.CITY.SGN.value, status=Enum.REQUEST_STATUS.Active.value)
        request_entities = list_Request_to_RequestEntity(requests)
        result = request_entities[:limit]
    except Exception as e:
        print str(e)
    finally:
        return result


def get_RequestEntity_list_by_username(username, get_deleted=False, limit=50):
    """

    :param username:
    :param get_deleted: bool default not get deleted request unless specify
    :param limit:
    :return:
    """
    result = []
    try:
        user = User.objects.get(username=username)
        account = Account.objects.get(user=user)
        requests = Request.objects.filter(account=account).order_by("-created_date").order_by("status")
        if not get_deleted:
            requests = requests.exclude(status=Enum.REQUEST_STATUS.Deleted.value)
        request_entities = list_Request_to_RequestEntity(requests)
        result = request_entities[:limit]
    except Exception as e:
        print str(e)
    finally:
        return result


@transaction.atomic
def delete_request(id, username):
    """
    This function will change the status of request into delete
    :param id: id of request need to be delete
    :return:
    """
    result = ResponseEntity()
    try:
        if not check_request_authentication(id, username):
            raise Exception, 'This request not belong to this user'
        request = Request.objects.get(id=id)
        if request.status == Enum.REQUEST_STATUS.Deleted.value:
            result.message = "This request is already deleted"
            result.success = False
            result.data = convert_Request_to_RequestEntity(request)
            return
        request.status = Enum.REQUEST_STATUS.Deleted.value
        request.save()
        result.message = "Success"
        result.success = True
        result.data = convert_Request_to_RequestEntity(request)
    except Exception as e:
        print str(e)
        result.success = False
        result.message = str(e)
        result.data = None
    finally:
        return result


def get_comments_by_request(request_id):
    result=[]
    try:
        comments = Comment.objects.filter(request_id=request_id)
        comment_entity_list = convert_comments_list_to_comment_entity_list(comments)
        result = comment_entity_list
    except Exception as e:
        print str(e)
    finally:
        return result


@transaction.atomic
def add_comment(comment_entity):
    result = ResponseEntity()
    try:
        comment = Comment()
        comment.username = comment_entity.username
        comment.content = comment_entity.content
        comment.request_id = comment_entity.request_id
        comment.created_date = datetime.now(pytz.timezone(settings.TIME_ZONE))
        comment.save()
        result.message = "Success"
        result.success = True
        result.data = comment
    except Exception as e:
        print str(e)
        result.success = False
        result.message = str(e)
        result.data = None
    finally:
        return result
