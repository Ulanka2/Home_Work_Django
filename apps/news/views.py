from apps.questions.models import Question
from django.shortcuts import render
from django.views.generic import View, DetailView #next time try to do it with ListView
from .models import Post
from  apps.employees.models import Employee


class MainPageView(View):

    def get(self, request):
        posts = Post.objects.filter(is_active=True)
        employee = Employee.objects.all()
        question = Question.objects.all()

        return render(request, 'main_page.html', context={'posts': posts, 'employee': employee, 'question': question})

class NewsDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'news_detail.html'

