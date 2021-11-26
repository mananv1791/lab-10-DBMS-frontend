from typing import ContextManager
from django.db import models
from django.http.response import Http404, HttpResponse
from django.shortcuts import render, resolve_url
from django.http import HttpResponse
import numpy

from .models import Customer, HasProRaw, Login, RaisedIssue, RawMaterial, Roles, RolesRoleDesc, Sales, Supplier, User, Product


def homepage(request):
    try:
        models = [User.objects.all(), Customer.objects.all(), HasProRaw.objects.all(), Login.objects.all(), Product.objects.all(), RaisedIssue.objects.all(
        ), RawMaterial.objects.all(), Roles.objects.all(), RolesRoleDesc.objects.all(), Sales.objects.all(), Supplier.objects.all()]

        print(request)
        index = 0
        if(request.POST.get('submit') != None):
            index = int(request.POST.get('dataTable'))

        heading = []
        data = []

        heading = models[index][0].returnHeading()
        for item in models[index]:
            data.append(item.returnAll())

        table = ['User', 'Customer', 'Has Pro Raw', 'Login', 'Product', 'Raised Issue',
                 ' Raw Material', 'Roles', 'Roles Description', 'Sales', 'Supplier']

        context = {
            "table": table,
            "data": data,
            "heading": heading,
            "tableName": table[index]
        }

        return render(request, "index.html", context)
    except:
        return render(request, "404.html")


def mainpage(request):
    return render(request, "homepage.html")


def queryShow(request):
    if request.POST:
        models = [User.objects.all(), Customer.objects.all(), HasProRaw.objects.all(), Login.objects.all(), Product.objects.all(), RaisedIssue.objects.all(
        ), RawMaterial.objects.all(), Roles.objects.all(), RolesRoleDesc.objects.all(), Sales.objects.all(), Supplier.objects.all()]

        index = 0
        if(request.POST.get('submit') != None):
            index = request.POST.get('showTable')
        print(index)
        user = models[int(index)]
        Data = []

        for item in user:
            Data.append(item.returnAll())
        # print(userData)
        tableName = ""
        inputName = ""
        if(request.POST.get('submit') != None):
            inputName = request.POST.get('inputName')

        for _ in user:
            if(inputName == str(_)):
                match = _
                break
        print(match.returnAll())

        context = {
            "name": match.returnAll(),
            "heading": match.returnHeading(),
        }
        return render(request, "query.html", context)

    return render(request, "query.html")
