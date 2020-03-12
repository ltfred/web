from django.urls import path
from .views import ArticleDetailView, ArticleCategoryView

urlpatterns = [
    path("detail/<int:article_id>/", ArticleDetailView.as_view(), name='detail'),
    path("category/<int:category_id>/", ArticleCategoryView.as_view(), name='category_article')
]
