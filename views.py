import json
import urllib
import urllib.request
import epoch
from PIL import Image
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import F
from django.views.generic import View

from .models import *


def index(request):
    portfolio = Portfolio.objects.filter().order_by('created_date')
    return render(request, 'web/index.html', locals())


def handler404(request, exception):
    return render(request, 'web/404.html', locals())


# def handler500(request, exception):
#     return render(request, '505.html', locals())


def team(request):
    team_type = TeamType.objects.filter().order_by('created_date')
    team_members = TeamMembers.objects.filter().order_by('created_date')
    return render(request, 'web/team.html')


def portfolio(request):
    params = {}
    sector = Sector.objects.filter().order_by('created_date')
    params.update({'tag_id': 4})
    portfolios = Portfolio.objects.filter().order_by('created_date')
    banner = PortfolioBanner.objects.all()

    end_date =
    str(end_date)
    c = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    start_date = Portfolio.objetcs.get('start_date')
    str(start_date)
    b = datetime.datetime.strptime(start_date, '%Y-%m-%d')

    current_date = Portfolio.objetcs.get('current_date')
    str(current_date)
    a = datetime.datetime.strptime(current_date, '%Y-%m-%d')
    # calculating ongoing progress

    x = b - a
    y = c - a
    p = (y * 100) / x

    return render(request, 'web/portfolio.html', {
        'p': p
    }, locals())


# a = datetime.datetime.strptime(startdate, '%Y-%m-%d')
# b = datetime.datetime.strptime(enddate, '%Y-%m-%d')
# c = datetime.datetime.strptime(currdate, '%Y-%m-%d')
#
# x = b - a
# y = c - a
#
# p = (y * 100 ) / x
#
# print(a.timestamp())
# print(b.timestamp())
# print(c.timestamp())
# print(x)
# print(y)
# print(p)