from django.urls import path
from .views import  QuestionDetailView, question

urlpatterns = [
    path('<int:pk>', QuestionDetailView.as_view(), name='question_detail_url'),
    
]