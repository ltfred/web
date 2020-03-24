import xadmin
from .models import *


class LinkXadmin(object):
    list_display = ['id', 'name', 'url']


xadmin.site.register(Link, LinkXadmin)
