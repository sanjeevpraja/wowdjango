from django import forms
from .models import *


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ExerciseForm(BaseForm):
    # name = forms.CharField(required=False)
    # description = forms.CharField(required=False, widget=forms.Textarea)
    # duration = forms.DurationField(required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Exercise
        fields = '__all__'
        # fields = [
        #     'name', 'description', 'duration', 'image',
        # ]
        # widgets = {'steps': forms.HiddenInput()}

