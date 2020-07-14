import markdown
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from haystack.views import SearchView
from article.models import ArticleDetail, ArticleCategory, ArticleLabel
from link.models import Link
from web.utils.common import paginator_func


class ArticleDetailView(View):

    def get(self, request, article_id):

        try:
            article = ArticleDetail.get_article_obj(id=article_id)
            article.view_count += 1
            article.save()
        except:
            raise
        article.content = markdown.markdown(article.content.replace("\r\n", '  \n'), extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ])
        related_articles = ArticleDetail.objects.filter(category2=article.category2).exclude(id=article.id).order_by("-digg_count")[0:4]
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
        page_num = request.GET.get('page', 1)
        q = request.GET.get('q', '')
        articles = ArticleDetail.objects.filter(Q(category1_id=category_id) | Q(category2_id=category_id))
        if q:
            if q == 'time':
                articles = articles.order_by('-create_time')
            elif q == 'hot':
                articles = articles.order_by('-view_count')
        page_list, total_page = paginator_func(articles, page_num)
        category = ArticleCategory.objects.get(id=category_id)
        context = {
            'articles': page_list,
            'category': category,
            'categories': ArticleCategory.get_categories(),
            'sub_categories': ArticleCategory.get_sub_categories(),
            'total_page': total_page
        }
        return render(request, 'category_article.html', context=context)


class ArticleStarView(View):

    def post(self, request, article_id):
        article_obj = ArticleDetail.get_article_obj(id=article_id)
        article_obj.digg_count += 1
        article_obj.save()
        return HttpResponse('success')


class LabelArticleView(View):

    def get(self, request, label_id):
        page_num = request.GET.get('page')
        page_num = page_num if page_num else 1
        label_obj = ArticleLabel.objects.get(id=label_id)
        label_articles = label_obj.labels.all()
        page_list, total_page = paginator_func(label_articles, page_num)
        context = {
            'label': label_obj,
            'categories': ArticleCategory.get_categories(),
            'label_articles': page_list,
            'total_page': total_page,
            'labels_and_count': ArticleLabel.get_labels()
        }
        return render(request, 'label_article.html', context)


class MySearchView(SearchView):

    template = 'search.html'

    def extra_context(self):
        content = super(MySearchView, self).extra_context()
        content['categories'] = ArticleCategory.get_categories()
        content['search_count'] = self.results.count()
        return content


class TimeLineView(View):

    def get(self, request):

        page = request.GET.get('page', 1)
        articles = ArticleDetail.objects.all().values('title', 'create_time', 'id')
        page_list, total_page = paginator_func(articles, page)
        context = {
            'articles': page_list,
            'count': articles.count(),
            'categories': ArticleCategory.get_categories()
        }
        return render(request, 'time_line.html', context=context)