# blog/views.py
from django.views.generic import ListView, DetailView, TemplateView
from django.template.response import TemplateResponse
from .models import Post


def return_posts_by_tag(request, arg):
    print(arg)
    context = {
        'posts': list(Post.objects.filter(categories=arg))
        }
    return TemplateResponse(request, "tag.html", context)




class BlogListView(ListView):
    model = Post
#    context_object_name = "posts"
    template_name = "index.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

