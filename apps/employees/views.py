from django.shortcuts import render
from django.views.generic import View, DetailView 
from  apps.employees.models import Employee

class EmploDetailView(DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'employee_detail.html'
