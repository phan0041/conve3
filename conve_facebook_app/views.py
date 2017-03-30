from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext



def login(request):
     context = RequestContext(request, {
         'request': request, 'user': request.user})
     return render_to_response('login.html', context_instance=context)



@login_required(login_url='/login')
def home(request):
    context = RequestContext(request, {
         'request': request, 'user': request.user, 'id':request.user.id, 'shipperrecord':request.user.shipperrecord_set.all()}
                             )
    return render_to_response('home.html', context_instance=context)


def logout(request):
    auth_logout(request)
    return redirect('/')
