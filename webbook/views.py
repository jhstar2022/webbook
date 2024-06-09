from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin



class Index(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, 'webbook/index.html', context)



class Write(LoginRequiredMixin, View):
    
    def get(self, request):
        form = PostForm()
        context = {
            'form': form,
            "title": "Blog"
        }
        return render(request, 'webbook/post_form.html', context)
    
    def post(self, request):
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('webbook:list')
        
        context = {
            'form': form
        }
        
        return render(request, 'webbook/post_form.html', context)


class Update(View):
    
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(initial={'title': post.title, 'content': post.content})
        context = {
            'form': form,
            'post': post,
            "title": "webbook"
        }
        return render(request, 'webbook/post_edit.html', context)
    
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST)
        
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('webbook:detail', pk=pk)
        
        context = {
            'form': form,
            "title": "webook"
        }
        
        return render(request, 'webbook/post_edit.html', context)
        

class Delete(View):
    
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('webbook:list')


class DetailView(View):
    
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        context = {
            "title": "webbook",
            'post_id': pk,
            'post_title': post.title,
            'post_writer': post.writer,
            'post_content': post.content,
            'post_created_at': post.created_at,
        }
        
        return render(request, 'webbook/post_detail.html', context)