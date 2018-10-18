from django.shortcuts import render
from blog_app.models import BlogPost, Comment
from django.views.generic import (TemplateView, ListView)

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__lte=timezone.now().order_by('-published_date')))

    
