from django import forms
from django.db.models import fields
from django.forms.models import ModelFormMetaclass
from . models import Student

class AddStudentForm(forms.ModelForm):
    class Meta :
        model = Student
        fields = ['name', 'roll_no', 'Class', 'city']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'roll_no' : forms.NumberInput(attrs={'class':'form-control'}),
            'Class' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
        }
        