from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView
)

from . import views

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:id>', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create')
]

