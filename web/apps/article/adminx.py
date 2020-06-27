import xadmin
from article.models import ArticleDetail, ArticleCategory, ArticleLabel


class ArticleXadmin(object):
    list_display = ['id', 'title', 'category1', 'category2']

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'category1':
            kwargs['queryset'] = ArticleCategory.objects.filter(parent__isnull=True)
        if db_field.name == 'category2':
            kwargs['queryset'] = ArticleCategory.objects.filter(parent__isnull=False)
        return super(ArticleXadmin, self).formfield_for_dbfield(db_field, **kwargs)


class ArticleCategoryXadmin(object):
    list_display = ['id', 'name', 'parent']

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'parent':
            kwargs['queryset'] = ArticleCategory.objects.filter(parent__isnull=True)
        return super(ArticleCategoryXadmin, self).formfield_for_dbfield(db_field, **kwargs)


class ArticleLabelXadmin(object):
    list_display = ['id', 'name']


xadmin.site.register(ArticleDetail, ArticleXadmin)
xadmin.site.register(ArticleCategory, ArticleCategoryXadmin)
xadmin.site.register(ArticleLabel, ArticleLabelXadmin)