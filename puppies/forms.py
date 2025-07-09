from django import forms
from .models import Puppy


class PuppyForm(forms.ModelForm):
    class Meta:
        model = Puppy
        fields = [
            'age_year',
            'age_month',
            'breed',
            'gender',   
            'kci_certificate',
            'location',
            'contact',
            'purpose',
            'price',
            'image',
        ]

    def __init__(self, *args, **kwargs):
        super(PuppyForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


