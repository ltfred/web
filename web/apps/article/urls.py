from django.urls import path
from .views import ArticleDetailView

urlpatterns = [
    path("detail/<int:article_id>/", ArticleDetailView.as_view(), name='detail')
]
