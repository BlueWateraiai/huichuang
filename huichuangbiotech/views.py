from django.shortcuts import render
from django.http import HttpResponse
from huichuangbiotech.models import *
from django.core.paginator import Paginator
import math
# Create your views here.


def query():
    """返回一定数量的新闻"""
    newslist = NewsModel.objects.all()[1:5]
    context = {'newslist': newslist}
    return context

    # """ctopic_id 数字代表主题的意义
    #    1 公司简介 2 公司文化 3 品牌与资质 4 资源与优势 6 葡萄糖浆系 7 麦芽糖浆系 8果葡糖浆系 9低温挤出酶解糖浆原料 10 酒精原料生产淀粉糖工艺 11 酒精原料生产酒精工艺 12单螺杆挤压设备 13技术研究推广 14 招聘信息
    #    15应聘指南 16 员工培训 17 生涯规划 18人才政策 19 人才战略
    # """
def companyinfo(request, ctopic_id):
    """显示单个公司信息主题的所有内容"""
    newslist = NewsModel.objects.all()[1:5]
    ctopic = CTopic.objects.get(id=ctopic_id)
    infolist = ctopic.companyinfomodel_set.all()
    context = {'infolist':infolist, 'newslist':newslist, 'ctopic':ctopic}
    return render(request, 'about.html', context)

def listinfo(request, ctopic_id):
    """显示特定产品服务主题信息内容"""
    newslist = NewsModel.objects.all()[1:5]
    ctopic = CTopic.objects.get(id=ctopic_id)
    infolist = ctopic.companyinfomodel_set.all()
    context = {'infolist':infolist, 'newslist':newslist, 'ctopic':ctopic}
    return render(request, 'list.html', context)

def newsinfo(request, ctopic_id):
    """显示特定媒体新闻主题信息内容"""

    """规定分页的信息"""
    # pagesize = 2
    # total = NewsModel.objects.all().count()
    # pagenumber = math.ceil(total/pagesize)
    # pagelist = range(1, pagenumber+1)
    # start = (page_id-1)*pagesize
    # end = page_id*pagesize
    # newslist = NewsModel.objects.order_by('title')[start:end]
    """配置django自带的分页功能"""
    newslist = NewsModel.objects.all()[1:5]
    list = NewsModel.objects.all()
    paginator = Paginator(list, 6)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    listnumber = range(1,contacts.paginator.num_pages+1)
    ctopic = CTopic.objects.get(id=ctopic_id)
    infolist = ctopic.companyinfomodel_set.all()
    context = {'infolist':infolist, 'contacts':contacts, 'ctopic':ctopic, 'listnumber':listnumber, 'newslist':newslist}
    return render(request, 'news.html', context)

def jobinfo(request, ctopic_id):
    """显示特定招聘主题信息内容"""
    newslist = NewsModel.objects.all()[1:5]
    ctopic = CTopic.objects.get(id=ctopic_id)
    infolist = ctopic.companyinfomodel_set.all()
    # 从数据库读取正文替换信息
    # for info in infolist:
    #     info.text = info.text.replace("\\n", "\n")
    context = {'infolist':infolist, 'newslist':newslist, 'ctopic':ctopic}
    return render(request, 'job.html', context)

def article(request, news_id):
    """显示单个新闻的详细内容"""
    new = NewsModel.objects.get(id=news_id)
    newslist = NewsModel.objects.all()[1:5]
    context = {'new': new,'newslist':newslist}
    return render(request, 'article.html', context)


# test------------------
# 数据库操作
def testdb(request):
    test1 = ClassifyModel(slug='test2',classify='test2')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def index(request):
    return render(request, 'index.html',query())

def about(request):
    return render(request, 'about.html', query())

def view_list(request):
    return render(request, 'list.html',query())

def contact(request):
    return render(request, 'contact.html', query())

def news(request):
    return render(request, 'news.html',query())

def job(request):
    return render(request, 'job.html', query())

def map(request):
    return render(request, 'map.html',query())


