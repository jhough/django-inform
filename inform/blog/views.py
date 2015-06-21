from __future__ import absolute_import
from django.views.generic import ListView, DetailView

from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

