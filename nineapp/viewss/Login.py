# encoding:utf-8

from django.shortcuts import render, redirect
from nineapp.models import User
"""
def home(request):
    return render(request, 'index.html')
"""

def do_login(request):
    if request.method == "POST":
        username = request.POST.get('usernamee', None)  #第二个username是html里写的name="username",如果html里改成aa，这就是aa
        user = User.objects.get(username = username)
        if user.username == None:
            return redirect('error')
        elif user.username == username :
            return redirect('home')
    elif request.method == 'GET':  #在urls里面url('login/', Login.do_login, name='login')调用到
        return render(request, 'login.html')

def home(request):
    return render(request, 'index.html')

def error(request):
    return render(request, 'error.html')







