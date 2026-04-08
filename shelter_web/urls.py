from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello_world, name='hello_world'),
    path('dog', views.all_dogs_views, name='dogs'),
    path('dogapi', views.dog_list_api, name='dogs_api'),
    path('dog/<int:dog_id>/', views.dog_detail, name='dog_detail')
]