#coding:utf-8
__author__ = 'Haddy Yang(Ysh)'
__start_date__ = '2016-06-12'
"""
    likes views
"""
from django.shortcuts import render
from django.http import HttpResponse
import json

from likes.models import Likes, LikesDetail
from django.contrib.contenttypes.models import ContentType

#导入likes下自定义的装饰器
from likes.decorator import check_login, check_request

@check_login
@check_request('type', 'id', 'direct')
def likes_change(request):
    u"""处理改变点赞状态
        Method: GET
        params: 
            type  : object type
            id    : object id
            direct: -1 or 1 (add like or remove like)
        return: json
    """
    #创建json对象需要的数据
    data = {}
    data['status'] = 200
    data['message'] = u'ok'
    data['nums'] = 0

    try:
        #获取对象模型
        obj_type = request.GET.get('type')
        obj_id = request.GET.get('id')
        user = request.user

        direct = 1 if request.GET.get('direct') == '1' else -1
        c = ContentType.objects.get(model = obj_type)

        #根据模型和id获取likes对象
        ls = Likes.objects.filter(content_type = c, object_id = obj_id)
        if len(ls)==0:
            #没有获取到对象，则新增一个Likes对象
            l = Likes(content_type = c, object_id = obj_id)
        else:
            l = ls[0]
        data['nums'] = l.likes_num

        #判断最近是否赞过，或者取消赞
        details = LikesDetail.objects.filter(likes = l, user = user).order_by('-pub_date')
        if len(details) == 0:
            liked = -1
        else:
            liked = 1 if details[0].is_like else -1

        #方向一致无效，避免多次点赞或者取消
        if liked == direct:
            raise Exception, u'Invalid operation'

        #更新记录
        l.likes_num += direct
        if l.likes_num < 0:
            l.likes_num = 0
        l.save()
        data['nums'] = l.likes_num

        #新增明细
        detail = LikesDetail(likes = l, user = user)
        detail.is_like = direct == 1
        detail.save()

    except Exception, e:
        data['status'] = 403
        data['message'] = e.message

    #返回结果
    return HttpResponse(json.dumps(data), content_type="application/json")

@check_request('type', 'id')
def likes_nums(request):
    u"""单独获取点赞的数量（也可以访问Likes模型获取数量）
        Method: GET
        params: 
            type  : object type
            id    : object id
        return: json
    """
    #创建json对象需要的数据
    data = {}
    data['status'] = 200
    data['message'] = u'ok'
    data['nums'] = 0

    try:
        #获取对象模型
        obj_type = request.GET.get('type')
        obj_id = request.GET.get('id')
        c = ContentType.objects.get(model = obj_type)

        #根据模型和id获取likes对象
        l = Likes.objects.get(content_type = c, object_id = obj_id)

        #获取数量
        data['nums'] = l.likes_num
    except Exception, e:
        data['nums'] = 0

    #返回结果
    return HttpResponse(json.dumps(data), content_type="application/json")