from django import forms
from .models import Post, Novel, Chapter


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']


class NovelForm(forms.ModelForm):
    class Meta:
        model = Novel
        fields = ['title', 'genre', 'description']


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['number', 'title', 'content']