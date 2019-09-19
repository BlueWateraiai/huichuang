from django.contrib import admin

# Register your models here.
from huichuangbiotech.models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','date','body','views','is_delete','classify')  # list
    search_fields = ('title',)
    # inlines = [TagInline]  # Inline
    # fieldsets = (
    #     ['Main', {
    #         'fields': ('name', 'email'),
    #     }],
    #     ['Advance', {
    #         'classes': ('collapse',),
    #         'fields': ('age',),
    #     }]
    #
    # )
admin.site.register(ClassifyModel)
admin.site.register(NewsModel,NewsAdmin)
admin.site.register(ProductModel)