from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Todo


def index(request):
    return HttpResponse('Hello,welcome to the index page.')
def todo_list(request):
    recent_post = Todo.objects.get(id_exact=1)
    return HttpResponse(recent_post.title+':'+recent_post.description)
