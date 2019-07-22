from django.conf.urls import url
from django.contrib import admin

from nineapp.viewss import Login, AddUser, UserMan
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.hello),
    url(r'^index/$', views.index),
    url(r'^add/$', views.add, name='add'),
    #url(r'^add2/(\d+)/(\d+)/$', views.add2, name='add2'),
    #url(r'^new_add/(\d+)/(\d+)/$', views.add2, name='add2'),
    #url(r'^$', views.index, name='home'),    #http://127.0.0.1:8000
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^aa/$', views.home, name='home'),  #name 可以用于在 templates, models, views中得到对应的网址，相当于“给网址取了个名字”，只要这个名字不变，网址变了也能通过名字获取到。
    #url(r'^add/(\d+)/(\d+)/$', views.add2, name='add2'),
    #url(r'^new_add/(\d+)/(\d+)/$', views.add2, name='add3'),
    url('login/', Login.do_login, name='login'),
    url('home/', Login.home, name='home'),
    url("home/register/", AddUser.addUser, name='register'),
    url('show/', UserMan.list, name='show'),
    url('error/',  Login.error, name='error'),
    url(r'^ajax_add/', views.ajax_add),
    url(r'^ajax_demo1/', views.ajax_demo1),
    url(r'^ajax/',views.ajax_temp),
    url(r'^host$', views.host),
    url(r'temp2/',views.temp3),
    url('ajaxForm/', views.ajaxForm)



]
