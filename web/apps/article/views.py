from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from article.models import ArticleDetail


class ArticleDetailView(View):

    def get(self, request, article_id):

        try:
            article = ArticleDetail.objects.get(id=article_id)
        except:
            raise

        context = {"article": article}

        return render(request, 'article_detail.html', context)