import markdown
from django.db.models import Q
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

        article = ArticleDetail.objects.filter(Q(category1_id=category_id) | Q(category2_id=category_id))

        context = {
            'articles': article
        }

        return render(request, 'category_article.html', context=context)