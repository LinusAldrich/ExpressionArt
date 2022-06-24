from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *

class DiaryForm(ModelForm):
    diary_description = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
        'class': 'diary_description'
    }))

    class Meta:
        model = Diary
        fields = '__all__'

class CanvasForm(forms.ModelForm):
    class Meta:
        model = Canvas
        fields = '__all__'

class CollageForm(forms.ModelForm):
    class Meta:
        model = Collage
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].strip = False
        self.fields['first_name'].strip = False
        self.fields['last_name'].strip = False
        self.fields['email'].strip = False

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
