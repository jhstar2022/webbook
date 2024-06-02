from django.urls import path
from . import views


app_name='webbook'

urlpatterns = [
    path('', views.Index.as_view(), name='list'),
    path('index/', views.Index2.as_view(), name='list2'),
    path('write/', views.write, name='write'),
]
