from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='lise'),
    path('index/', views.Index2.as_view(), name='lise2'),
    path('base/', views.base.as_view()),
]
