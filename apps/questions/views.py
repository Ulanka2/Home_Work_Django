from django.shortcuts import render, redirect
from django.views.generic import View, DetailView 
from  .models import Question
from .forms import QuestionForm

class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'question_detail.html'

# def question(request):
#     if request.method == "POST":
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.save()
#             return redirect('news_detail', pk=question.pk)
#     else:
#         form = QuestionForm()
#     return render(request, 'question_edit.html', {'form': form})
