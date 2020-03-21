import xadmin
from .models import *


class LinkXadmin(object):
    list_display = ['name', 'url']


xadmin.site.register(Link, LinkXadmin)
