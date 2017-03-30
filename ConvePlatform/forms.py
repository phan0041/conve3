# -*- coding: utf-8 -*-
from django import forms
from datetime import datetime, date

# form error message override
from django.forms import Field, DecimalField
from django.utils.translation import ugettext_lazy

from AccountManagement.views import reset_password, email_is_exist
from Common.Entity.Entity import AccountEntity
from Common.Entity.Enum import *

DecimalField.default_error_messages['invalid'] = "Vui lòng nhập số!"

Field.default_error_messages = {
    'required': "Thông tin bắt buộc!",
    'invalid': 'Thông tin không hợp lệ!'
}


class CreateRequestForm(forms.Form):
    """
    define a contact form class
    """
    # valid if not empty
    SELECT_CITY = (
        ('', '-------'),
        (CITY.SGN.value, CITY.SGN.label()),
        (CITY.HAN.value, CITY.HAN.label()),
        (CITY.HCM.value, CITY.HCM.label()),
        (CITY.OTHER.value, CITY.OTHER.label()),
    )
    SELECT_CATEGORY = (
        (CATEGORY.Dry.value, CATEGORY.Dry.label()),
        (CATEGORY.Wet.value, CATEGORY.Wet.label()),
        (CATEGORY.Other.value, CATEGORY.Other.label()),
    )

    SELECT_CURRENCY = (
        (CURRENCY.SGD.value, CURRENCY.SGD.label()),
        (CURRENCY.VND.value, CURRENCY.VND.label()),
    )

    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': u'Tên hàng'}, ))
    category = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=SELECT_CATEGORY)
    origin_city = forms.CharField(required=True, widget=forms.Select(choices=SELECT_CITY))
    origin_desc = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                'placeholder': u'Địa chỉ nhận hàng. Ví dụ: Số 1 Hùng Vương, Hà Nội'}))
    destination_city = forms.CharField(required=True, widget=forms.Select(choices=SELECT_CITY))
    destination_desc = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                     'placeholder': u'Địa chỉ giao hàng. Ví dụ: Số 1 Orchard Road, Singapore'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    img_url = forms.URLField(required=False, widget=forms.HiddenInput())
    thumb_url = forms.URLField(required=False, widget=forms.HiddenInput())
    img_assembly_id = forms.CharField(required=False, widget=forms.HiddenInput())
    price = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price_currency = forms.CharField(required=False,
                                     widget=forms.Select(choices=SELECT_CURRENCY, attrs={'class': 'form-control'}))
    expiry_date = forms.DateTimeField(required=True, initial=datetime.now().strftime("%m/%d/%Y"),
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_expiry_date(self):
        data = self.cleaned_data['expiry_date']
        if date(data.year, data.month, data.day) < date.today():
            raise forms.ValidationError(u"Ngày chuyển hàng không hợp lệ!")
        return data

    def clean_destination_city(self):
        origin = self.cleaned_data['origin_city']
        dest = self.cleaned_data['destination_city']

        if origin==dest or (origin != str(CITY.SGN.value) and dest != str(CITY.SGN.value)):
            raise forms.ValidationError(u"Điểm đi và điểm đến không được trùng nhau, và một trong hai điểm là Singapore!")
        return dest

    @classmethod
    def from_request_entity(cls, request_entity):
        """
        instantiate form and populate data from request entity
        :param cls: CreateRequestForm
        :param request_entity: RequestEntity
        :return: dict
        """
        img_url, thumb_url = None, None
        category = [cat.value for cat in request_entity.category]

        if len(request_entity.image_url) > 0:
            img_url = request_entity.image_url[0]

        if len(request_entity.thumb_url) > 0:
            thumb_url = request_entity.thumb_url[0]

        data_dict = {
            'title': request_entity.title,
            'category': category,
            'origin_city': request_entity.origin_city.value if request_entity.origin_city is not None else None,
            'origin_desc': request_entity.origin_address,
            'destination_city': request_entity.destination_city.value if request_entity.destination_city is not None else None,
            'destination_desc': request_entity.destination_address,
            'description': request_entity.description,
            'img_url': img_url,
            'thumb_url': thumb_url,
            'price': request_entity.price,
            'price_currency': request_entity.price_currency.value if request_entity.price_currency is not None else None,
            'expiry_date': request_entity.expired_date.strftime("%m/%d/%Y") if request_entity.expired_date is not None else None
        }
        form = cls(data_dict)
        return form


class LoginForm(forms.Form):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ResetPasswordForm(forms.Form):
    username_or_email = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))


class RegistrationForm(forms.Form):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': u'Tên đăng nhập'}, ))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': u'Mật khẩu'}))
    retype_password = forms.CharField(required=True,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                        'placeholder': u'Xác nhận lại mật khẩu'}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': u'Nhập email'}))
    phone = forms.CharField(required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': u'Số điện thoại'}))
    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': u'Họ'}, ))
    first_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': u'Tên và họ đêm'}, ))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if (' ' in username):
            raise forms.ValidationError(u"Tên đăng nhập không được chứa kí tự trắng!")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if (' ' in email):
            raise forms.ValidationError(u"Email không được chứa kí tự trắng!")
        if ('@' not in email):
            raise forms.ValidationError(u"Email không hợp lệ!")
        if (email_is_exist(email)):
            raise forms.ValidationError(u"Email này đã tồn tại trong tài khoản khác")
        return email
    
    def clean_retype_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('retype_password')

        if not password2:
            raise forms.ValidationError(u"Vui lòng nhập lại mật khẩu!")
        if password1 != password2:
            raise forms.ValidationError(u"Xác nhận mật khẩu không khớp!")
        return password2


class EditProfileForm(forms.Form):
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': u'Nhập email'}))
    phone = forms.CharField(required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': u'Số điện thoại chính'}))
    extra_phone = forms.CharField(required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': u'Số điện thoại phụ'}))
    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': u'Họ'}, ))
    first_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': u'Tên và họ đêm'}, ))
    description = forms.CharField(required=False, max_length=250,
                                 widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': u'Đôi dòng giới thiệu về bản thân...'}, ))
    address = forms.CharField(required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': u'Địa chỉ liên lạc'}, ))
    facebook_link = forms.URLField(required=False,
                                  widget=forms.URLInput(attrs={'class': 'form-control',
                                                             'placeholder': u'Đường link đến tài khoảng facebook'}, ))
    photo_link = forms.URLField(required=False, widget=forms.HiddenInput())
    thumb_link = forms.URLField(required=False, widget=forms.HiddenInput())

    @classmethod
    def from_account_entity(cls, account_entity):
        """
        instatiate from with prepopulated data
        :param account_entity: AccountEntity
        :return:
        """
        data_dict = {
            'username': account_entity.username,
            'email': account_entity.email,
            'phone': account_entity.first_phone,
            'extra_phone': account_entity.second_phone,
            'last_name': account_entity.last_name,
            'first_name': account_entity.first_name,
            'address': account_entity.address,
            'facebook_link': account_entity.facebook_link,
            'photo_link': account_entity.photo_link,
            'thumb_link': account_entity.thumb_link,
            'description': account_entity.description,
        }
        form = cls(data_dict)
        return form


class ChangePasswordForm(forms.Form):
    password_old = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': u'Mật khẩu hiện tại'}))
    password_new = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': u'Mật khẩu mới'}))
    retype_password = forms.CharField(required=True,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                        'placeholder': u'Xác nhận lại mật khẩu mới'}))

    def __init__(self, user, data=None):
        self.user = user
        super(ChangePasswordForm, self).__init__(data=data)

    def clean_retype_password(self):
        password1 = self.cleaned_data.get('password_new')
        password2 = self.cleaned_data.get('retype_password')

        if not password2:
            raise forms.ValidationError(u"Vui lòng nhập lại mật khẩu!")
        if password1 != password2:
            raise forms.ValidationError(u"Xác nhận mật khẩu không khớp!")
        return password2

    def clean_password_old(self):
        password = self.cleaned_data.get('password_old', None)
        if not self.user.check_password(password):
            raise forms.ValidationError(u'Mật khẩu hiện tại không chính xác')


class PostCommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'placeholder': u'Nội dung bình luận ...'}))