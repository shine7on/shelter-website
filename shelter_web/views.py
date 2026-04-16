from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Dog, Breed


# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World')


def all_dogs_views(request):
    dogs = Dog.objects.all()
    breeds = Breed.objects.all()
    return render(request, 'shelter_web/template_demo.html', {'dogs': dogs, 'breeds': breeds})

# Filter data 
def dog_list_api(request):
    dogs = Dog.objects.all()

    # age year
    age_year = request.GET.get('age_year', '')
    if age_year:
        dogs = dogs.filter(age_year=age_year)
    
    # age month
    age_month = request.GET.get('age_month', '')
    if age_month:
        dogs = dogs.filter(age_month=age_month)
    
    # weight
    weight = request.GET.get('weight', '')
    if weight:
        dogs = dogs.filter(weight)


    sex = request.GET.get('sex', '')
    if sex:
        dogs = dogs.filter(sex=sex)

    # now try adding status and breed yourself..
    status = request.GET.get('status', '')
    if status:
        dogs = dogs.filter(status=status)
    
    breed = request.GET.get('breed', '')
    if breed:
        dogs = dogs.filter(breed__id=breed)

    listDogs = dogs.values('id','name', 'breed__breed', 'age_year','age_month','weight','status','sex', 'photo') 
    return JsonResponse(list(listDogs), safe=False)


# Display a detail page of dog
def dog_detail(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)
    breeds = Breed.objects.all()

    return render(request, 'shelter_web/dog_detail.html', {'dog':dog})


# Home page
'''
def dog_detail(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)
    breeds = Breed.objects.all()
    return render(request, 'shelter_web/dog_detail.html', {'dog':dog})


# adoptation form page
'''