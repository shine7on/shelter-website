from django.contrib import admin
from .models import Dog, Breed, Adoptation
from .form import DogForm

# Register your models here.
admin.site.register(Breed)
admin.site.register(Adoptation)

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    # how to display multiple vars in the one line
    def age_display(self, obj):
        return f'{obj.age_year}y {obj.age_month}m'
    
    def weight_display(self, obj):
        return f'{obj.weight} kg'
    
    # change the name of variable to display
    age_display.short_description = 'age'
    weight_display.short_description = 'weight[kg]'

    list_display = ('name', 'age_display', 'breed', 'weight', 'sex', 'status')
    search_fields = ('name', 'status')
    list_filter = ('sex', 'status', 'breed')
    form = DogForm
    fields = ('name', 'birthday', ('age_year', 'age_month'), 'breed', 'sex', 'status', ('weight', 'weight_unit'), 'description', 'photo')

    
