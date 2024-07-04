from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Genre(models.Model):
    name = models.CharField(max_length=100)

class Novel(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='novels')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Chapter(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name='chapters')
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ReadingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_history')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='reading_history')
    last_read_at = models.DateTimeField(auto_now=True)

class NovelLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='novel_likes')
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name='novel_likes')
    created_at = models.DateTimeField(auto_now_add=True)

class ChapterLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chapter_likes')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='chapter_likes')
    created_at = models.DateTimeField(auto_now_add=True)

class UserNovelPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='novel_permissions')
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name='user_permissions')
    can_read = models.BooleanField(default=False)