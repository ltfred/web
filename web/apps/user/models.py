from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    nickname = models.CharField(verbose_name='用户昵称', max_length=20)
    avatar = models.URLField(verbose_name='用户头像')

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname