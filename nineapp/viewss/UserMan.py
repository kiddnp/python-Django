# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from nineapp import models


def list(request):
    people_list = models.User.objects.all()
    return render(request, 'show.html', {"people_list": people_list})

