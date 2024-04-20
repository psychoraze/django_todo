from django.shortcuts import render
from .models import TODO
import datetime


def index(request):
    return render(request, "index.html", {"todos": TODO.objects.all()})


def detail(request, todo_id):
    return render(request, "detail.html", {"todo": TODO.objects.get(id=todo_id)})


def todo_rating5(request):
    return render(
        request,
        "rating5.html",
        {"todos": TODO.objects.filter(rating=5)},
    )


def todo_below_5(request):
    return render(
        request,
        "todo_below_5.html",
        {"todos": TODO.objects.exclude(rating=5)},
    )
