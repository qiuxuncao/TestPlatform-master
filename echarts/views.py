# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
import pymysql
from django.http import JsonResponse
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.decorators import api_view, throttle_classes

# Create your views here.


# def echarts(request):
#     # 下面等价于：select distinct auth,count() as blog_count from cms_blogpost group by auth
#     # auth_count_blog=BlogPost.objects.values('auth').distinct().annotate(blog_count=Count('auth')).all()
#     # print '第1个作者的数量为：', auth_count_blog
#     # auth_count_blog=[{'blog_count': 1, 'auth': u'guchen'}, {'blog_count': 1, 'auth': u'\u6c6a\u5a07'},
#     # {'blog_count': 7, 'auth': u'\u8c37\u6668'}]
#     auth_count_blog = {'blog_count': [10, 15, 20],
#                        'auth': ["grn", "watryto", "zyruhu"]}
#     #  向js中传递数据必须json.dumps()处理
#     return render(request, 'echarts.html', {'auth_count_blog': json.dumps(auth_count_blog)})


def jQuery_get(request):
    res = {"data": "这是后台返回的数据","status": "true"}
    #  向js中传递数据必须json.dumps()处理
    return render(request, 'jQuery_get.html', {'res': json.dumps(res)})

def jQuery_post(request):
    res = {"data": "这是post请求后，后台返回的数据","status": "true"}
    #  向js中传递数据必须json.dumps()处理
    return render(request, 'jQuery_post.html', {'res': json.dumps(res)})

def echarts(request):
    db = pymysql.connect("localhost", "root", "guchen", "guchen_test", charset='utf8')
    cursor = db.cursor()
    sql = "select * from userCaseInfo"
    cursor.execute(sql)
    results = cursor.fetchall()
    print results
    ret = list(results)
    print ret
    users = []
    caseCount = []
    for i in range(ret.__len__()):
        user =ret[i][1]
        print
        users.append(user)
    print users

    for m in range((ret.__len__())):
        caseNo = ret[m][2]
        caseCount.append(caseNo)
    print caseCount
    db.close()
    print 123
    print {'users': users, 'caseCount': caseCount}
    return render(request, "echarts.html", {'caseInfo': json.dumps({'users':users, 'caseCount':caseCount})})
# echart2()


def showcase(request):
    """
    从数据库中读取作者的用例信息，并用于前台可视化展示
    :param request:
    :return:
    """
    db = pymysql.connect("localhost", "root", "guchen", "guchen_test", charset='utf8')
    cursor = db.cursor()
    sql = "select * from userCaseInfo"
    cursor.execute(sql)
    results = cursor.fetchall()
    print results
    # 向js中传递数据必须json.dumps()处理
    return render(request, "showcase.html", {'caseInfo': json.dumps(list(results))})


# showcase()

def case_info(requset):

    return JsonResponse({"code": 200, "msg": "success"})


# 用djangorestframework创建post接口时需要继承APIView
class caseInfo(APIView):

    # 这里必须写请求方式post、get等
    def post(self, requset):

        userCaseInfoId = requset.POST['userCaseInfoId']
        db = pymysql.connect("localhost", "root", "guchen", "guchen_test", charset='utf8')
        cursor = db.cursor()
        sql = "select * from userCaseInfo where id= %s" % userCaseInfoId
        cursor.execute(sql)
        results = cursor.fetchall()
        r=list(results[0])
        print r
        return JsonResponse({"msg": "success","code": 200,
                             'data':{'id':r[0],'name':r[1],'caseCount':r[2],'passCount':r[3],'failCount':r[4]}},
                            content_type="application/json,charset=utf-8")

    def get(self,request):
        '''
        前台访问caseInfoGet接口时调用该方法
        :param request:
        :return: 返回一个json对象，包含用例信息
        '''

        userCaseInfoId = request.GET['userCaseInfoId']
        db = pymysql.connect('localhost','root','guchen','guchen_test',charset='utf8')
        cursor = db.cursor()
        sql = "select * from userCaseInfo where id=%s" % userCaseInfoId
        cursor.execute(sql)
        results = cursor.fetchall()
        r = list(results[0])
        return JsonResponse({
            'code':200,
            'message':'success',
            'data':{
                'id': r[0],
                'name': r[1],
                'caseCount': r[2],
                'passCount': r[3],
                'failCount': r[4]}
        })

