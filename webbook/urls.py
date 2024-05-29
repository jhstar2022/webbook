from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='lise'),
    path('base/', views.base.as_view()),
]
