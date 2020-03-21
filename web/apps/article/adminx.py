import xadmin
from article.models import ArticleDetail, ArticleCategory, ArticleLabel


class ArticleXadmin(object):
    list_display = ['title', 'category1', 'category2']
    style_fields = {'labels': 'checkbox-inline', }


class ArticleCategoryXadmin(object):
    list_display = ['name', 'parent']


class ArticleLabelXadmin(object):
    pass

xadmin.site.register(ArticleDetail, ArticleXadmin)
xadmin.site.register(ArticleCategory, ArticleCategoryXadmin)
xadmin.site.register(ArticleLabel, ArticleLabelXadmin)