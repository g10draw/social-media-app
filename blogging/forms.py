from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_text', 'image')
        widgets = {
            'post_text': forms.Textarea(attrs={'rows': 3})
        }