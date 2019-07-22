from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# 引入我们创建的表单类
from .forms import AddForm
import json
from nineapp.models import Host,Business
from nineapp.models import Usernew
from django.shortcuts import render, redirect
import json


def hello(request):
    return HttpResponse("第九次")

#def index(request):
#    return HttpResponse(u"欢迎光临 第九次!")
def index(request):
    return render(request, 'index.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))
"""
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))
"""

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
"""
def index(request):
    return render(request, 'home.html')    #这里的nineapp是指templates下的
"""
"""
def home(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home2.html', {'TutorialList': TutorialList})
"""
"""

def index(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据
        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['aa']     #cleaned_data中对应的值都必须按照model中定义的字段类型取值，否则校验不通过或保存时报错
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})

"""
def ajax_demo1(request):
    return render(request, "ajax_demo1.html")

def ajax_add(request):
    #time.sleep(10)  #不影响页面发送其他的请求
    i1 = int(request.GET.get("i1"))
    i2 = int(request.GET.get("i2"))
    ret = i1 + i2
    return JsonResponse(ret, safe=False)
    #return render(request,'index.html')  #返回一个页面没有意义，就是一堆的字符串，拿到了这个页面，你怎么处理，你要做什么事情，根本就没有意义

def ajax_temp(request):
    return render(request, "ajax_temp.html")
"""

#https://blog.csdn.net/huangql517/article/details/81259011
def temp(request):
    if request.method=="post":
        print(request.body)
        print(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        login_states={'user':None,'error_msg':None}
        if username=="pangchao" and password=='123':
            login_states['user']=username
        else:
            login_states['erro_msg']='username or password is wrong!'
        return HttpResponse(json.dumps(login_states))
    return render(request, "temp.html")
"""
def host(request):
    if request.method == "GET":
        v1 = Host.objects.filter(nid__gt=0)
        v2 = Host.objects.filter(nid__gt=0).values('nid', 'hostname', 'b_id', 'b__caption')
        v3 = Host.objects.filter(nid__gt=0).values_list('nid', 'hostname', 'b_id', 'b__caption')

        b_list = Business.objects.all()

        return render(request, 'host.html', {'v1': v1, 'v2': v2, 'v3': v3, 'b_list': b_list})

    elif request.method == "POST":

        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        # models.Host.objects.create(hostname=h,
        #                            ip=i,
        #                            port=p,
        #                            b=models.Business.objects.get(id=b)
        #                            )
        Host.objects.create(hostname=h,
                                   ip=i,
                                   port=p,
                                   b_id=b
                                   )
        #return redirect('/host')
        return render(request, 'host.html')

###########################################################3
from django.shortcuts import render, redirect, HttpResponse
from django import forms
from django.forms import widgets
import json


class AjaxForm(forms.Form):
    username = forms.CharField(
        required=True,
        min_length=3,
        error_messages={
            "min_length": "用户名输入不正确",
        }
    )
    gender = forms.BooleanField(
        widget=widgets.RadioSelect(choices=[(0, "男"), (1, "女"), ]),
        required=False
    )

def ajaxForm(request):
    if request.method == "GET":
        user = AjaxForm()
        print("999 ")
        return render(request, "temp2.html", {"user": user})
    else:
        ret = {"status": "NG", "msg": None}
        af = AjaxForm(request.POST)
        if af.is_valid():
            print(af.cleaned_data)
            Usernew.objects.create(**af.cleaned_data)
            ret["status"] = "OK"
            return HttpResponse(json.dumps(ret))
        else:
            print("NG")
            ret["msg"] = af.errors
            return HttpResponse(json.dumps(ret))

def temp3(request):
    return render(request, "temp2.html")

