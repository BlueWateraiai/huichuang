"""
    Author: mushan
    Date: 2018/12/4 18:43
    Version: 1.0
    Describe: 汇创生物公司的 URL 链接
"""

from django.urls import path
from huichuangbiotech import views
from django.conf.urls import url
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('list/', views.view_list, name='list'),
    path('news/', views.news, name='news'),
    path('article/', views.article, name='article'),
    path('job/', views.job, name='job'),
    path('map', views.map, name='map'),
    path('contact/', views.contact, name='contact'),

    # 显示特定招聘主题信息内容
    path('job/(?p<ctopic_id>\d)/', views.jobinfo, name='jobinfo'),
    # 显示特定媒体新闻主题信息内容
    path('news/(?p<ctopic_id>\d)/', views.newsinfo, name='newsinfo'),
    #显示特定产品服务主题信息内容
    path('list/(?p<ctopic_id>\d)/', views.listinfo, name='listinfo'),
    # 显示特定公司信息主题的内容
    path('about/(?p<ctopic_id>\d)/', views.companyinfo, name='companyinfo'),
    # # 显示特定新闻的详情页
    path('newsdeail/(?p<news_id>\d)/', views.article, name='article'),

    # 测试数据库操作
    path('testdb/',views.testdb),
]
