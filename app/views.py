from django.shortcuts import render
from .models import TODO
import datetime
def index(request):
    return render(request, 'index.html',{"todos":TODO.objects.all()})

def detail(request, todo_id):
    return render(request, 'detail.html',{"todo":TODO.objects.get(id=todo_id)})


def level_gt_2(request):
    return render(request, 'level_gt_2.html',{"todos":TODO.objects.filter(importants_level__gt=2)})

def level_lt_2(request):
    return render(request, 'level_lt_2.html',{"todos":TODO.objects.filter(importants_level__lt=2)})

def todo_created_today(request):
    return render(request, 'todo_created_today.html',{"todos":TODO.objects.filter(created__date=datetime.date.today())})

def todo_was_created_not_today(request):
    return render(request, 'todo_was_created_not_today.html',{"todos":TODO.objects.exclude(created__date=datetime.date.today())})