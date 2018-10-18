from django import forms
from blog_app.models import BlogPost, Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = BlogPost
        fields = ('author', 'title', 'text')


# css classes add to widgets
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(form.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }
