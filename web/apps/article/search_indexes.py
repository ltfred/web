from haystack import indexes

from .models import ArticleDetail


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    """Article索引数据模型类"""
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return ArticleDetail

    def index_queryset(self, using=None):
        return self.get_model().objects.all()