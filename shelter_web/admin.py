from django.contrib import admin
from .models import Dog

# Register your models here.
# admin.site.register(Dog)

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed', 'sex', 'status')
    search_fields = ('name', 'breed')
    # list_filter = ('status')