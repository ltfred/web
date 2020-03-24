from datetime import timedelta
from django.shortcuts import render
from django.utils import timezone
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
        shi_count =ArticleDetail.objects.filter(category1_id=1).count()
        tech_count =ArticleDetail.objects.filter(category1_id=2).count()
        tool_count =ArticleDetail.objects.filter(category1_id=3).count()
        ci_count =ArticleDetail.objects.filter(category1_id=6).count()
        data = {
            'new_articles': new_articles,
            'carousel_article': carousel_article,
            'categories': categories,
            'tech_articles': tech_articles,
            'life_articles': life_articles,
            'tech_new_articles': tech_new_articles,
            'shi_count': shi_count,
            'tech_count': tech_count,
            'tool_count': tool_count,
            'ci_count': ci_count,


        }
        return render(request, 'index.html', context=data)