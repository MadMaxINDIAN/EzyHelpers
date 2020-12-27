from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('blog/<str:blog_title>', views.blog),
    path('create_blog', views.create_blog)
]
