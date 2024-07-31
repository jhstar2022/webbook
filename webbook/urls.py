from django.urls import path
from . import views


app_name='webbook'

urlpatterns = [
    path('', views.Index.as_view(), name='list'),
    # 글 상세 조회
    path("detail/<int:pk>/ ", views.DetailView.as_view(), name='detail'),
    # 글 작성
    path("write/", views.Write.as_view(), name='write'),
    # 글 수정
    path("detail/<int:pk>/edit/", views.Update.as_view(), name='edit'),
    # 글 삭제
    path("detail/<int:pk>/delete/", views.Delete.as_view(), name='delete'),
    # 책 리스트
    path('novel_list', views.novel_list, name='novel_list'),
    # 책 상세
    path('novel/<int:novel_id>/', views.novel_detail, name='novel_detail'),
    # 챕터 상세
    path('novel/<int:novel_id>/chapter/<int:chapter_number>/', views.chapter_detail, name='chapter_detail'),
    # 책 작성
    path('create_novel/', views.create_novel, name='create_novel'),
    # 책 수정
    path('update_novel/<int:novel_id>/', views.update_novel, name='update_novel'),
    # 책 삭제
    path('delete_novel/<int:novel_id>/', views.delete_novel, name='delete_novel'),
    # 챕터 생성
    path('novel/<int:novel_id>/create_chapter/', views.create_chapter, name='create_chapter'),
    path('novel/<int:novel_id>/update_chapter/<int:chapter_number>/', views.update_chapter, name='update_chapter'),
    path('novel/<int:novel_id>/delete_chapter/<int:chapter_number>/', views.delete_chapter, name='delete_chapter'),
]
