#blog/urls.py
from django.urls import path
from . import views
from .views import BlogListView , BlogDetailView, AboutPageView


urlpatterns =  [
    path("tag/<str:cat>/", views.return_posts_by_tag, name="tag_view"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post"),
    path('', BlogListView.as_view(), name='index'),
    path('about', AboutPageView.as_view(), name='about'),
    
    ]