from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.Form):
    title = forms.CharField(max_length=36)
    slug = forms.CharField(max_length=36)
    text = forms.CharField(max_length=36)  

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        
        if new_slug == 'create':
            raise ValidationError('Слаг не может быть create')
        return new_slug


    def save(self):
        new_post = Post.objects.create(title = self.cleaned_data['title'],
        slug = self.cleaned_data['slug'],
        text = self.cleaned_data['text'],)
        return new_post