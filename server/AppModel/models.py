# -*- coding:UTF-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page
import datetime
from django.utils.html import format_html
from AppModel import *


# class UserInfo(models.Model):
#     AUTH_CHOICES = [
#     ('0', '员工'),
#     ('1', '主管'),
#     ('2', '主任'),
#     ('3', '管理员'),
#     ]
#     nick_name = models.CharField(max_length=200,verbose_name='微信名')
#     user_name = models.CharField(max_length=200,verbose_name='用户名')
#     weixin_openid = models.CharField(max_length=200,verbose_name='微信ID')
#     phone_number = models.CharField(max_length=200,verbose_name='手机号')
#     auth = models.CharField(max_length=200, choices=AUTH_CHOICES,verbose_name='用户权限')
#     address = models.CharField(max_length=200,verbose_name='常用地址')

#     class Meta:
#         verbose_name = '用户信息'
#         verbose_name_plural = '用户信息'
    
#     def __str__(self):
#         return self.user_name

