from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


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



def write(request):
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('webbook:list')
    else:
        form = PostForm()
        
    return render(request, 'webbook/write.html',{'form': form})

