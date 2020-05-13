from django.shortcuts import render
from django.views.generic import TemplateView
from article.models import ArticleDetail, ArticleCategory
from index.models import Carousel



class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content["new_articles"] = ArticleDetail.objects.all()[0:12]
        content["carousel_article"] = Carousel.objects.filter(is_active=True)
        content["categories"] = ArticleCategory.get_categories()
        content["tech_articles"] = ArticleDetail.objects.filter(category1_id=5).order_by('-view_count')[0:5]
        content["life_articles"] = ArticleDetail.objects.filter(category1_id=2).order_by('-view_count')[0:5]
        content["tech_new_articles"] = ArticleDetail.objects.filter(category1_id=5).order_by('-create_time')[0:8]
        content["shi_count"] = ArticleDetail.objects.filter(category1_id=1).count()
        content["tech_count"] = ArticleDetail.objects.filter(category1_id=2).count()
        content["tool_count"] = ArticleDetail.objects.filter(category1_id=3).count()
        content["ci_count"] = ArticleDetail.objects.filter(category1_id=6).count()
        return content