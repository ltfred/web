from django.db import models

# Create your models here.
from web.utils.base_mode import BaseModel


class Link(BaseModel):

    name = models.CharField(verbose_name='名称', max_length=20, help_text='20字以内')
    url = models.URLField(verbose_name='地址')

    class Meta:
        db_table = 'link'
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name