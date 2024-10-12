from .models import Task
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'core/index.html'
    context_object_name = 'tasks'

class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'core/view-task.html'
    context_object_name = 'task'

class CreateTaskView(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'core/add-task.html'
    fields = ('user','title','description')
    success_url = reverse_lazy('index')

class UpdateTaskView(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'core/update-task.html'
    fields = ('title','description','is_done')
    success_url = reverse_lazy('index')
    context_object_name = 'task'

class DeleteTaskView(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('index')
    template_name = 'core/delete-task.html'