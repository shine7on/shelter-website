from django import forms
from shelter_web.models import Dog
from django.utils.safestring import mark_safe

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
            "age_year": "Age (Year/Month)",
            "age_month": '',
            'weight_unit': '',
        }
        help_texts = {
            "name": "Some useful help text.",
        }
        widgets = {
            'age_year': SuffixNumberInput(suffix="year(s)"),
            "age_month": SuffixNumberInput(suffix="month(s)"),
        }
