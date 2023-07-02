from django import forms
from .models import *


class ExerciseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['image'].required = False
        self.fields['steps'].required = False
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Exercise
        # fields = '__all__'
        fields = [
            'name', 'description', 'duration', 'steps', 'image',
        ]
        # widgets = {'steps': forms.HiddenInput()}

