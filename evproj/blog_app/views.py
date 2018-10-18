from django.shortcuts import render
from blog_app.models import BlogPost, Comment
from blog_app.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetialView):
    model = BlogPost

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    form_class = Postform
    model = BlogPost

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    form_class = Postform
    model = BlogPost

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_list.html'
    model = BlogPost

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
