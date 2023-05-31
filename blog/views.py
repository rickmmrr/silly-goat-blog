# blog/views.py
from django.views.generic import ListView, DetailView, TemplateView
from django.template.response import TemplateResponse
from django.template import loader
from .models import Post
from django.shortcuts import render
from django.http import HttpResponse


def return_posts_by_tag(request, cat):
    posts = Post.objects.filter(categories__title=cat)

    # template = loader.get_template("tag.html")

    context = {"posts": posts, "the_tag": cat}

    # check = template.render(context, request)

    return render(request, "tag.html", context)


class BlogListView(ListView):
    model = Post
    #    context_object_name = "posts"
    template_name = "index.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
