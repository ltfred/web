import xadmin
from xadmin import views
from .models import *


class CarouselXadmin(object):
    list_display = ['id', 'article', 'is_active']


class GlobalSetting(object):
    site_title = 'Fred的博客后台管理'
    site_footer = 'Fred的博客后台管理'


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(Carousel, CarouselXadmin)