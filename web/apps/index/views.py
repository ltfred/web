from django.shortcuts import render
from django.views import View
from article.models import ArticleDetail, ArticleCategory
from index.models import Carousel


class IndexView(View):

    def get(self, request):

        new_articles = ArticleDetail.objects.all()[0:8]
        carousel_article = Carousel.objects.filter(is_active=True)
        categories = ArticleCategory.get_categories()
        data = {
            'new_articles': new_articles,
            'carousel_article': carousel_article,
            'categories': categories
        }
        return render(request, 'index.html', context=data)