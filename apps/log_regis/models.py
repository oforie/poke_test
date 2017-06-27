# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render, HttpResponse, redirect
from django.contrib import messages
from django.db import models
import datetime
import re
import bcrypt


context = {}

class UserManager(models.Manager):

    def registrations(self, request):
        # Users.objects.all().delete()
        name = request.POST['name']
        alias = request.POST['alias']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pw = request.POST['confirm_pw']
        dob = request.POST['date']
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        date_regex = '/^(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01])\/(19|20)\d{2}$/'
       
        
        error_count = 0

        if len(alias) < 2:
            error_count += 1
            messages.error(request, 'alias is too short.')
        if len (name) < 2:
            error_count += 1
            messages.error(request, 'First name is too short.')
        if not re.match(regex, email):
            error_count += 1
            messages.error(request, 'please enter a valid email')
        if Users.objects.filter(email = email):
            error_count+=1
            messages.error(request, "email already in use")
        if password != confirm_pw:
            error_count += 1
            messages.error(request, 'Please enter matching passwords.')
        if len(password)< 8:
            error_count+= 1
            messages.error(request, 'Password too short.')
        # if not re.match(date_regex, dob):
        #     error_count +=1
        #     messages.error(request, 'please enter valid date of birth')
        # come back and validate dob
        if error_count < 1:
            reg_password = request.POST['password']
            encoded_pw = reg_password.encode(encoding="utf-8", errors="strict")
            encrypted_pw = bcrypt.hashpw(encoded_pw, bcrypt.gensalt())
            print encoded_pw
            new_user = Users.objects.create(name=name, alias=alias, email=email, password = encrypted_pw)
            request.session['name'] = new_user.name
            request.session['id'] = new_user.id
            print request.session['id']
            print request.session['name'], 'has been successfully registered!'
            return True
        else:
            print "....registration aborted...."
            return False


            #login validations
    def login(self, request):
        email = request.POST['email']
        password_input = request.POST['password']

        try:
            user = Users.objects.filter(email = email)[0]
            # print "Table password", user.password == bcrypt.hashpw(password_input.encode(), user.password.encode())
                # request.session['user_id'] = existing_user.id
            request.session['name'] = user.name
        except:
            messages.info(request, 'Invalid Login')
            return False    
            print "troubleshooting" 


        if bcrypt.hashpw(password_input.encode(), user.password.encode()) == user.password.encode():

            # request.session[ user_id'] = user.id
            request.session['name'] = user.name
            return True
        else:
            messages.info(request, "Invalid Login")
            print "login attempt failed"
            return False

 
    # def pw_hashing(self, postData): 
    #     reg_password = postData
    #     encoded_pw = reg_password.encode(encoding="utf-8", errors="strict")
    #     hashed = bcrypt.hashpw(encoded_pw, bcrypt.gensalt())
    #     return hashed

class Users(models.Model):
    name=models.CharField(max_length=30)
    alias=models.CharField(max_length=30)
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=50)
    dob = models.DateField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.name + ','+ self.alias + ','+ str(self.id) 
    objects=UserManager()

class Traded_pokes(models.Model):
    poker= models.ForeignKey(Users, related_name='pokes')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
