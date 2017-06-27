# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..log_regis.models import Users

# # Create your models here.
# class Traded_pokes(models.Model):
#     poker= models.ForeignKey(Users, related_name='pokes')
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)

   
# def index(request):
#     return render(request, 'pokes/index.html')

# def poking(request):
#         results = Users.Traded_pokes.create(request.POST)
#         print results
#         return redirect('/')
  