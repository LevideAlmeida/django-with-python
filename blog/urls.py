from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('<int:post_id>/', views.post, name='post'),
    path('posts/', views.blog, name='blog'),
]
