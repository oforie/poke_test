# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.shortcuts import render, redirect, HttpResponse

# total_pokes = []

# def index(request):
#     return render(request, 'poke/pokes.html')

# def process(request):
#     poke_count = 0
#     results = Traded_pokes.objects.create(request.POST)
#     if results:
#         poke_count += 1
#         context = {
#             'results':Traded_pokes.objects.all()
#         }
#     total_pokes += 1 
#     return redirect('/')