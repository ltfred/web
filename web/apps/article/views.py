import markdown
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from article.models import ArticleDetail, ArticleCategory, ArticleLabel


class ArticleDetailView(View):

    def get(self, request, article_id):

        try:
            article = ArticleDetail.objects.get(id=article_id)
        except:
            raise
        article.content = markdown.markdown(article.content.replace("\r\n", '  \n'), extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ])
        categories = ArticleCategory.get_categories()
        related_articles = ArticleDetail.objects.filter(category2=article.category2)[0:4]
        labels_and_count = ArticleLabel.get_labels()
        context = {
            "article": article,
            'categories': categories,
            'related_articles': related_articles,
            'labels_and_count': labels_and_count

        }

        return render(request, 'article_detail.html', context)


class ArticleCategoryView(View):

    def get(self, request, category_id):
        q = request.GET.get('q')
        articles = ArticleDetail.objects.filter(Q(category1_id=category_id) | Q(category2_id=category_id))
        if q:
            if q == 'time':
                articles = articles.order_by('-create_time')
            elif q == 'hot':
                articles = articles.order_by('-digg_count')
        category = ArticleCategory.objects.get(id=category_id)
        categories = ArticleCategory.get_categories()
        sub_categories = ArticleCategory.get_sub_categories()

        context = {
            'articles': articles,
            'category': category,
            'categories': categories,
            'sub_categories': sub_categories,
        }

        return render(request, 'category_article.html', context=context)


class ArticleStarView(View):

    def post(self, request, article_id):

        article_obj = ArticleDetail.objects.get(id=article_id)
        article_obj.digg_count += 1
        article_obj.save()
        return HttpResponse('success')
