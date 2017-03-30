__author__ = 'Dan'

from Common.etc import utils
import Enum


class AccountEntity:
    username = None
    last_name = None
    first_name = None
    created_date = None
    email = None
    first_phone = None
    second_phone = None
    address = None
    photo_link = None
    thumb_link = None
    facebook_link = None
    view_num = None
    description = None

    def __init__(self, username=None, last_name=None, first_name=None, created_date=None, email=None,
                 first_phone=None, second_phone=None, address=None, photo_link=None, thumb_link=None,
                 facebook_link=None, view_num=None, description=None):
        self.username = username
        self.last_name = last_name
        self.first_name = first_name
        self.created_date = created_date
        self.email = email
        self.first_phone = first_phone
        self.second_phone = second_phone
        self.address = address
        self.photo_link = photo_link
        self.thumb_link = thumb_link
        self.facebook_link = facebook_link
        self.view_num = view_num
        self.description = description

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class RequestEntity:
    request_id = None
    username = None
    title = None
    description = None
    category = []  # Category Enum type
    price = None
    price_currency = None  # Currecy enum type
    origin_city = None  # City Enum Type
    origin_address = None
    destination_city = None  # City Enum Type
    destination_address = ""
    image_url = []  # list of url to images
    thumb_url = []  # url to thumbnail image
    expired_date = None  # enum type
    status = None  # active status
    created_date = None  # date type
    last_modified_date = None  # date type

    def __init__(self):
        pass

    @staticmethod
    def create_request_entity(username, title, category, price, origin_city, origin_desc,
                              destination_city, destination_desc, description, img_url, expired_date, thumb_url,
                              price_currency=1, id=None, status=Enum.REQUEST_STATUS.Active):
        request_entity = RequestEntity()
        request_entity.request_id = id
        request_entity.username = username
        request_entity.title = title
        request_entity.category = utils.convert_string_list_to_enum_category_list(category)
        request_entity.price = price
        request_entity.price_currency = Enum.CURRENCY(int(price_currency))
        request_entity.origin_city = Enum.CITY(int(origin_city))
        request_entity.origin_address = origin_desc
        request_entity.destination_city = Enum.CITY(int(destination_city))
        request_entity.destination_address = destination_desc
        request_entity.description = description
        request_entity.image_url = utils.convert_string_to_list(img_url)
        request_entity.expired_date = expired_date
        request_entity.thumb_url = utils.convert_string_to_list(thumb_url)
        request_entity.status = status
        return request_entity


class ResponseEntity:
    success = None  # True, False
    message = None  # If failed, provide reason here
    data = None  # return data on success

    def __unicode__(self):
        return u'Success: %s Message: %s Data: %s' % (self.success, self.message, self.data)


class CommentEntity:
    comment_id = None
    content = None
    username = None
    created_date = None
    request_id = None

    def __init__(self, comment_id=None, username=None, content=None, request_id=None, created_date=None):
        self.comment_id = comment_id
        self.username = username
        self.content = content
        self.request_id = request_id
        self.created_date = created_date
