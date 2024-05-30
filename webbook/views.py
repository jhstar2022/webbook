from django.views import View
from django.shortcuts import render
from .models import Post


class Index(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, 'webbook/index.html', context)


class Index2(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, 'webbook/index2.html', context)


class base(View):
    def get(self, request):
        return render(request, 'webbook/base.html')