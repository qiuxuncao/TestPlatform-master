# coding:utf-8
"""TestPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from echarts.views import echarts
from echarts.views import showcase
# from echarts.views import echarts2
from echarts.views import jQuery_get
from echarts.views import jQuery_post
from echarts.views import case_info
from echarts.views import caseInfo
# 用于生成接口文档
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^echarts/', echarts),
    url(r'^jQuery_get/', jQuery_get),
    url(r'^jQuery_post/', jQuery_post),
    # url(r'^echarts2/', echarts2),
    url(r'^showcase/', showcase),
    url(r'^caseInfo/', case_info),
    url(r'^caseInfoPost', caseInfo.as_view()),
    url(r'^caseInfoGet', caseInfo.as_view()),
    url(r'docs/', include_docs_urls(title="guchen")),
]
