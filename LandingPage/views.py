from django.shortcuts import render
from models import Record, Email
import gSheet_services
from datetime import datetime
from django.http import HttpResponse
from django.core.validators import validate_email
import gSheet_services
from datetime import datetime
from django.shortcuts import render, get_object_or_404, render_to_response
# from forms import ShipperRecordForm, ShipperRecordDeleteForm
from django.http import HttpResponseRedirect, HttpResponseForbidden
# from django import forms
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from LandingPage import general_util

from django.utils.crypto import get_random_string

def IndexView(request):
    template_name   = 'LandingPage/index.html'
    # gSheet_services.update_data()
    shipper_list_fromHN     = Record.objects.filter(direction='#fromHN', is_checked=True, date__gt=datetime.now()).order_by('date')
    shipper_list_fromHCM    = Record.objects.filter(direction='#fromHCM', is_checked=True, date__gt=datetime.now()).order_by('date')
    shipper_list_toHN       = Record.objects.filter(direction='#toHN', is_checked=True, date__gt=datetime.now()).order_by('date')
    shipper_list_toHCM      = Record.objects.filter(direction='#toHCM', is_checked=True, date__gt=datetime.now()).order_by('date')

    # generate token for form
    request.session['token'] = generateToken()

    context = {'shipper_list_fromHN': shipper_list_fromHN,
               'shipper_list_fromHCM': shipper_list_fromHCM,
               'shipper_list_toHN': shipper_list_toHN,
               'shipper_list_toHCM': shipper_list_toHCM,
               'token': request.session['token'],
               }
    return render(request, template_name, context)


def submit(request):
    string = request.GET.get("email", "")
    string_type = request.GET.get("type", "")

    # check token #
    token = request.GET.get("nonce", "")
    if "token" not in request.session:
        return HttpResponse("Invalid token")
    elif token != request.session['token']:
        return HttpResponse("Invalid token")
    else:   #valid token
        del request.session['token']

    if len(Email.objects.filter(email=string)) == 0 and general_util.validate_register_email(string):
        email = Email()
        gSheet_services.add_email(string, string_type)
        email.email = string
        email.save()
        return HttpResponse("Success")
    else:
        if not general_util.validate_register_email(string):
            return HttpResponse("Error")
        else:
            return HttpResponse("Dup")


def generateToken():
    return get_random_string(length=32)


def ShipperView(request):
    template_name = 'LandingPage/shipper.html'
    context = {}
    return render(request, template_name, context)

def SignupView(request):
    template_name = 'LandingPage/signup.html'
    context = {}
    return render(request, template_name, context)

def ContactView(request, question_id):
    template_name = 'LandingPage/contact.html'
    context = {
        'question_id': question_id
    }
    return render(request, template_name, context)

# def TestView(request):
#     template_name = 'LandingPage/test_fblogin.html'
#     context = {}
#     return render(request, template_name, context)
# #
# @login_required(login_url='/login')
# def DeleteRecord(request, id=None,template_name='delete-confirmation.html'):
#     if id:
#         record = get_object_or_404(ShipperRecord, pk=id)
#         if record.user != request.user:
#             return HttpResponseForbidden()
#     if request.method == 'POST':
#         if 'cancel' in request.POST:
#             return HttpResponseRedirect('/home')
#         form = ShipperRecordDeleteForm(request.POST, instance=record)
#         if form.is_valid():
#             record.delete()
#             return HttpResponseRedirect('/home')
#     else:
#         form = ShipperRecordDeleteForm()
#
#     return render_to_response(template_name, {
#         'form': form,
#         }, context_instance=RequestContext(request))


#
# @login_required(login_url='/login')
# def GetRecord(request, id=None, template_name='submit.html'):
#     if 'cancel' in request.POST:
#         return HttpResponseRedirect('/home')
#     if id:
#         record = get_object_or_404(ShipperRecord, pk=id)
#         if record.user != request.user:
#             return HttpResponseForbidden()
#     else:
#         record = ShipperRecord(user=request.user)
#
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = ShipperRecordForm(request.POST or None, instance=record)
#
#         # check whether it's valid:
#         if form.is_valid():
#             form.save()
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/home/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = ShipperRecordForm(instance=record)
#
#     return render_to_response(template_name, {
#         'form': form,
#         }, context_instance=RequestContext(request))


