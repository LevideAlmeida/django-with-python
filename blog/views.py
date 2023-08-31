from django.shortcuts import render
from . import data
from typing import Optional, Any
from django.http import Http404

# Create your views here.

posts = data.posts


def blog(request):

    context = {
        'title': 'Blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def post(request, post_id):
    found_post: Optional[dict[str, Any]] = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404()

    context = {
        'post': found_post,
        'title': found_post['title']
    }

    return render(
        request,
        'blog/post.html',
        context
    )
