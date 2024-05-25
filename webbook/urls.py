from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view()),
    path('base/', views.base.as_view()),
]
