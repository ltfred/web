import markdown
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from article.models import ArticleDetail, ArticleCategory


class ArticleDetailView(View):

    def get(self, request, article_id):

        try:
            article = ArticleDetail.objects.get(id=article_id)
        except:
            raise
        article.content = markdown.markdown(article.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ])
        categories = ArticleCategory.get_categories()

        context = {
            "article": article,
            'categories': categories
        }

        return render(request, 'article_detail.html', context)
