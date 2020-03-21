import xadmin
from .models import *

class UserXadmin(object):
    list_display = ['nickname', 'email']


# xadmin.site.register(Users, UserXadmin)