from django.db import models

# Create your models here.


class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        abstract = True

# 主题类
class ClassifyModel(BaseModel):
    slug = models.SlugField()
    classify = models.CharField(verbose_name='分类', max_length=10, unique=True)

# 新闻内容类
class NewsModel(BaseModel):
    status = (
        (0, '显示'),
        (1, '隐藏'),
    )

    title = models.CharField(verbose_name='标题', max_length=100, unique=True)
    author = models.CharField(verbose_name='作者', max_length=20)
    date = models.DateTimeField(verbose_name='发布时间')
    body = models.TextField(verbose_name='内容')
    views = models.IntegerField(verbose_name='浏览次数', default=0)
    is_delete = models.BooleanField(verbose_name='状态', default=False, choices=status)
    classify = models.ForeignKey(to='ClassifyModel', on_delete=models.CASCADE, verbose_name='分类')

# 产品类
class ProductModel(BaseModel):
    choices = (
        ('product', '产品'),
        ("service", '服务'),
        ('equipment', '设备'),
    )
    product = models.CharField(verbose_name='名称', max_length=30, unique=True)
    details = models.TextField(verbose_name='详情')
    classify = models.CharField(verbose_name='分类', max_length=10, choices=choices)



class CTopic(models.Model):
    """公司信息的相关主题"""
    text = models.CharField(max_length=200, unique=True)#由字符或文本组成的数据

# 公司信息类
class CompanyInfoModel(models.Model):
    """关联公司信息主题的具体内容"""
    ctopic = models.ForeignKey(CTopic, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=600)  # 由字符或文本组成的数据
    pic = models.ImageField(upload_to='upload')