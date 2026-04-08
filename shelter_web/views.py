from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Dog, Breed


# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World')


def all_dogs_views(request):
    dogs = Dog.objects.all()
    breeds = Breed.objects.all()
    return render(request, 'shelter_web/template_demo.html', {'dogs': dogs, 'breeds': breeds})

def dog_list_api(request):
    dogs = Dog.objects.all()
    listDogs = dogs.values('id','name','status','sex') 
    return JsonResponse(list(listDogs), safe=False)