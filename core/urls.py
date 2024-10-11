from django.urls import path
from .views import TaskListView,TaskDetailView,CreateTaskView,UpdateTaskView,DeleteTaskView
urlpatterns = [
    path('',TaskListView.as_view(),name='index'),
    path('task/<int:pk>/',TaskDetailView.as_view(),name='view-task'),
    path('create/',CreateTaskView.as_view(),name='add-task'),
    path('update/task/<int:pk>',UpdateTaskView.as_view(),name='update-task'),
    path('delete/task/<int:pk>',DeleteTaskView.as_view(),name='delete-task'),
]