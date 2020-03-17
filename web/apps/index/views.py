from django.shortcuts import render
from django.views import View
from article.models import ArticleDetail, ArticleCategory
from index.models import Carousel


class IndexView(View):

    def get(self, request):

        new_articles = ArticleDetail.objects.all()[0:8]
        carousel_article = Carousel.objects.filter(is_active=True)
        categories = ArticleCategory.get_categories()
        tech_articles = ArticleDetail.objects.filter(category1_id=5).order_by('-view_count')[0:5]
        life_articles = ArticleDetail.objects.filter(category1_id=2).order_by('-view_count')[0:5]
        tech_new_articles = ArticleDetail.objects.filter(category1_id=5).order_by('-create_time')[0:8]
        data = {
            'new_articles': new_articles,
            'carousel_article': carousel_article,
            'categories': categories,
            'tech_articles': tech_articles,
            'life_articles': life_articles,
            'tech_new_articles': tech_new_articles

        }
        return render(request, 'index.html', context=data)