# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
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
import random

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
                # qrcode.make("https://brilliantlife.com.cn:8888/admin/").save(img_path)
                qrcode.make("https://brilliantlife.com.cn:8020/media/qrcode/pages/index/index/"+str(cmp_info.id)).save(img_path)
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
            is_login = "1" #成功 0登录失败，跳转到身份认证
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
            res_data["is_exist"] = "0" #不存在
            # 增加创建用户动作 openid phonenumber nickname
            try:
                # 用户登录时判断用户是否存在
                # userinfo = UserInfo.objects.get(weixin_openid=openid)
                userinfo = UserInfo.objects.get(weixin_openid=openid)
                res_data["is_exist"] = "1"
                return HttpResponse(json.dumps(res_data),content_type='application/json')
            except :
                try:
                    ui = UserInfo.objects.get(phone_number=phone_number)
                    ui.weixin_openid=openid
                    ui.save()
                    res_data["is_exist"] = "1"
                    return HttpResponse(json.dumps(res_data),content_type='application/json')
                except:
                    res_data["is_exist"] = "0"
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


# 获取最后一次提交的成绩
@api_view(['POST'])
def get_answer_result(request):
    if request.method == 'POST':
        if request.data["phone_number"]:
            eslist = ExamScore.objects.filter(phone_number=request.data["phone_number"]).last()
            ans_res ={}
            ans_res["score"]= eslist.score
            if eslist.score == 100:
                # ans_res["hint"]="恭喜您获得满分！您获得1次抽奖机会"
                ans_res["hint"]="恭喜您获得满分！您有机会获得会员日普惠商品一件"
            else:
                ans_res["hint"]="继续努力"
            ans_res["remain"] = _compute_remind_award_num()
            res_json = {"error": 0,"msg": {
                        "answer_result": ans_res }}
            return Response(res_json)

# 交卷接口
@api_view(['POST'])
def submit_paper(request):
    if request.method == 'POST':
        user_phone_number = request.data["phone_number"]
        answer_list = request.data["answers"]
        total_score=100
        right_num = len(json.loads(answer_list))
        wrong_num = 0
        al = json.loads(answer_list)
        for a in al:
            qb_info = QuestionBank.objects.get(id=a["pid"])
            tmp_qb = qb_info.answer
            if len(qb_info.answer) == 1:
                tmp_qb = qb_info.answer[0]
            if tmp_qb == a["answer"]:
                continue
            else:
                total_score = total_score - qb_info.score
                right_num = right_num -1
                wrong_num = wrong_num +1
        if total_score<= 0:
            total_score=0
        logger.info('user phone_number is: %s submit paper' % (user_phone_number))
        try:
            ui = UserInfo.objects.get(phone_number=user_phone_number)
            es = ExamScore(user_name = ui.user_name,
                            phone_number = user_phone_number,
                            company_name = ui.company_name, 
                            score =  total_score,
                            right_num =  right_num,
                            wrong_num =  wrong_num)
            es.save()
            res_json ={}
            res_json["error"]=0
            res_json["msg"]="提交成功"
            return Response(res_json)
        except:
            res_json ={}
            res_json["error"]=0
            res_json["msg"]="未进行手机号认证，请点击手机号登录"
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
        ii=1
        for qb_info in question_bank_list:
            qd_od = _get_questiondetail_by_id(qb_info)
            tmp_json = {}
            tmp_json["id"] = ii
            tmp_json["pid"] = qb_info
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
            ii = ii+1
            ret_questionList.append(tmp_json)
        res_json = {"error": 0,"msg": {
                    "questionList": ret_questionList }}
        return Response(res_json)


def _get_questiondetail_by_id(pid):
    if pid:
        qb_info_set = QuestionBank.objects.filter(id=pid)
        serializer = QuestionBankSerializer(qb_info_set,many=True)
        return serializer.data[0]

# 获取排名
@api_view(['GET'])
def get_rankinfo(request):
    if request.method == 'GET':
        rank_info = ExamScore.objects.all().order_by('-score')
        res = []
        tmp_set = set()
        i=0
        for obj in rank_info:
            i= i+1
            if i > 20:
                break
            if obj.phone_number in tmp_set:
                continue
            try:
                ul = UserInfo.objects.filter(phone_number=obj.phone_number)
                if len(ul)>0:
                    user_info = ul[0]
            except ObjectDoesNotExist as err:
                logger.error('此员工不在员工列表中，ERR: %s' % err)
                continue
            tmp_set.add(obj.phone_number)
            tmp={}
            tmp['id'] = user_info.user_name
            tmp['tel'] = user_info.phone_number
            tmp['score'] = obj.score
            tmp['img'] = str(user_info.pic_head)
            res.append(tmp)
        #serializer = ExamScoreInfoSerializer(rank_info, many=True)
        res_json = {"error": 0,"msg": {
                    "rankList": res }}
        return Response(res_json)


#获取活动数量
@api_view(['GET'])
def get_award_num(request):
    if request.method == 'GET':
        r_num = int(_compute_remind_award_num())
        award_info = ActionInfo.objects.filter(start_time__lte=datetime.datetime.now(),end_time__gte=datetime.datetime.now()).order_by('start_time')
        logger.info('award_info: %s' % award_info.count())
        if award_info.count() == 0:
            res_json = {
                "error":1,
                "msg": "此时间暂无活动。"
            }
            return Response(res_json)
        obj = award_info[0]
        res_json = {
            "error":1,
            "msg": {
                "award": r_num
            }
        }
        return Response(res_json)


# 获取奖品信息
@api_view(['GET'])
def get_award_info(request):
    if request.method == 'GET':
        awardinfoset = AwardInfo.objects.all()
        serializer = AwardInfoSerializer(awardinfoset, many=True)
        res_json = {"error": 0,"msg": {
                    "awardlist": serializer.data }}
        return Response(res_json)


# 获取领奖信息
@api_view(['POST'])
def get_user_award_info(request):
    if request.method == 'POST':
        try:
            phone_number = request.data["phone_number"]
            awards = UserAward.objects.filter(phone_number=phone_number)
            user_info = UserInfo.objects.get(phone_number=phone_number)
            company_info = CompanyInfo.objects.get(company_name=user_info.company_name)
            if awards.count() == 0:
                tmp = {}
                tmp['name'] = user_info.user_name
                tmp['tel'] = user_info.phone_number
                tmp['labour'] = user_info.labour_union
                tmp['company'] = user_info.company_name
                tmp['company_address'] = company_info.company_address
                tmp['company_connect'] = company_info.company_connect
                tmp['company_phone'] = company_info.company_phone
                res_json = {"error": 0,"msg": {"awardInfos": tmp ,"hint": '顶部提示',"noInfoHint": '请联系基层单位联系人更新您的个人信息后才能正常参加活动'}}
                return Response(res_json)
            award = awards[0]
            tmp={}
            tmp['name'] = award.user_name
            tmp['tel'] = award.phone_number
            tmp['labour'] = award.labour_name
            tmp['company'] = award.company_name
            tmp['company_address'] = award.company_address
            tmp['company_connect'] = company_info.company_connect
            tmp['company_phone'] = company_info.company_phone
            res_json = {"error": 0,"msg": {"awardInfos": tmp ,"hint": '顶部提示',"noInfoHint": '请联系基层单位联系人更新您的个人信息后才能正常参加活动'}}
            return Response(res_json)
        except Exception as e:
            logger.error('参数错误.',e)
            res_json = {"error": 0,"msg":  { "awardInfos": {}, "hint": '顶部提示',"noInfoHint": '请联系基层单位联系人更新您的个人信息后才能正常参加活动'} }
            return Response(res_json)


def _compute_remind_award_num():
     # 计算活动一共多少天 total_num 
    aio = ActionInfo.objects.get(action_name='安全月活动第一次')
    total_num = int(aio.active_long)
     # 获取活动每天可领取奖品数量 default_num =1800
    default_num = int(aio.current_award_total)
     # 计算是活动第几天   cd = current_day  - start_day +1
    cd = datetime.date(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day) - aio.start_time
     # 活动剩余天数  remind_day = total_num -cd
    rd = total_num - (cd.days+1)
     # 获取活动共剩余奖品数量 remind_award_num
    total_ra_num = int(aio.current_remind_num)
     # 查看当天剩余奖品   remind_award_num = remind_award_num - 1800*remind_day
    c_r_award_num = total_ra_num - default_num*rd
    return c_r_award_num


# 领取奖品接口
@api_view(['POST'])
def revice_award(request):
    if request.method == 'POST':
        phone_number = request.data["phone_number"]
        award_id = request.data["award_id"]
        apart_id = request.data["apart_id"]
        try:
            if datetime.datetime.now().hour >=9:
                user_info = UserInfo.objects.get(phone_number=phone_number)
                #查看用户是否已经领奖
                try:
                    uif = UserAward.objects.get(phone_number=phone_number)
                    # 如果有领取记录则回复 不能再领
                    res_json = {"error": 0,"msg":"已领奖无法再次领取"}
                    return Response(res_json)
                    # 如果  
                except:
                    # 如果没有领取记录，且当天还有奖品可领
                    if _compute_remind_award_num() > 0 :
                        cpi = CompanyInfo.objects.get(id=apart_id)
                        aw = AwardInfo.objects.get(id=award_id)
                        if int(aw.award_num)>0:
                            ua = UserAward(user_name=user_info.user_name,
                                phone_number=phone_number,
                            company_address=cpi.company_address,
                            company_name=cpi.company_name,
                            award_name=aw.award_name,
                            labour_name=user_info.labour_union,
                            award_image=aw.award_image,
                            is_finished=True)
                            ua.save()
                            # 更新奖品数量
                            aw.award_num = str(int(aw.award_num) -1)
                            aw.save()
                            # 更新活动奖品数量
                            ai = ActionInfo.objects.get(action_name='七一活动')
                            ai.current_remind_num = str(int(ai.current_remind_num) -1)
                            ai.save()
                            res_json = {"error": 0,"msg":"已登记领奖"}
                            return Response(res_json)
                        else:
                            res_json = {"error": 0,"msg":"该奖品今日已无库存"}
                            return Response(res_json) 
                    else:
                        res_json = {"error": 0,"msg":"恭喜您获得满分！活动火热，普惠商品已被领空，请明日在来"}
                        return Response(res_json)
            else:
                res_json = {"error": 0,"msg":"上午9:00才能开抢哦！"}
                return Response(res_json)
        except:
            res_json = {"error": 0,"msg":"领取物品失败，请您扫描二维码参加活动或联系技术人员！"}
            return Response(res_json)


#确认备注信息
@api_view(['POST'])
def submit_user_info(request):
    if request.method == 'POST':
        phone_number = request.data["phone_number"]
        apart_id = request.data["apart_id"]
        try:
            user_info = UserInfo.objects.get(phone_number=phone_number)
            user_info.desc = request.data["remark"]
            user_info.company_name = CompanyInfo.objects.get(id=apart_id).company_name
            user_info.save()
            res_json = {"error": 0,"msg": "提交备注成功","is_update": True}
            return Response(res_json)
        except:
            res_json = {"error": 0,"msg": "提交备注失败"}
            return Response(res_json)

#更新身份信息
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        id_card = request.data["id_card"]
        try:
            user_info = UserInfo.objects.get(id_card=id_card)
            user_info.phone_number = request.data["phone_number"]
            user_info.weixin_openid = request.data["open_id"]
            user_info.save()
            res_json = {"error": 0,"msg": "更新信息成功"}
            return Response(res_json)
        except:
            res_json = {"error": 0,"msg": "后台没有该用户请联系管理员"}
            return Response(res_json)

#更新身份信息
@api_view(['POST'])
def get_award_history(request):
    if request.method == 'POST':
        phone_number = request.data["phone_number"]
        try:
            userawardinfoset = UserAward.objects.filter(phone_number=phone_number)
            serializer = UserAwardInfoSerializer(userawardinfoset, many=True)
            res_json = {"error": 0,"msg": {
                    "awardlist": serializer.data }}
            return Response(res_json)
        except:
            res_json = {"error": 0,"msg": "没有该用户领奖信息"}
            return Response(res_json)

#获取是否在活动时间
@api_view(['GET'])
def is_in_activity_time(request):
    if request.method == 'GET':
        tpi = TestPaperInfo.objects.get(title='五一活动卷')
        ct = datetime.datetime.now().utcnow()
        st = tpi.starttime.replace(tzinfo=None)
        et = tpi.endtime.replace(tzinfo=None)
        if ct.__ge__(st) and ct.__le__(et):
            res_json = {"error": 0,"msg": "活动开始","is_start": True}
            return Response(res_json)
        else:
            res_json = {"error": 1,"msg": "活动尚未开始","is_start": False}
            return Response(res_json)


#是否是会员
@api_view(['POST'])
def is_member(request):
    if request.method == 'POST':
        phone_number = request.data["phone_number"]
        try:
            userinfolist = UserInfo.objects.filter(phone_number=phone_number)
            can_get_prize = True
            try:
                upi = UserPrizeInfo.objects.filter(phone_number=phone_number)
                if len(upi)>0:
                    can_get_prize =False
            except:
                pass
            if len(userinfolist) >0:
                res_json = {"is_member": True,"msg": "success" ,'can_get_prize':can_get_prize}
                return Response(res_json)
            else:
                res_json = {"is_member": False,"msg": "对不起您不是会员，请联系管理员",'can_get_prize':can_get_prize}
                return Response(res_json)
        except:
            res_json = {"is_member": False,"msg": "对不起您不是会员，请联系管理员",'can_get_prize':can_get_prize}
            return Response(res_json)


#判断抽奖结果
@api_view(['POST'])
def get_prize_info(request):
    if request.method == 'POST':
        phone_number = request.data["phone_number"]
        apart_id = request.data["apart_id"]
        pi = PrizeInfo.objects.get(prize_name="百事可乐一包")
        upl = UserPrizeInfo.objects.filter(phone_number=phone_number)
        user_info = UserInfo.objects.get(phone_number=phone_number)
        can_lottery = 1
        if len(upl) > 0:
            can_lottery = 0
        try:
            prize_list=[]
            a ={"id":1,"desc":'中奖了'}
            b ={"id":2,"desc":'谢谢'}
            c ={"id":3,"desc":'中奖了'}
            d ={"id":4,"desc":'谢谢'}
            prize_list.append(a)
            prize_list.append(b)
            prize_list.append(c)
            prize_list.append(d)
            prize_info={"prize_list":prize_list}
            if can_lottery == 1:
                x = random.randint(0,100)
                name = pi.prize_name
                id = 1
                is_prized = True
                if x> int(float(pi.prize_probability)*100) or int(pi.current_remind_num) <=0:
                    name = "谢谢,未中奖"
                    id = -1
                    is_prized = False
                prize_result = {"id":id,"name":name,"img": pi.prize_image.name}
                prize_info={"prize_list":prize_list,'prize_result':prize_result,'can_lottery':can_lottery}
                # 登记中奖信息
                if int(pi.current_remind_num) > 0 :
                    cpi = CompanyInfo.objects.get(id=apart_id)
                    ua = UserPrizeInfo(user_name=user_info.user_name,
                        phone_number=phone_number,
                    company_address=cpi.company_address,
                    company_name=cpi.company_name,
                    prize_name=pi.prize_name,
                    labour_name=user_info.labour_union,
                    is_prized=is_prized)
                    ua.save()
                    # 更新活动奖品数量
                    pi.current_remind_num = str(int(pi.current_remind_num) -1)
                    pi.save()
                else:
                    cpi = CompanyInfo.objects.get(id=apart_id)
                    ua = UserPrizeInfo(user_name=user_info.user_name,
                        phone_number=phone_number,
                    company_address=cpi.company_address,
                    company_name=cpi.company_name,
                    prize_name=pi.prize_name,
                    labour_name=user_info.labour_union,
                    is_prized=is_prized)
                    ua.save()
                return Response({"prize_info":prize_info})
            else:
                prize_result = {"id":1,"name":pi.prize_name,"img": pi.prize_image.name}
                prize_info={"prize_list":prize_list,'prize_result':prize_result,'can_lottery':can_lottery}

        except:
            res_json = {"is_member": False,"msg": "对不起您不是会员，请联系管理员"}
            return Response(res_json)




#获取规则接口
@api_view(['GET'])
def get_rule_info(request):
    data={
    "rule_content": '1.活动时间：2022年7月1日至7月3日（具体时间以微信通知为准）；\n2.参与范围：经开区在库职工；\n3.每人只有一次领取物品机会，当天领完即止；\n4.请扫描本单位专属二维码参加活动，避免信息不匹配造成不能正常参加活动，或者奖品不能送达个人；\n5.普惠物品将送至职工所在单位；\n技术支持：孙照瑛  联系电话：15022746250'
    }
    return Response(data)