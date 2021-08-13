from django.db import models
from django.urls import reverse

class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.TextField()
    img = models.ImageField(upload_to='post_image', null=True, blank=True)
    is_active = models.BooleanField(default=False)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employee_detail_url', kwargs={'pk': self.pk})