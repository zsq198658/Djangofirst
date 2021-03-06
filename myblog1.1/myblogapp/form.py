# coding:utf-8

from django import forms
from myblogapp.models import UserInfo, User


class GetLoginForm(forms.Form):
    username = forms.CharField(label='账号', max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入账号'}))
    password = forms.CharField(label='密码', max_length=200,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))


class GetRegForm(forms.Form):
    username = forms.CharField(label='账号', max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入账号'}))
    password1 = forms.CharField(label='密码', max_length=200,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))
    password2 = forms.CharField(label='请再输入一次密码', max_length=200,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请再输入一次密码'}))


class UserInfoForm(forms.Form):
    class Meta:
        model = UserInfo
        fields = '__all__'
