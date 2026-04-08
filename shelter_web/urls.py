from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('hello', views.hello_world, name='hello_world'),
    path('dog', views.all_dogs_views, name='dogs'),
    path('dogapi', views.dog_list_api, name='dogs_api'),
    path('dog/<int:dog_id>/', views.dog_detail, name='dog_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)