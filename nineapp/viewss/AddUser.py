# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from nineapp import models


def addUser(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        mail = request.POST.get("mail", None)
        phone = request.POST.get("phone", None)
        models.User.objects.create(username=username, password=password, email=mail, telphone=phone)
        print('展示信息')
        return redirect('show')


