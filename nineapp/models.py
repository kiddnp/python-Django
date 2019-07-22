from django.db import models
# coding:utf-8

"""
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
"""

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
        return self.name

class Book(models.Model):
    nid = models.AutoField(primary_key=True)    #AutoField有序整形 IntegerField整形
    title = models.CharField(max_length=32)    #CharField字符
    author = models.CharField(max_length=32)
    publishDate = models.DateField()    #DateField日期类型
    price = models.DecimalField(max_digits=5, decimal_places=2)    #DecimalField浮点型也可以用FloatField

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __unicode__(self):  # __str__ on Python 3
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):  # __str__ on Python 3
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __unicode__(self):  # __str__ on Python 3
        return self.headline

class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title

class User(models.Model):
    username = models.CharField(max_length=20);
    password = models.CharField(max_length=20);
    email = models.EmailField(max_length=50);
    telphone = models.IntegerField();
    CreateTime = models.DateTimeField();
    Last_LoginTime = models.DateTimeField();

class abc(models.Model):
    username = models.CharField(max_length=20);
    password = models.CharField(max_length=20);
    email = models.EmailField(max_length=50);
    telphone = models.IntegerField();
    CreateTime = models.DateTimeField();
    Last_LoginTime = models.DateTimeField();

class Usernew(models.Model):
    username = models.CharField(max_length=50)
    gender = models.BooleanField()

class Userr(models.Model):
    username = models.CharField(max_length=20);
    password = models.CharField(max_length=20);
    email = models.EmailField(max_length=50);
    telphone = models.IntegerField();
    CreateTime = models.DateTimeField();
    Last_LoginTime = models.DateTimeField();
    class Meta:
        db_table = "userr"

#https://www.cnblogs.com/iexperience/p/10001919.html
class Business(models.Model):
    # id
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32, null=True, default="SA")
    # fk = models.ForeignKey('Foo')

class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32, db_index=True)
    ip = models.GenericIPAddressField(protocol="ipv4", db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey(to="Business", to_field='id')

