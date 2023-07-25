from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Member
from django.contrib.auth.models import User, Group


class SignUPform(UserCreationForm):
    groups = forms.ModelChoiceField(queryset=Group.objects.all(), initial=2)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'groups', 'password1', 'password2']


class MemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Member
        fields = '__all__'
