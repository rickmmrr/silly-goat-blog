#blog/urls.py
from django.urls import path
from .views import BlogListView , BlogDetailView, AboutPageView

urlpatterns =  [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post"),
    path('', BlogListView.as_view(), name='index'),
    path('about', AboutPageView.as_view(), name='about'),
    ]