# -*- coding:UTF-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page
import datetime
from django.utils.html import format_html
from AppModel import *
from multiselectfield import MultiSelectField


class CompanyInfo(models.Model):
    company_name = models.CharField(max_length=200,verbose_name='公司名字')
    company_address = models.CharField(max_length=200,verbose_name='公司地址')
    company_connect = models.CharField(max_length=200,verbose_name='联系人')
    company_phone = models.CharField(max_length=200,verbose_name='联系电话')
    company_desc = models.CharField(max_length=200,verbose_name='其它描述')
    prcode_image = models.ImageField(u'二维码图片',null=True, blank=True, upload_to='prcode_image') #(一个单位一个二维码,进小程序)
    prcode_url = models.CharField(max_length=200,verbose_name='二维码url')
    
    class Meta:
        verbose_name = '公司信息'
        verbose_name_plural = '公司信息'
    
    def __str__(self):
        return self.company_name


class UserInfo(models.Model):
    gender_choice = [
        ("0", "女"),
        ("1", "男"),
    ]
    nations = [
        ("0","汉族"),
        ("1","回族"),
        ("2","满族"),
    ]
    policy_roles = [
        ("0","党员"),
        ("1","团员"),
        ("2","群众"),
    ]
    user_name = models.CharField(max_length=200,verbose_name='用户名')
    nick_name = models.CharField(max_length=200,verbose_name='微信名')
    gender = models.CharField(max_length=20,verbose_name='性别', choices=gender_choice,default=1)
    nation = models.CharField(max_length=200,verbose_name='民族', choices=nations,default=0)
    policy_role = models.CharField(max_length=20,verbose_name='政治面貌', choices=policy_roles,default=2)
    household = models.CharField(max_length=200,verbose_name='户籍类型',default="非农业")
    is_bd = models.BooleanField(verbose_name='是否八大群体',default="True")
    job_status = models.BooleanField(verbose_name='就业状态',default="True")
    id_card = models.CharField(max_length=200,verbose_name='身份证号')
    phone_number = models.CharField(max_length=200,verbose_name='手机号码')
    mig_worker = models.BooleanField(verbose_name='是否农民工',default="True")
    company_name = models.CharField(max_length=200,verbose_name='单位名称')
    labour_union = models.CharField(max_length=200,verbose_name='所属工会')
    join_union = models.DateField(verbose_name='入会时间',default=datetime.date.today)
    weixin_openid = models.CharField(max_length=200,verbose_name='微信ID')
    pic_head = models.ImageField(u'头像',null=True, blank=True, upload_to='head_image')
    desc = models.CharField(max_length=200,verbose_name='备注',default='-')

    
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
    
    def __str__(self):
        return self.user_name

class QuestionBank(models.Model):
    title = models.TextField('题目')
    qtype = models.CharField('题目类型',choices=(('单选','单选'),('多选','多选'),('判断','判断')),max_length=40)
    a = models.CharField('A选项',max_length=40)
    b = models.CharField('B选项',max_length=40)
    c = models.CharField('C选项',max_length=40)
    d = models.CharField('D选项',max_length=40)
    e = models.CharField('E选项',max_length=40)
    answer = MultiSelectField('答案',choices=(('A','A'),('B','B'),('C','C'),('D','D'),('E','E')),default='A')
    score = models.IntegerField('分值')

    class Meta:
        verbose_name = '题库'
        verbose_name_plural = '题库'


    def __str__(self):
        return '<%s 分:%s>' % (self.score, self.title)


class TestPaperInfo(models.Model):
    title = models.CharField(max_length=200,verbose_name='考卷名称',default='测试卷')
    starttime = models.DateTimeField(verbose_name='开始时间')
    endtime = models.DateTimeField(verbose_name='结束时间')
    examtime = models.IntegerField(verbose_name='考试时长')
    pid = models.ManyToManyField(QuestionBank,verbose_name='考题')
    
    class Meta:
        verbose_name = '试卷'
        verbose_name_plural = '试卷'


#成绩榜
class ExamScore(models.Model):
    user_name =  models.CharField(max_length=200,verbose_name='用户名')
    phone_number = models.CharField(max_length=200,verbose_name='手机号码')
    company_name =  models.CharField(max_length=200,verbose_name='所属公司')
    score =  models.IntegerField(verbose_name='总分')
    right_num =  models.CharField(max_length=200,verbose_name='答对题目')
    wrong_num =  models.CharField(max_length=200,verbose_name='答错题目')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='考试时间')  # 创建时间

# 奖品信息
class AwardInfo(models.Model):
    award_name = models.CharField(max_length=200,verbose_name='奖品名字')
    award_image = models.ImageField(u'奖品图片',null=True, blank=True, upload_to='award_image')
    current_max = models.CharField(max_length=200,verbose_name='当天被选择次数')
    
    class Meta:
        verbose_name = '奖品信息'
        verbose_name_plural = '奖品信息'
    
    def __str__(self):
        return self.award_name


class ActionInfo(models.Model):
    action_name = models.CharField(max_length=200,verbose_name='活动名称')
    start_time = models.DateField(verbose_name='活动开始时间')
    end_time = models.DateField(verbose_name='活动结束时间')
    active_long = models.CharField(max_length=200,verbose_name='活动时长')
    current_award_total = models.CharField(max_length=200,verbose_name='每天可领取奖品份数',default='1800')
    award_total_num = models.CharField(max_length=200,verbose_name='奖品总数')
    current_remind_num = models.CharField(max_length=200,verbose_name='奖品剩余总量')
    
    class Meta:
        verbose_name = '奖品份数管理'
        verbose_name_plural = '奖品份数管理'
    
    def __str__(self):
        return self.action_name

class UserAward(models.Model):
    user_name = models.CharField(max_length=200,verbose_name='用户名')
    phone_number = models.CharField(max_length=200,verbose_name='手机号码')
    labour_name = models.CharField(max_length=200,verbose_name='工会名称')
    company_name = models.CharField(max_length=200,verbose_name='所答考卷单位')
    company_address = models.CharField(max_length=200,verbose_name='单位地址')
    is_finished= models.BooleanField(verbose_name='是否已领奖品',default="False") 
    award_name = models.CharField(max_length=200,verbose_name='奖品信息')
    revice_time = models.DateField(verbose_name='领奖时间',default=datetime.date.today)
    award_image = models.ImageField(u'奖品图片',null=True, blank=True, upload_to='award_image')
    
    class Meta:
        verbose_name = '领奖信息'
        verbose_name_plural = '领奖信息'
    
    def __str__(self):
        return self.user_name


class WeixinSessionKey(models.Model):
    weixin_openid = models.CharField(max_length=200,verbose_name='openid')
    weixin_sessionkey = models.CharField(max_length=200,verbose_name='sessionkey')
    update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')

    class Meta:
        verbose_name = '微信用户SK'
        verbose_name_plural = '微信用户SK'


