from django.contrib import admin

# Register your models here.
from huichuangbiotech.models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','date','body','views','is_delete','classify')  # list
    search_fields = ('title',)



admin.site.register(ClassifyModel)
admin.site.register(NewsModel,NewsAdmin)
admin.site.register(ProductModel)
admin.site.register(CTopic)
admin.site.register(CompanyInfoModel)