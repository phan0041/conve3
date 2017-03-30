# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
import json, hmac, hashlib
from datetime import datetime, timedelta

from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from Common.Entity.Entity import RequestEntity, AccountEntity, CommentEntity
from Common.Entity import Enum
from .forms import CreateRequestForm, LoginForm, RegistrationForm, ResetPasswordForm, EditProfileForm, \
    ChangePasswordForm, PostCommentForm
from .decorators import login_required_message_and_redirect as login_required

from RequestManagement.views import get_highlight_request_from_singapore, get_highlight_request_from_vietnam, \
    count_request, create_request, get_RequestEntity_list_by_username, get_request, get_requests, update_request, \
    delete_request as delete_request_backend, get_comments_by_request, add_comment
from AccountManagement.views import get_AccountEntity_by_username, get_account, register as register_user, \
    reset_password as reset_password_backend, update_account, change_password_by_username, email_is_exist_in_other_account


from Common.etc import utils
from django.core.mail import send_mail
import settings
from django.utils import timezone


def index(request):
    """
    Render home page.
    :param request:
    :return:
    """
    template = 'ConvePlatform/index.html'

    # send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
    #           ['conve100893@gmail.com'], fail_silently=False)

    request_counter = {
        'to_sg': [count_request(Enum.CITY.HAN, Enum.CITY.SGN), count_request(Enum.CITY.HCM, Enum.CITY.SGN)],
        'from_sg': [count_request(Enum.CITY.SGN, Enum.CITY.HAN), count_request(Enum.CITY.SGN, Enum.CITY.HCM)]
    }

    request_list_sg_vn = _preprocess_request_entity_list(get_highlight_request_from_singapore(4))
    request_list_vn_sg = _preprocess_request_entity_list(get_highlight_request_from_vietnam(4))

    context = {'request_from_sg': request_list_sg_vn,
               'request_to_sg': request_list_vn_sg,
               'request_counter': request_counter}

    return render(request, template, context)


def registration(request):
    """
    on GET request, render registration page
    on POST request, process registration form
    :param request: HttpRequest return to index page
    :return:
    """
    template = 'ConvePlatform/registration.html'

    # GET request
    if request.method == "GET":
        form = RegistrationForm()
        context = {'form': form}
        return render(request, template, context)

    # POST request
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            result = get_account(form.cleaned_data['username'])
            if not result.success:
                acc = AccountEntity()
                acc.username = form.cleaned_data['username']
                acc.email = form.cleaned_data['email']
                acc.first_phone = form.cleaned_data['phone']
                acc.last_name = form.cleaned_data['last_name']
                acc.first_name = form.cleaned_data['first_name']

                # register account action
                result = register_user(acc, form.cleaned_data['password'])
                if result.success:
                    return login(request, from_backend=True)
                else:
                    message = result.message if result.message is not None \
                                            else u'Hệ thống có lỗi không thể đăng ký tài khoản này!'
                    #DEBUG
                    messages.error(request, message)
            else:
                # duplicate account
                messages.error(request, message=u'Tên đăng nhập này đã tồn tại!')
        else:
            messages.error(request, message=u'Form đăng ký có lỗi!')

        context = {'form': form}
        return render(request, template, context)


def logout(request):
    """
    process logout request. upon logout redirect to recurrent view or index
    :param request:
    :return: HttpResponseRedirect redirect to homepage
    """
    auth_logout(request)
    return HttpResponseRedirect(request.GET.get('next', reverse('index')))


def login(request, from_backend=False):
    """
    on get request, render login view
    on logging in, process submitted credential and initiate session data
    :param request:
    :param from_backend: bool backend login
    :return:
    """
    template = 'ConvePlatform/login.html'
    if request.user.is_authenticated():
        return redirect(reverse("index"))

    if request.method == "GET":
        form = LoginForm()
        context = {'form': form}
        context["next"] = request.GET.get('next', '')
        return render(request, template, context)

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    # Redirect to a success page.

                    if "next" in request.POST and request.POST['next'] != '':
                        return redirect(request.POST["next"])
                    else:
                        return redirect(reverse("index"))
                else:
                    context = {'form': form,
                               'error_message': 'Tài khoản của bạn đã bị khóa',
                               'next': request.POST["next"]}
                    return render(request, template, context)
            else:
                context = {'form': form,
                           'error_message': 'Sai tên đăng nhập hoặc mật khẩu',
                           'next': request.POST["next"]}
                return render(request, template, context)
        else:
            context = {'form': form,
                       'error_message': 'Mẫu đơn không hợp lệ',
                       'next': request.POST["next"]}
            return render(request, template, context)


def reset_password(request, from_backend=False):
    """

    :param request:
    :param from_backend:
    :return:
    """
    template = 'ConvePlatform/reset_password.html'
    if request.user.is_authenticated():
        return redirect(reverse("index"))

    if request.method == "GET":
        form = ResetPasswordForm()
        context = {'form': form}
        context["next"] = request.GET.get('next', '')
        return render(request, template, context)

    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            # todo: do login authentication and set session
            username_or_email = form.cleaned_data["username_or_email"]
            reset_result = reset_password_backend(username_or_email)
            error_message = None
            success_message = None
            if not reset_result.success:
                error_message = u"Tên đăng nhập hoặc email không tồn tại!"
            else:
                email = reset_result.data['email']
                success_message = 'Mật khẩu mới đã được gửi đi đến email '+str(email)+\
                                '. Nhấn gửi lại nếu bạn chưa nhận được mật khẩu mới sau 30 giây'
            context = {'form': form,
                       'error_message': error_message,
                       'success_message': success_message,
                       'next': request.POST["next"]}
            return render(request, template, context)

        else:
            context = {'form': form,
                       'error_message': 'Mẫu đơn không hợp lệ',
                       'next': request.POST["next"]}
            return render(request, template, context)


def browse(request):
    """
    Render list of item request page
    :param request:
    :return:
    """
    template = "ConvePlatform/browse_request.html"
    filters = {
        'origin': None,
        'destination': None,
    }
    if 'origin' in request.GET and request.GET['origin'] != '':
        filters['origin'] = request.GET['origin']
    if 'destination' in request.GET and request.GET['destination'] != '':
        filters['destination'] = request.GET['destination']

    result = get_requests(status=Enum.REQUEST_STATUS.Active, origin=filters['origin'],
                          destination=filters['destination'])
    if result.success:
        list_req = _preprocess_request_entity_list(result.data)

        cities_tuple = (
            ('', '-------'),
            (Enum.CITY.SGN.value, Enum.CITY.SGN.label()),
            (Enum.CITY.HAN.value, Enum.CITY.HAN.label()),
            (Enum.CITY.HCM.value, Enum.CITY.HCM.label()),
            (Enum.CITY.OTHER.value, Enum.CITY.OTHER.label()),
        )
        context = {
            "request": list_req,
            "cities": cities_tuple,
            "filters": filters
        }

        # todo: trim title, account_id

        return render(request, template, context)


@login_required(login_url='/login', message=u'Bạn phải đăng nhập để đăng hàng!')
def create(request):
    """
    Render create new item request page
    :param request:
    :return:
    """
    template = 'ConvePlatform/create_request.html'
    error_message = None

    if request.method == 'GET':
        # create new parameters, signature pair to pass to template
        params_json, signature = _generate_signature()

        # render new form to submit
        form = CreateRequestForm(initial={'origin_city': '', 'destination_city': ''})

        context = {'form': form,
                   'json_assy': params_json,
                   'sign': signature}
        return render(request, template, context)

    if request.method == 'POST':
        # submit form
        form = CreateRequestForm(request.POST)

        if form.is_valid():
            request_entity = RequestEntity.create_request_entity(request.user.username, form.cleaned_data['title'],
                                                                 form.cleaned_data['category'],
                                                                 form.cleaned_data['price'],
                                                                 form.cleaned_data['origin_city'],
                                                                 form.cleaned_data['origin_desc'],
                                                                 form.cleaned_data['destination_city'],
                                                                 form.cleaned_data['destination_desc'],
                                                                 form.cleaned_data['description'],
                                                                 form.cleaned_data['img_url'],
                                                                 expired_date=form.cleaned_data['expiry_date'],
                                                                 thumb_url=form.cleaned_data['thumb_url'],
                                                                 price_currency=form.cleaned_data['price_currency'])
            result = create_request(request_entity)
            if result.success:
                return HttpResponseRedirect(reverse('profile-owner'))
            else:
                error_message = result.message

            context = {'form': form,
                       'error_message': error_message}
            return render(request, template, context)
        else:
            # form submission fail, come back to create request page
            context = {'form': form,
                       'error_message': u'Thông tin không hợp lệ'}
            return render(request, template, context)


@login_required(login_url='/login')
def edit_request(request, request_id):
    """
    update a user request
    :param request:
    :param request_id:
    :return:
    """
    template = "ConvePlatform/edit_request.html"
    error_message = None
    params_json, signature = _generate_signature()

    result = get_request(request_id)
    if not result.success:
        raise Http404

    request_entity = result.data

    #editor is not owner, then reject request
    if request_entity.username != request.user.get_username():
        raise Http404

    if request.method == "GET":
        #render edit page
        form = CreateRequestForm.from_request_entity(request_entity)

        context = {'form': form,
                   'json_assy': params_json,
                   'sign': signature,
                   'item_id': request_id}
        return render(request, template, context)

    if request.method == 'POST':
        #form submission, then process to update
        form = CreateRequestForm(request.POST)

        if form.is_valid():
            request_entity = RequestEntity.create_request_entity(request.user.username, form.cleaned_data['title'],
                                                                 form.cleaned_data['category'],
                                                                 form.cleaned_data['price'],
                                                                 form.cleaned_data['origin_city'],
                                                                 form.cleaned_data['origin_desc'],
                                                                 form.cleaned_data['destination_city'],
                                                                 form.cleaned_data['destination_desc'],
                                                                 form.cleaned_data['description'],
                                                                 form.cleaned_data['img_url'],
                                                                 status=request_entity.status,
                                                                 expired_date=form.cleaned_data['expiry_date'],
                                                                 thumb_url=form.cleaned_data['thumb_url'],
                                                                 price_currency=form.cleaned_data['price_currency'],
                                                                 id=request_id)

            result = update_request(request_entity, request.user.username)
            if result.success:
                return HttpResponseRedirect(reverse('profile-owner'))
            else:
                error_message = u'Hệ thống có lỗi không thể cập nhật giao dịch này!'
        else:
            error_message = u'Form cập nhật có lỗi!'

        context = {'error_message': error_message,
                   'item_id': request_id,
                   'form': form,
                   'json_assy': params_json,
                   'sign': signature}
        return render(request, template, context)


@login_required(login_url='/login')
def delete_request(request):
    """
    update a user request
    :param request:
    :param request_id:
    :return:
    """

    if request.method == "POST":
        request_id = request.POST['id']
        username = request.user.username
        result = delete_request_backend(request_id, username)

        if result.success:
            pass
        else:
            error_message = u'Hệ thống có lỗi không thể cập nhật giao dịch này!'
            print result.message

        return redirect('profile-owner')


@login_required(login_url='/login')
def update_status_request(request, set_active):
    if request.method == "POST":
        request_id = None
        username = None
        new_status = None

        if "id" in request.POST:
            request_id = request.POST["id"]
            username = request.user.username
            result = get_request(request_id)

            if result.success:
                request_entity = result.data
                if set_active:
                    new_status = 1
                else:
                    new_status = 2
                request_entity.status = Enum.REQUEST_STATUS(new_status)
                if request_entity.username == username:
                    result = update_request(request_entity, username)
                    if result.success:
                        return redirect('profile-owner')
                    else:
                        error_message = u'Hệ thống có lỗi không thể cập nhật giao dịch này!'

            else:
                error_message = u'Hệ thống có lỗi không thể cập nhật giao dịch này!'


def detail(request, request_id=None):
    """
    render request detail page

    :param request:
    :param request_id:
    :return:
    """
    template = "ConvePlatform/detail_request.html"

    result = get_request(request_id)
    if result.success:
        request_entity = result.data
        obj = _preprocess_request_entity(request_entity)
        comments = get_comments_by_request(request_id)
        form = PostCommentForm()
        context = {"request": obj, "comments": comments, "form": form}

        return render(request, template, context)

    else:
        raise Http404


@login_required(login_url='/login', message=u'Bạn phải đăng nhập để đăng bình luận!')
def post_comment(request, request_id):
    # process form and add_comment(CommentEntity) to db
    # redirect to detail page on finish
    # if fail, set fail message

    if request.method == "POST":
        form = PostCommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']  #may need to escape string here
            comment = CommentEntity(username=request.user.username, content=content, request_id=request_id)
            result = add_comment(comment)
            if result.success:
                message = u'Đã đăng bình luận'
                messages.success(request, message)
            else:
                message = u'Hệ thống có lỗi không thể đăng bình luận. Vui lòng thử lại'
                messages.error(request, message)
        else:
            message = u'Form Bình luận không hợp lê.'
            messages.error(request, message)

    return redirect('detail-request', request_id=request_id)


@login_required(login_url='/login')
def profile_owner(request):
    """
    render user profile page in owner mode

    :param request:
    :return:
    """

    rendered = _profile(request, owner=True)
    return rendered


def profile_guest(request, username=None):
    """
    render user profile in view mode
    TODO: refactor to join with profile_owner view
    :param username: string viewing account's username
    :param request:
    :return:
    """
    if request.user.is_authenticated() and request.user.username == username:
        # if user access their own profile page, redirecto to owner view mode
        return redirect('profile-owner')

    rendered = _profile(request, username, owner=False)
    return rendered


def _profile(request, username=None, owner=False):
    """
    render personal page
    :param owner: string if user viewing their profile
    :param username: string viewing account's username
    :param request:
    :return:
    """
    template = "ConvePlatform/personal_dashboard.html"

    if owner:
        username = request.user.username

    result = get_AccountEntity_by_username(username)
    if not result.success:
        raise Http404

    items = get_RequestEntity_list_by_username(username)
    if not result.success:
        raise Http404

    items = _preprocess_request_entity_list(items)

    context = {"items": items, "account_entity": result.data, "owner": owner}

    return render(request, template, context)


@login_required(login_url='/login')
def edit_profile(request, mode=1):
    """
    render and process edit profile page
    :param request:
    :return:
    """

    template = "ConvePlatform/edit_profile.html"
    error_message = None
    params_json, signature = _generate_signature('7ce647508e1211e5bb08313767328f2d')
    form = None
    thumb_link = None

    username = request.user.username
    result = get_account(username)
    # if account does not exist, throw 404 page
    if not result.success or not isinstance(result.data, AccountEntity):
        raise Http404
    account_entity = result.data

    if request.method == "GET":
        if mode == 1:
            form = EditProfileForm.from_account_entity(account_entity)
        elif mode == 2:
            form = ChangePasswordForm(user=request.user)
        else:
            raise Http404
        # context = {'thumb_link': account_entity.thumb_link,
        #            'form': form,
        #            'json_assy': params_json,
        #            'sign': signature}
        #
        # return render(request, template, context)

    elif request.method == 'POST':
        #form submission, process to update
        if mode == 1:
            # edit profile form
            form = EditProfileForm(request.POST)

            if form.is_valid():
                data_form = form.cleaned_data
                if email_is_exist_in_other_account(data_form['email'], request.user.username):
                    error_message = u'Email này đã tồn tại trong tài khoản của người khác'
                else:
                    account_entity = AccountEntity(username=username, last_name=data_form['last_name'],
                                                   first_name=data_form['first_name'],
                                                   email=data_form['email'], first_phone=data_form['phone'],
                                                   second_phone=data_form['extra_phone'],
                                                   address=data_form['address'], photo_link=data_form['photo_link'],
                                                   thumb_link=data_form['thumb_link'],
                                                   facebook_link=data_form['facebook_link'],
                                                   description=data_form['description'])
                    result = update_account(account_entity)
                    if result.success:
                        return HttpResponseRedirect(reverse('profile-owner'))
                    else:
                        error_message = u'Hệ thống có lỗi không thể cập nhật!'
            else:
                error_message = u'Form cập nhật có lỗi!'
        elif mode == 2:
            # edit password form
            form = ChangePasswordForm(user=request.user, data=request.POST)

            if form.is_valid():
                password_new = form.cleaned_data.get("password_new")
                result = change_password_by_username(username=username, password=password_new)

                if result.success:
                    return login(request, from_backend=True)
                else:
                    error_message = u'Hệ thống có lỗi không thể cập nhật!'
            else:
                error_message = u'Form cập nhật có lỗi!'
        else:
            # wrong edit mode
            raise Http404
    else:
        # wrong request method
        raise Http404

    context = {'thumb_link': account_entity.thumb_link,
               'error_message': error_message,
               'form': form,
               'json_assy': params_json,
               'sign': signature,
               'mode': mode}
    return render(request, template, context)


# def _generate_mock_request():
#     obj = RequestEntity()
#     obj.title = u'Nem rán hạ long'
#     obj.request_id = "1"
#     obj.account_id = "testuser"
#     obj.description = u'Một món ăn từ Hà nội'
#     obj.category = CATEGORY.Dry
#     obj.price = "5"
#     obj.price_currency = CURRENCY.VND
#     obj.origin_city = CITY.SGN
#     obj.origin_address = u'Kim Tian Place'
#     obj.destination_city = CITY.HAN
#     obj.destination_address = u'Ngã tư sở'
#     obj.image_url = ['http://tmp.transloadit.com.s3.amazonaws.com/063c8d207eff11e5836f973e843a6ac4.jpg']
#     obj.thumb_url = 'http://tmp.transloadit.com.s3.amazonaws.com/06da05a07eff11e58314f1d86b506b8e.jpg'
#     obj.status = REQUEST_STATUS.Active
#     obj.created_date = "27/10/2015 23:45"
#     obj.last_modified_date = "27/10/2015 23:45"
#
#     return obj
#
#
# def _generate_list_mock_request(n):
#     list_obj = []
#     for i in xrange(0, n):
#         list_obj.append(_generate_mock_request())
#     return list_obj


def _preprocess_request_entity(item):
    """
    convert request entity data to ready-for-render format
    :param item: RequestEntity
    :return:
    """
    if item is None:
        return None

    # item.category = item.category.label() if item.category is not None else None
    category=[]
    for element in item.category:
        category.append(element.label())
    item.category = category
    item.price_currency = item.price_currency.label() if item.price_currency is not None else None
    item.origin_city = item.origin_city.label() if item.origin_city is not None else None
    item.destination_city = item.destination_city.label() if item.destination_city is not None else None
    item.status = item.status.value if item.status is not None else None
    return item


def _preprocess_request_entity_list(item_list):
    """
    convert list of request entity data to ready-for-render format
    :param item_list: list of RequestEntity
    :return:
    """
    result = [_preprocess_request_entity(item) for item in item_list]
    return result


def howitwork(request):
    """
    Render Howitwork

    :param request:
    :return:
    """
    template = 'ConvePlatform/howitwork.html'
    context = {}
    return render(request, template, context)


def _generate_signature(template_id="38269e9083c111e5bcf7dd94179bcc0e"):
    """ This function generate a signature for transloadit authentication

    default template_id 38269e9083c111e5bcf7dd94179bcc0e: upload product image
    other options for template_id: 7ce647508e1211e5bb08313767328f2d to upload profile image
    :return:
    """
    # secret key
    secret_key = 'da3526e02eddada4bc4169ede60dbb8eca8bbd7a'

    # Parameters for transloadit
    params = {
        'auth': {
            'expires': (datetime.now() +
                        timedelta(days=1)).strftime('%Y/%m/%d %H:%M:%S'),
            'key': "b85957207a6011e5ba7185d27b0d665c"
        },
        'template_id': template_id,
    }
    json_data = json.dumps(params, separators=(',', ':'))  # create json data dumps

    sign = hmac.new(secret_key, json_data, hashlib.sha1).hexdigest()
    return json_data, sign
