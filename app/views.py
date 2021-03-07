from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.db.models import ObjectDoesNotExist

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    template = 'base.html'
    context = {}
    return render(request, template, context)


def login(request):
    """
    login procedure.
    currently combine with ldap and djang default authentication.
    :param request:
    :return:
    """
    template = 'auth/login.html'
    acc = request.POST.get('account')
    pwd = request.POST.get('password')
    context = {}
    user = authenticate(request,
                        username=str(acc),
                        password=pwd)

    if user is not None:
        auth_login(request, user)
        return redirect('index')
    else:
        context['error_msg'] = 'Error for account or password.'
    return render(request, template, context)


@login_required(login_url='/login/')
def logout(request):
    auth_logout(request)
    return redirect('login')
