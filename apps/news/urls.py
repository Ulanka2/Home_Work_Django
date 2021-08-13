from django.urls import path
from .views import MainPageView, NewsDetailView

urlpatterns = [
    path('news/', MainPageView.as_view(), name='news_list'),
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail_url'),
]