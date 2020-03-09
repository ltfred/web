from django.shortcuts import render
from django.views import View
from article.models import ArticleDetail, ArticleCategory
from index.models import Carousel


class IndexView(View):

    def get(self, request):

        new_articles = ArticleDetail.objects.all()[0:8]
        carousel_article = Carousel.objects.filter(is_active=True)
        parent_category = ArticleCategory.objects.filter(parent__isnull=True)
        categories = []
        for category in parent_category:
            sub_categories = ArticleCategory.objects.filter(parent=category)
            categories.append({
                'category': category,
                'sub_categories': sub_categories
            })
        data = {
            'new_articles': new_articles,
            'carousel_article': carousel_article,
            'categories': categories
        }
        return render(request, 'index.html', context=data)