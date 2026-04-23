from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Dog, Breed, Adoptation
from .form import AdoptionForm


# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World')


def all_dogs_views(request):
    dogs = Dog.objects.all()
    breeds = Breed.objects.all()
    return render(request, 'shelter_web/all_dogs.html', {'dogs': dogs, 'breeds': breeds})

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


# adoptation form page
def adopt_form(request):
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            Adoptation.objects.create(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                phone = form.cleaned_data['phone'],
                street = form.cleaned_data['street'],
                city = form.cleaned_data['city'],
                state = form.cleaned_data['state'],
                zip = form.cleaned_data['zip_code'],
                housing = form.cleaned_data['housing_type'],
                yard = form.cleaned_data['has_yard'],
                interested_dog = form.cleaned_data['dog'].name,
                comment = form.cleaned_data['notes'],
            )
            return redirect('success')
    else:
        form = AdoptionForm()
        
    return render(request, 'shelter_web/form.html', {'form': form})


def submission_success(request):
    return render(request, 'shelter_web/submission_success.html')