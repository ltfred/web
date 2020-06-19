from django.db import models
from article.models import ArticleDetail
from web.utils.base_mode import BaseModel


class Carousel(BaseModel):
    article = models.ForeignKey(ArticleDetail, on_delete=models.PROTECT)
    is_active= models.BooleanField(verbose_name='是否激活', default=False)

    class Meta:
        db_table = 'carousel'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
