from django.contrib import admin
from .models import *
# Register your models here.


class ArticleDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'view_count')

admin.site.register(ArticleDetail, ArticleDetailAdmin)
admin.site.register(ArticleCategory)