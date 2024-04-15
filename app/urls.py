from django.urls import path
from .views import *


urlpatterns = [
    path('', index , name='index'),
    path('detail/<int:todo_id>', detail, name='detail'),
    path('todo_created_today', todo_created_today, name='todo_created_today'),
    path('todo_was_created_not_today', todo_was_created_not_today, name='todo_was_created_not_today'),
]