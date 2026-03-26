from django.contrib import admin
from .models import Dog, Breed
from .form import DogForm

# Register your models here.
admin.site.register(Breed)

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_display', 'breed', 'sex', 'status')
    search_fields = ('name', 'status')
    list_filter = ('sex', 'status', 'breed')
    form = DogForm
    fields = ('name', 'birthday', ('age_year', 'age_month'), 'breed', 'sex', 'status', ('weight', 'weight_unit'), 'description')

    # how to display multiple vars in the one line
    def age_display(self, obj):
        return f'{obj.age_year}y {obj.age_month}m'
