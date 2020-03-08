from django.shortcuts import render
from django.views import View
from article.models import ArticleDetail
from index.models import Carousel


class IndexView(View):

    def get(self, request):

        new_articles = ArticleDetail.objects.all()[0:8]
        carousel_article = Carousel.objects.filter(is_active=True)
        data = {
            'new_articles': new_articles,
            'carousel_article': carousel_article
        }
        return render(request, 'index.html', context=data)