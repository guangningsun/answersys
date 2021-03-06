from django.contrib import admin
from answersysapp import views
from django.conf.urls import include, url
from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings
from AppModel import admin as appadmin
from django.views.generic.base import RedirectView

urlpatterns = [
    url('admin/', admin.site.urls),
    path('weixin_sns/<js_code>', views.weixin_sns),
    path('weixin_gusi/', views.weixin_gusi),
    path('get_qrcode/', views.get_qrcode),
    path('create_qrcode/', views.create_qrcode),
    path('get_testpaperinfo/',views.get_testpaperinfo),
    path('get_rankinfo/',views.get_rankinfo),
    path('get_award_num/',views.get_award_num),
    path('get_answer_result/',views.get_answer_result),
    path('submit_paper/',views.submit_paper),
    path('get_award_info/',views.get_award_info),
    path('get_user_award_info/',views.get_user_award_info),
    path('submit_user_info/',views.submit_user_info),
    path('revice_award/',views.revice_award),
    path('register_user/',views.register_user),
    path('get_award_history/',views.get_award_history),
    path('is_in_activity_time/',views.is_in_activity_time),
    path('is_member/',views.is_member),
    path('get_prize_info/',views.get_prize_info),
    path('get_rule_info/',views.get_rule_info),
    
    
    
    

    path('get_user_info_by_wxid/<weixin_id>', views.get_user_info_by_wxid),
    
    re_path(r'^media/(?P<path>.+)$', serve, {'document_root': settings.MEDIA_ROOT}),

] 
 
