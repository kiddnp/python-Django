from django import forms


class AddForm(forms.Form):
    aa = forms.IntegerField()     #表单内容用来接收整形，并且验证通过后，会将这个字段的值转换为整形
    b = forms.IntegerField()