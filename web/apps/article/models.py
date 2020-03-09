from django.db import models

# Create your models here.
from mdeditor.fields import MDTextField

from user.models import Users
from web.utils.base_mode import BaseModel


class ArticleDetail(BaseModel):
    author = models.ForeignKey(Users, on_delete=models.PROTECT, related_name='user')
    title = models.CharField(verbose_name='文章标题', max_length=50, help_text='50字以内')
    category1 = models.ForeignKey('ArticleCategory', on_delete=models.PROTECT, related_name='category1')
    category2 = models.ForeignKey('ArticleCategory', on_delete=models.PROTECT, related_name='category2')
    cover = models.URLField(verbose_name='文章封面')
    content = MDTextField(verbose_name='文章内容')
    view_count = models.IntegerField(verbose_name='浏览量', default=0)
    digg_count = models.IntegerField(verbose_name='点赞数', default=0)
    comment_count = models.IntegerField(verbose_name='评论数', default=0)
    des = models.TextField(verbose_name='文章简介')
    labels = models.ManyToManyField('ArticleLabel', related_name='labels')


    class Meta:
        db_table = 'article_detail'
        verbose_name = '文章详情'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.title


class ArticleCategory(BaseModel):
    name = models.CharField(verbose_name='分类名', max_length=20, help_text='20字以内')
    parent = models.ForeignKey('self', verbose_name='父级分类', null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        db_table = 'article_category'
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    @classmethod
    def get_categories(cls):
        parent_category = cls.objects.filter(parent__isnull=True)
        categories = []
        for category in parent_category:
            sub_categories = cls.objects.filter(parent=category)
            categories.append({
            'category': category,
            'sub_categories': sub_categories
            })
        return categories

class ArticleComment(BaseModel):
    pass


class ArticleLabel(BaseModel):
    name = models.CharField(verbose_name='文章标签', max_length=20)

    class Meta:
        db_table = 'labels'
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name