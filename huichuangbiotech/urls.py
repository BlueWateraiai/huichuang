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
    path('product/', views.product, name='product'),
    path('service/', views.service, name='service'),
    path('equipment/', views.equipment, name='equipment'),
    path('news/', views.news, name='news'),
    path('article/', views.article, name='article'),
    path('job/', views.job, name='job'),
    path('map', views.map, name='map'),

    # 显示特定新闻的详情页
    path('news/(?p<news_id>\d)/$', views.article, name='article'),

    # 测试数据库操作
    path('testdb/',views.testdb),
]
