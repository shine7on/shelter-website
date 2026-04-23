from django import forms
from shelter_web.models import Dog, Adoptation
from django.utils.safestring import mark_safe

from datetime import date

class SuffixNumberInput(forms.NumberInput):
    def __init__(self,suffix='',attrs=None):
        self.suffix = suffix
        # make sure e,E,+,- do not work while admin is filling the form
        default_attrs = {'onkeydown': 'return event.key !== "e" && event.key !== "E" && event.key !== "+" && event.key !== "-"'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

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
            # I can do more styling if I add css file
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
            
            if age_year != None and age_month == None:
                age_month = 0
            elif age_year == None and age_month != None:
                age_year = 0
        
            if age_year < 0 or age_month < 0 or age_month > 11:
                raise forms.ValidationError("Invalid input")
        
        cleaned_data["age_year"] = age_year
        cleaned_data["age_month"] = age_month



        # weigth logic: 
        # convert it to kg if admins put lb/g value
        weight = cleaned_data.get('weight')
        unit = cleaned_data.get('weight_unit')

        if unit == 'g':
            weight = weight/1000
        elif unit == 'lb':
            weight = round(0.453592*weight, 2)
        
        cleaned_data["weight"] = weight
        cleaned_data['weight_unit'] = 'kg'

        return cleaned_data


# Shared Tailwind classes
INPUT_CLASS = (
    "w-full bg-stone-50 border-0 rounded-lg px-3 py-2.5 "
    "text-sm text-gray-900 focus:ring-2 focus:ring-emerald-700 outline-none"
)
SELECT_CLASS = (
    "w-full bg-stone-50 border-0 rounded-lg px-3 py-2.5 "
    "text-sm text-gray-900 focus:ring-2 focus:ring-emerald-700 outline-none cursor-pointer"
)
TEXTAREA_CLASS = (
    "w-full bg-stone-50 border-0 rounded-lg px-3 py-2.5 "
    "text-sm text-gray-900 focus:ring-2 focus:ring-emerald-700 outline-none resize-y min-h-[90px]"
)


class AdoptionForm(forms.Form):
    # --- Personal Info ---
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Jane'}),
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Doe'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': INPUT_CLASS, 'placeholder': 'jane@example.com'}),
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': '(555) 000-0000'}),
    )

    # --- Address ---
    STATE_CHOICES = [
        ('', 'Select one...'),
        ('yes_fenced', 'Yes, fenced'),
        ('yes_unfenced', 'Yes, unfenced'),
        ('no', 'No'),
    ]

    street = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': '123 Main St'}),
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Springfield'}),
    )
    state = forms.ChoiceField(
        choices = [('', 'Select a state...')] + [(s, s) for s in Adoptation.StateType],
        widget=forms.Select(attrs={'class': SELECT_CLASS}),
    )
    zip_code = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': '62701'}),
    )

    # --- Living Situation ---
    HOUSING_CHOICES = [
        ('', 'Select one...'),
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('townhouse', 'Townhouse'),
        ('other', 'Other'),
    ]
    housing_type = forms.ChoiceField(
        choices=HOUSING_CHOICES,
        widget=forms.Select(attrs={'class': SELECT_CLASS}),
    )

    YARD_CHOICES = [
        ('', 'Select one...'),
        ('yes_fenced', 'Yes, fenced'),
        ('yes_unfenced', 'Yes, unfenced'),
        ('no', 'No'),
    ]
    has_yard = forms.ChoiceField(
        choices=YARD_CHOICES,
        widget=forms.Select(attrs={'class': SELECT_CLASS}),
    )
    

    # --- Dog Selection ---
    dog = forms.ModelChoiceField(
        queryset=Dog.objects.filter(status='Not-Adopted'), 
        empty_label='Select a dog...',
        widget=forms.Select(attrs={'class': SELECT_CLASS}),
    )

    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': TEXTAREA_CLASS,
            'placeholder': 'Tell us a bit about your lifestyle, experience with dogs, etc.',
        }),
    )

    # --- Validation ---
    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        digits = ''.join(filter(str.isdigit, phone))
        if len(digits) < 10:
            raise forms.ValidationError("Please enter a valid phone number.")
        return phone

    def clean_zip_code(self):
        zip_code = self.cleaned_data.get('zip_code', '')
        if not zip_code.isdigit() or len(zip_code) not in (5, 9):
            raise forms.ValidationError("Enter a valid ZIP code (5 or 9 digits).")
        return zip_code