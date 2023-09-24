# appname/forms.py
from django import forms
from .models import Student

class StudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']
