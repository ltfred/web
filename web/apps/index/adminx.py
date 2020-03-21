import xadmin
from xadmin import views
from .models import *


class CarouselXadmin(object):
    list_display = ['article', 'is_active']


class GlobalSetting(object):
    site_title = 'Fred'
    site_footer  = 'Fred'


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(Carousel, CarouselXadmin)