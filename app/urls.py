from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("detail/<int:todo_id>", detail, name="detail"),
    path("todo_below_5", todo_below_5, name="todo_below_5"),
    path("rating5", todo_rating5, name="rating5"),
]
