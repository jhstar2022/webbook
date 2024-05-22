from django.urls import path
from . import veiws

urlpatterns = [
    path('', veiws.index.as_view(), name='index'),
]
