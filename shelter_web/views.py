from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog


# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World')


def all_dogs_views(request):
    dogs = Dog.objects.all()
    return render(request, 'shelter_web/template_demo.html', {'dogs': dogs})