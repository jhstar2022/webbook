from django.views import View
from django.shortcuts import render
from .models import Post


class Index(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts,
            'title': 'blog'
        }
        return render(request, 'webbook/index.html', context)

class base(View):
    def get(self, request):
        return render(request, 'webbook/base.html')