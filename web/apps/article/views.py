import markdown
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from haystack.views import SearchView

from article.models import ArticleDetail, ArticleCategory, ArticleLabel
from link.models import Link


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
        related_articles = ArticleDetail.objects.filter(category2=article.category2)[0:4]
        context = {
            "article": article,
            'categories': ArticleCategory.get_categories(),
            'related_articles': related_articles,
            'labels_and_count': ArticleLabel.get_labels(),
            'links': Link.objects.all()

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
        context = {
            'articles': articles,
            'category': category,
            'categories': ArticleCategory.get_categories(),
            'sub_categories': ArticleCategory.get_sub_categories(),
        }

        return render(request, 'category_article.html', context=context)


class ArticleStarView(View):

    def post(self, request, article_id):

        article_obj = ArticleDetail.objects.get(id=article_id)
        article_obj.digg_count += 1
        article_obj.save()
        return HttpResponse('success')


class LabelArticleView(View):

    def get(self, request, label_id):
        label_obj = ArticleLabel.objects.get(id=label_id)
        label_articles = label_obj.labels.all()

        context = {
            'label': label_obj,
            'categories': ArticleCategory.get_categories(),
            'label_articles': label_articles
        }
        return render(request, 'label_article.html', context)



class MySearchView(SearchView):

    template = 'search.html'

    def extra_context(self):
        content = super(MySearchView, self).extra_context()
        content['categories'] = ArticleCategory.get_categories()
        return content
