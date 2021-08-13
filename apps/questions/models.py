from django.db import models
from django.urls import reverse

class Question(models.Model):
    contact = models.CharField(max_length=255)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact

    def get_absolute_url(self):
        return reverse('question_detail_url', kwargs={'pk': self.pk})
