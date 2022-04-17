# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import viewsets, filters,permissions
from AppModel.serializer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from collections import OrderedDict
from AppModel.models import *
from django.db.models import Avg, Count, Min, Sum
import hashlib,urllib,random,logging,requests,base64
import json,time,django_filters,xlrd,uuid
from rest_framework import status
import time, datetime
import requests,configparser
from AppModel.WXBizDataCrypt import WXBizDataCrypt 
from django.conf import settings
import qrcode,os
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.DEBUG)
handler = logging.FileHandler("./answersysapp.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


conf_dir = settings.CONF_DIR
cf = configparser.ConfigParser()
cf.read(conf_dir)
logger.info("成功加载配置文件 %s " % (conf_dir))

# 内部方法用于返回json消息
# done
def _generate_json_message(flag, message):
    if flag:
        return HttpResponse("{\"error\":0,\"msg\":\""+message+"\"}",
                            content_type='application/json',
                            )
    else:
        return HttpResponse("{\"error\":1,\"msg\":\""+message+"\"}",
                            content_type='application/json',
                            )
@api_view(['GET'])
def get_qrcode(request):
    if request.method == 'GET':
        return render(request, "qrcode.html")                 


@api_view(['POST'])
def create_qrcode(request):
    if request.method == 'POST':
        if request.data["company_name"]:
            try:
                # import pdb;pdb.set_trace()
                cmp_info = CompanyInfo.objects.get(company_name=request.data["company_name"])
                img_path = os.path.split(os.path.realpath(__file__))[0]+"/../media/prcode_image/"+cmp_info.company_name+".jpg"
                qrcode.make("https://brilliantlife.com.cn:8888/admin/").save(img_path)
                cmp_info.prcode_image = "prcode_image/"+cmp_info.company_name+".jpg"
                cmp_info.save()
                context = {'cmp_info':cmp_info} 
                # return render(request,'qrcode.html',context)
                j ={}
                j["error"] = 0
                j["cmp_name"] = cmp_info.company_name
                j["cmp_img"] = "prcode_image/"+cmp_info.company_name+".jpg"
                print(j)
                # import pdb;pdb.set_trace()
                return HttpResponse(json.dumps(j),content_type='application/json',)
                # return HttpResponse("{\"error\":0,\"cmp_name\":\""+cmp_info.company_name+"\",\"cmp_img\":\""+cmp_info.prcode_image+"\"}",
                #                     content_type='application/json',
                #                     )
            except:
                return HttpResponse("{\"error\":1,\"msg\":\"该公司\"}",
                                    content_type='application/json',
                                    )
    

# weixin 登录
@api_view(['POST'])
def weixin_sns(request,js_code):
    if request.method == 'POST':
        APPID = cf.get("WEIXIN", "weixin_appid")
        SECRET = cf.get("WEIXIN", "weixin_secret")
        JSCODE = js_code
        logger.debug("获取appid %s  secret %s" % (APPID,SECRET))
        requst_data = "https://api.weixin.qq.com/sns/jscode2session?appid="+APPID+"&secret="+SECRET+"&js_code="+JSCODE+"&grant_type=authorization_code"
        req = requests.get(requst_data)
        logger.debug("拼接的微信登录url 为 %s" % (requst_data ))
        if req.status_code == 200:
            openid = json.loads(req.content)['openid']
            session_key = json.loads(req.content)['session_key']
            # WeixinSessionKey.objects.update_or_create(weixin_openid=openid,
            #                                         weixin_sessionkey=session_key)
            is_login = "1"
            # user_auth = "0"
            try:
                wsk = WeixinSessionKey.objects.get(weixin_openid=openid)
                wsk.weixin_sessionkey = session_key
                wsk.save()
                userinfo = UserInfo.objects.get(weixin_openid=openid)
                # 增加用户是否已登录
                is_login = "1"
                # user_auth = userinfo.auth
            except WeixinSessionKey.DoesNotExist:
                cwsk = WeixinSessionKey(weixin_openid=openid,weixin_sessionkey=session_key)
                cwsk.save()
                is_login = "0"
            except UserInfo.DoesNotExist:
                return HttpResponse("{\"error\":0,\"msg\":\"登录失败,不存在该用户\",\"openid\":\""+openid+"\",\"is_login\":\""+is_login+"\"}",
                            content_type='application/json',)


            return HttpResponse("{\"error\":0,\"msg\":\"登录成功\",\"openid\":\""+openid+"\",\"is_login\":\""+is_login+"\"}",
                            content_type='application/json',)
        else:
            return Response(_generate_json_message(False,"code 无效"))


# weixin 获取用户信息
@api_view(['POST'])
def weixin_gusi(request):
    if request.method == 'POST':
        appId = cf.get("WEIXIN", "weixin_appid")
        openid = request.POST['openid']
        try:
            sessionKey = WeixinSessionKey.objects.get(weixin_openid=openid).weixin_sessionkey
            encryptedData = request.POST['encryptedData']
            iv = request.POST['iv']
            pc = WXBizDataCrypt(appId, sessionKey)
            res_data = pc.decrypt(encryptedData, iv)
            phone_number = res_data["phoneNumber"]
            # 增加创建用户动作 openid phonenumber nickname
            try:
                # 用户登录时判断用户是否存在
                userinfo = UserInfo.objects.get(weixin_openid=openid)
                # res_data["auth"]= userinfo.auth
            except UserInfo.DoesNotExist:
                # 不存在则创建新用户
                userinfo = UserInfo(weixin_openid=openid,
                                    phone_number=phone_number)
                                    # ,auth="0")
                userinfo.save()
                # res_data["auth"] = "0"
            return HttpResponse(json.dumps(res_data),content_type='application/json')
        except:
            return HttpResponse(json.dumps("{\"error\":1}"),content_type='application/json')


def __weixin_send_message(touser,date3,thing6,phrase1):
    # get access token
    APPID = cf.get("WEIXIN", "weixin_appid")
    SECRET = cf.get("WEIXIN", "weixin_secret")
    get_access_token_request_data = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid="+APPID+"&secret="+SECRET+""
    req_access = requests.get(get_access_token_request_data)
    access_token = json.loads(req_access.content)['access_token']
    body = {
            "access_token":access_token,
            "touser": touser,
            "template_id": cf.get("WEIXIN", "weixin_template_id"),
            "miniprogram_state": cf.get("WEIXIN", "miniprogram_state"),
            "data":{
                "date3": {
                    "value": date3
                },
                "thing6":{
                    "value": thing6
                },
                "phrase1":{
                    "value": phrase1
                }
            }

    }
    requst_data = "https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token="+access_token+""
    response = requests.post(requst_data, data = json.dumps(body))
    logger.info("通知用户 %s  内容为 %s  微信服务器返回结果为 %s" % (touser, json.dumps(body),response.content))
    return 0


# 通过微信id获取用户信息
@api_view(['GET'])
def get_user_info_by_wxid(request,weixin_id):
    if request.method == 'GET':
        userset = UserInfo.objects.filter(weixin_openid=weixin_id)
        serializer = UserInfoSerializer(userset, many=True)
        res_json = {"error": 0,"msg": {
                    "user_info": serializer.data }}
        return Response(res_json)

# 获取试卷信息
@api_view(['GET'])
def get_testpaperinfo(request):
    if request.method == 'GET':
        testpaperset = TestPaperInfo.objects.all()
        serializer = TestPaperInfoSerializer(testpaperset, many=True)
        #获取问题数组
        question_bank_list = serializer.data[0]['pid']
        ret_questionList =[]
        for qb_info in question_bank_list:
            qd_od = _get_questiondetail_by_id(qb_info)
            tmp_json = {}
            tmp_json["id"] = qb_info
            tmp_json["title"] =qd_od["title"]
            tmp_json["type"] = qd_od["qtype"]
            tmp_json["right_answer"] = qd_od["answer"]
            ret_chooseitems =[]
            for i in ["a","b","c","d","e"]:
                if qd_od[i] != '-':
                    ci ={}
                    ci["item_index"] = i.upper()
                    ci["item_content"] = qd_od[i]
                    ret_chooseitems.append(ci)
            tmp_json["chooseItems"] = ret_chooseitems

            ret_questionList.append(tmp_json)
        res_json = {"error": 0,"msg": {
                    "testpaper_info": ret_questionList }}
        return Response(res_json)


def _get_questiondetail_by_id(pid):
    if pid:
        qb_info_set = QuestionBank.objects.filter(id=pid)
        serializer = QuestionBankSerializer(qb_info_set,many=True)
        return serializer.data[0]


@api_view(['GET'])
def get_rankinfo(request):
    if request.method == 'GET':
        rank_info = ExamScore.objects.all().order_by('-score')
        res = []
        for obj in rank_info:
            try:
                user_info = UserInfo.objects.get(user_name=obj.user_name)
            except ObjectDoesNotExist as err:
                logger.error('此员工不在员工列表中，ERR: %s' % err)
                continue
            tmp={}
            tmp['id'] = user_info.user_name
            tmp['tel'] = user_info.phone_number
            tmp['score'] = obj.score
            tmp['img'] = str(user_info.pic_head)
            res.append(tmp)
        #serializer = ExamScoreInfoSerializer(rank_info, many=True)
        res_json = {"error": 0,"msg": {
                    "rankList": res }}
        return Response(json.dumps(res_json))
