from django.contrib import admin
from .models import Dog, Breed
from .form import DogForm

# Register your models here.
admin.site.register(Breed)

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_year', 'breed', 'sex', 'status')
    search_fields = ('name', 'status')
    # list_filter = ('breed')
    form = DogForm
    fields = ('name', 'birthday', ('age_year', 'age_month'), 'breed', 'sex', 'status', ('weight', 'weight_unit'), 'description')