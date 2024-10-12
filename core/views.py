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

    #arrange the order of the list
    def get_queryset(self):
        model = self.model
        queryset = model.objects.order_by('-created_at')
        return queryset
    
    #display only the task of the login user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        return context

class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'core/view-task.html'
    context_object_name = 'task'

class CreateTaskView(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'core/add-task.html'
    fields = ('title','description')
    success_url = reverse_lazy('index')

    #set the creator of the task base who is login
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTaskView,self).form_valid(form)

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