# -*- coding:UTF-8 -*-
from django.contrib import admin
from AppModel.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin
import logging,json,datetime
from django.utils.html import format_html
from django import forms
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page
from django.utils.html import format_html,escape, mark_safe
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import time
import decimal


logger = logging.getLogger(__name__)
logger.setLevel(level = logging.DEBUG)
handler = logging.FileHandler("./answersysapp.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# 公司管理
@admin.register(CompanyInfo)
class CompanyInfoAdmin(ImportExportModelAdmin): 
    list_display=['company_name','company_address','company_connect','company_phone','company_desc','prcode_image','prcode_url']
    search_fields =('company_name','company_address','company_connect','company_phone','company_desc','prcode_image','prcode_url')
    fieldsets = [
       ('用户数据', {'fields': ['company_name','company_address','company_connect','company_phone','company_desc','prcode_image','prcode_url'], 'classes': ['']}),
    ]
    list_per_page = 15

# 用户管理
@admin.register(UserInfo)
class UserInfoAdmin(ImportExportModelAdmin): 
    list_display=['user_name','gender','nation','policy_role','household','is_bd','job_status','id_card','phone_number','mig_worker','company_name','labour_union','join_union']
    search_fields =('user_name','gender','nation','policy_role','household','is_bd','job_status','id_card','phone_number','mig_worker','company_name','labour_union','join_union')
    fieldsets = [
       ('用户数据', {'fields': ['user_name','gender','nation','policy_role','household','is_bd','job_status','id_card','phone_number','mig_worker','company_name','labour_union','join_union'], 'classes': ['']}),
    ]
    list_per_page = 15    


# 奖品管理
@admin.register(AwardInfo)
class AwardInfoAdmin(ImportExportModelAdmin): 
    list_display=['award_name','award_image','current_max']
    search_fields =('award_name','award_image','current_max')
    fieldsets = [
       ('用户数据', {'fields': ['award_name','award_image','current_max'], 'classes': ['']}),
    ]
    list_per_page = 15 


# 题库管理
@admin.register(QuestionBank)
class QuestionBankAdmin(ImportExportModelAdmin): 
    list_display=['title','qtype','a','b','c','d','e','answer','score']
    search_fields =('title','qtype','a','b','c','d','e','answer','score')
    fieldsets = [
       ('用户数据', {'fields': ['title','qtype','a','b','c','d','e','answer','score'], 'classes': ['']}),
    ]
    list_per_page = 15 

# 考卷管理
@admin.register(TestPaperInfo)
class TestPaperInfoAdmin(admin.ModelAdmin): 
    list_display=['title','starttime','endtime','examtime']
    search_fields =('title','starttime','endtime','examtime')
    fieldsets = [
       ('用户数据', {'fields': ['title','starttime','endtime','examtime','pid'], 'classes': ['']}),
    ]
    list_per_page = 15

# 员工成绩管理
@admin.register(ExamScore)
class ExamScoreAdmin(admin.ModelAdmin): 
    list_display=['user_name','company_name','score','right_num','wrong_num']
    search_fields =('user_name','company_name','score','right_num','wrong_num')
    fieldsets = [
       ('用户数据', {'fields': ['user_name','company_name','score','right_num','wrong_num'], 'classes': ['']}),
    ]
    list_per_page = 15


@admin.register(ActionInfo)
class ActionInfoAdmin(admin.ModelAdmin): 
    list_display=['start_time','end_time','active_long','current_award_total','award_total_num','current_remind_num']
    search_fields =('start_time','end_time','active_long','current_award_total','award_total_num','current_remind_num')
    fieldsets = [
       ('用户数据', {'fields': ['start_time','end_time','active_long','current_award_total','award_total_num','current_remind_num'], 'classes': ['']}),
    ]
    list_per_page = 15
     

# 领奖管理
@admin.register(UserAward)
class UserAwardAdmin(admin.ModelAdmin): 
    list_display=['user_name','company_name','answer_exam_name','is_finished','award_name']
    search_fields =('user_name','company_name','answer_exam_name','is_finished','award_name')
    fieldsets = [
       ('用户数据', {'fields': ['user_name','company_name','answer_exam_name','is_finished','award_name'], 'classes': ['']}),
    ]
    list_per_page = 15

    
admin.site.site_title = "泰达智慧群团"
admin.site.site_header = "泰达智慧群团1.0.1"


