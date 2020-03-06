from django.shortcuts import render
from django.views import View
from article.models import ArticleDetail


class IndexView(View):

    def get(self, request):

        new_articles = ArticleDetail.objects.all()[0:8]
        data = {
            'new_articles': new_articles,
        }
        return render(request, 'index.html', context=data)