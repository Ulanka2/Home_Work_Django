from django.urls import path
from django.urls import path
from apps.employees.views import  EmploDetailView


urlpatterns = [
    path('<int:pk>', EmploDetailView.as_view(), name='employee_detail_url'),

]