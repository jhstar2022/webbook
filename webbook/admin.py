from django.contrib import admin
from .models import Post

from .models import User, Genre, Novel, Chapter, Comment, ReadingHistory, NovelLike, ChapterLike, UserNovelPermission


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'created_at')
    list_filter = ('genre', 'created_at')
    search_fields = ('title', 'author__username')

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'novel', 'number', 'created_at')
    list_filter = ('novel', 'created_at')
    search_fields = ('title', 'novel__title')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'chapter', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'chapter__title')

@admin.register(ReadingHistory)
class ReadingHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'chapter', 'last_read_at')
    list_filter = ('last_read_at',)
    search_fields = ('user__username', 'chapter__title')

@admin.register(NovelLike)
class NovelLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'novel', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'novel__title')

@admin.register(ChapterLike)
class ChapterLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'chapter', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'chapter__title')

@admin.register(UserNovelPermission)
class UserNovelPermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'novel', 'can_read')
    list_filter = ('can_read',)
    search_fields = ('user__username', 'novel__title')

admin.site.register(Post)
