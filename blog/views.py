from django.shortcuts import render
from .models import *


def blog_home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog_home.html', context)