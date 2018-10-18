from django.shortcuts import render
from blog_app.models import BlogPost, Comment
from blog_app.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView, CreateView)

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__lte=timezone.now().order_by('-published_date')))

class PostDetailView(DetialView):
    model = BlogPost

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    form_class = Postform
    model = BlogPost
