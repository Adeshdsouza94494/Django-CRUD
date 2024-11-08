from django import forms

from .models import Student


class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'email', 'phone', 'branch'] 
        labels = {'firstname': "First Name", 'lastname': "Last Name",'email': "Email Id", 'phone': "Phone no" ,'branch':"Branch"}
        widgets = {
            'firstname': forms.TextInput(attrs={"class": "form-control"}),
            'lastname': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'phone': forms.NumberInput(attrs={"class": "form-control"}),
            'branch': forms.Select(attrs={"class": "form-control"}),
        }