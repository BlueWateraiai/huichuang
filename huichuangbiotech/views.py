from django.shortcuts import render
from django.http import HttpResponse
from huichuangbiotech.models import *
# Create your views here.


def query():
    newslist = NewsModel.objects.all()
    context = {'newslist': newslist}
    return context

def index(request):

    return render(request, 'index.html',query())


def about(request):
    return render(request, 'about.html',query())


def view_list(request):
    return render(request, 'list.html',query())


def product(request):
    return render(request, 'product.html',query())


def service(request):
    return render(request, 'service.html',query())


def equipment(request):
    return render(request, 'equipment.html',query())


def news(request):
    return render(request, 'news.html',query())


def article(request, news_id):
    """显示单个新闻的详细内容"""
    new = NewsModel.objects.get(id=news_id)
    context = {'new': new}
    return render(request, 'article.html', context)


def job(request):
    return render(request, 'job.html', query())


def map(request):
    return render(request, 'map.html',query())


# test------------------
# 数据库操作
def testdb(request):
    test1 = ClassifyModel(slug='test2',classify='test2')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")