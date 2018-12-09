# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
import pymysql
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