#
# /*
# comment
#
# ??u tiên thì em vi?t ra func declare mà hôm trc mình agree
# sau khi anh xong ui hòm hòm, lúc a g?n data vào template thì anh g?i service
# anh lên ?ây check ci th? có gì thay ??i
# */
#
# /*
# function declare
# def create_request(account,title,description,type,price,source_city,source_address,destination_city,destination_address,photo_link):
# def get_active_request_list():
# def get_all_request_list():
#
# */
#
# /*
# Note:
# From Dan: later implement currency
# */

class RequestManagement:

    def __init__(self):
        return


    def create(self, request):
        """
        create new item request.

        :param image_url: list of url to image
        :param thumb_url: url to thumbnail image
        :return: boolean false for fail, return RequestEntity
        """
        return


    def get(self):
        """
        get all request
        :return:
        """
        #todo: unnecessary method. to be removed in production
        return


    def get_by_id(self, request_id):
        """
        get request by id

        :param request_id:
        :return: request
        """
        return


    def get_by_account_id(self, account_id):
        """
        get list of request by account_id

        :param request_id_list: list of id
        :return: list of request
        """
        return


    def delete(self, request_id):
        """
        delete request by id

        :param request_id:
        :return: return deleted request object
        """
        return


    def update(self, request):
        """
        update a request, base on changes in fields

        :return: boolean fail, object successful

        """
        return


    def get_summary(self, origin_city, destination_city = None):
        """
        get summary of traffic, using certain algorithm
        :param origin_city:
        :param destination_city: optional. if not specified, query with all possible destination
        :return: request
        """
        return


CITY = (
    ('SG', 'Singapore'),
    ('HN', 'Ha Noi'),
    ('HCM', 'Ho Chi Minh'),
    )

CATEGORY = (
    ('1', u'?? l?ng'),
    ('2', u'?? khô'),
    ('3', u'Không ph?i th?c ?n'),
)

class Request:
    account_id = ""         #owner account id
    title = ""
    description = ""
    category = CATEGORY     # enum type
    price = ""
    origin_city = CITY      # enum type
    origin_address = ""
    destination_city = CITY     #enum type
    destination_address = ""
    image_url = []          #list of url to images
    thumb_url = ""          #url to thumbnail image
    expected_pickup_time = ""   #enum type
    active_status = True    #active status
    date_created = ""       #date type
    date_modified = ""      #date type


class RequestsSummary:
    origin_country = CITY
    destination_country = CITY
    total_request = {
        'city_code_here' : 0,
        'HN' : 10
    }

    #destination == None ==> return all dest
    #destination != None ==> return 1 cai

    highlight_request = []  #list of request_id

class ResponseEntity:
    success = None #bool
    message = None #str
    object = None #object
