from django.urls import path
from .views import ArticleDetailView, ArticleCategoryView, ArticleStarView

app_name = 'article'

urlpatterns = [
    path("detail/<int:article_id>/", ArticleDetailView.as_view(), name='detail'),
    path("category/<int:category_id>/", ArticleCategoryView.as_view(), name='category_article'),
    path("star/<int:article_id>/", ArticleStarView.as_view(), name='article_star'),

]
