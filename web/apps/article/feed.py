from django.contrib.syndication.views import Feed
from django.shortcuts import reverse
from .models import ArticleDetail


class BlogFeed(Feed):
    # 标题
    title = 'Fred的个人博客'
    # 描述
    description = '分享自己的一知识'
    # 链接
    link = "/"

    def items(self):
        # 返回所有文章
        return ArticleDetail.objects.all().order_by("-create_time")

    def item_title(self, item):
        # 返回文章标题
        return item.title

    def item_description(self, item):
        # 返回文章描述
        return item.des

    def item_link(self, item):
        # 返回文章详情页的路由
        return reverse('article:detail', args=(item.id,))
