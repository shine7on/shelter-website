from django.contrib import admin
from .models import Dog, Breed

# Register your models here.
admin.site.register(Breed)

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_year', 'breed', 'sex', 'status')
    search_fields = ('name', 'breed', 'status')
    # list_filter = ('breed')
    fields = ('name', 'birthday', ('age_year', 'age_month'), 'breed', 'sex', 'status', ('weight', 'weight_unit'), 'description')