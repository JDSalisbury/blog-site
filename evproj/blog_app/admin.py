from django.contrib import admin
from blog_app.models import BlogPost, Comment
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Comment)
