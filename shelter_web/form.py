from django import forms
from shelter_web.models import Dog
from django.utils.safestring import mark_safe

from datetime import date

class SuffixNumberInput(forms.NumberInput):
    def __init__(self,suffix='',attrs=None):
        self.suffix = suffix
        super().__init__(attrs)

    def render(self,name,value,attrs=None,renderer=None):
        input_html = super().render(name, value, attrs, renderer)
        return mark_safe(
            f'''
            <div style="display:inline-flex; align-items:center;">
                {input_html}
                <span style="margin-left:6px; font-size:12px; color:#666;">
                    {self.suffix}
                </span>
            </div>
            '''
        )


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 
                  'birthday', 
                  'age_year', 
                  'age_month', 
                  'breed', 
                  'sex', 
                  'status', 
                  'weight', 
                  'weight_unit', 
                  'description']
        labels = {
            "age_year": "Age",
            "age_month": '',
            'weight_unit': '',
        }
        help_texts = {
            "age_year": "Used only when exact birthday is unknown. Example: 6 years 10 months",
        }
        widgets = {
            'age_year': SuffixNumberInput(suffix="year(s)", attrs={'style': 'width: 80px'}),
            "age_month": SuffixNumberInput(suffix="month(s)", attrs={'style': 'width: 80px'}),
            'weight': forms.NumberInput(attrs={'style': 'width: 100px'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()

        # birthday logic: 
        # calculate the duration based on the birthday
        # or manually put year, month by admins
        birthday = cleaned_data.get("birthday")
        age_year = cleaned_data.get("age_year")
        age_month = cleaned_data.get("age_month")

        today = date.today()
        
        if birthday:
            if birthday > today:
                raise forms.ValidationError("Birthday cannot be in the future.")
            
            age_year = today.year - birthday.year
            age_month = today.month - birthday.month

            if today.day < birthday.day:
                age_month -= 1
            
            if age_month < 0:
                age_year -= 1
                age_month = 12 + age_month
        else:
            if age_year == None and age_month == None:
                raise forms.ValidationError("Add age (year/month)")
            elif age_year < 0 or age_month < 0 or age_month > 11:
                raise forms.ValidationError("Invalid input")
            elif age_year != None and age_month == None:
                age_month = 0
            elif age_year == None and age_month != None:
                age_year = 0
        
        cleaned_data["age_year"] = age_year
        cleaned_data["age_month"] = age_month



        # weigth logic: 
        # convert it to kg if admins put lb/g value
        weight = cleaned_data.get('weight')
        unit = cleaned_data.get('weight_unit')

        if unit == 'g':
            weight = weight/1000
        elif unit == 'lb':
            weight = round(0.453592*weight)
        
        cleaned_data["weight"] = weight
        cleaned_data['weight_unit'] = 'kg'

        return cleaned_data
