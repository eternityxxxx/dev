from django.urls import path

from .views import index

app_name = 'pipeline'

urlpatterns = [
    path('index/', index, name='index'),
]
