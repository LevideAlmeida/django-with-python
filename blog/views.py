from django.shortcuts import render
from . import data

# Create your views here.


def blog(request):

    context = {
        'text': 'BLOG',
        'title': 'Blog',
        'posts': data.posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def post(request, id):
    context = {
        'text': 'BLOG',
        'title': 'Blog',
        'posts': data.posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )
