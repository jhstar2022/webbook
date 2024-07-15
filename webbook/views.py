from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Novel, Chapter, UserNovelPermission
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import NovelForm, ChapterForm


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


@login_required
def novel_list(request):
    novels = Novel.objects.filter(user_permissions__user=request.user, user_permissions__can_read=True)
    return render(request, 'webbook/novel_list.html', {'novels': novels})

@login_required
def novel_detail(request, novel_id):
    novel = get_object_or_404(Novel, id=novel_id)
    permission = get_object_or_404(UserNovelPermission, user=request.user, novel=novel, can_read=True)
    return render(request, 'webbook/novel_detail.html', {'novel': novel})

@login_required
def chapter_detail(request, novel_id, chapter_number):
    novel = get_object_or_404(Novel, id=novel_id)
    permission = get_object_or_404(UserNovelPermission, user=request.user, novel=novel, can_read=True)
    chapter = get_object_or_404(Chapter, novel=novel, number=chapter_number)
    return render(request, 'chapters/chapter_detail.html', {'chapter': chapter})

@login_required
def create_novel(request):
    if request.method == 'POST':
        form = NovelForm(request.POST)
        if form.is_valid():
            novel = form.save(commit=False)
            novel.author = request.user
            novel.save()
            UserNovelPermission.objects.create(user=request.user, novel=novel, can_read=True)
            return redirect('novel_detail', novel_id=novel.id)
    else:
        form = NovelForm()
    return render(request, 'webbook/novel_form.html', {'form': form})

@login_required
def update_novel(request, novel_id):
    novel = get_object_or_404(Novel, id=novel_id, author=request.user)
    if request.method == 'POST':
        form = NovelForm(request.POST, instance=novel)
        if form.is_valid():
            form.save()
            return redirect('novel_detail', novel_id=novel.id)
    else:
        form = NovelForm(instance=novel)
    return render(request, 'webbook/novel_form.html', {'form': form})

@login_required
def delete_novel(request, novel_id):
    novel = get_object_or_404(Novel, id=novel_id, author=request.user)
    if request.method == 'POST':
        novel.delete()
        return redirect('novel_list')
    return render(request, 'webbook/novel_confirm_delete.html', {'novel': novel})

@login_required
def create_chapter(request, novel_id):
    novel = get_object_or_404(Novel, id=novel_id, author=request.user)
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.novel = novel
            chapter.save()
            return redirect('chapter_detail', novel_id=novel.id, chapter_number=chapter.number)
    else:
        form = ChapterForm()
    return render(request, 'chapters/chapter_form.html', {'form': form})

@login_required
def update_chapter(request, novel_id, chapter_number):
    chapter = get_object_or_404(Chapter, novel_id=novel_id, number=chapter_number, novel__author=request.user)
    if request.method == 'POST':
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect('chapter_detail', novel_id=novel_id, chapter_number=chapter.number)
    else:
        form = ChapterForm(instance=chapter)
    return render(request, 'chapters/chapter_form.html', {'form': form})

@login_required
def delete_chapter(request, novel_id, chapter_number):
    chapter = get_object_or_404(Chapter, novel_id=novel_id, number=chapter_number, novel__author=request.user)
    if request.method == 'POST':
        chapter.delete()
        return redirect('novel_detail', novel_id=novel_id)
    return render(request, 'chapters/chapter_confirm_delete.html', {'chapter': chapter})