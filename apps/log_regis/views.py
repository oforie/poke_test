# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import redirect, render, HttpResponse, redirect
import bcrypt
from .models import Users, UserManager
import re

context = {}
def index(request):
    try:
        request.session.pop['first_name']
    except:
        return render(request, 'log_regis/index.html')

def show(request):
    user = Users.objects.all()
    context = {
        'Users':user
    }
    return render(request, 'log_regis/show.html', context)

def register(request):
    if Users.objects.registrations(request):
        return redirect('/show')
    else:
        context['messages']=get_messages(request)
        return render(request, 'log_regis/index.html', context)

           
def login(request):
    print "....starting login process"
    if Users.objects.login(request):
        Users.objects.all()
        return redirect('/show')
           
    else:
        print 'failed'
        context['messages']=get_messages(request)
        return redirect('log_regis/index.html', context)

def process(request):
    print request.POST
    request.POST = 1
    request.session['pokes'] = request.POST
    request.session['pokes'] += 1
    return redirect('/show')