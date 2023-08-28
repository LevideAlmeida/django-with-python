from django.shortcuts import render

# Create your views here.

context = {
    'text': 'BLOG',
    'title': 'Blog'
}


def blog(request):
    return render(
        request,
        'blog/index.html',
        context
    )
