from django.urls import path
from . import veiws

urlpatterns = [
    path('', veiws.index),
    path('web/', veiws.Index.as_view())

]