# blog/views.py
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post



class BlogListView(ListView):
    model = Post
    template_name = "index.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

