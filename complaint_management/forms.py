from django import forms
from .models import User, Employee, Customer, Product, Complaint
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'designation', 'phone_number', 'salary', 'email']

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact_number', 'address', 'email', 'place']

    def clean_contact_number(self):
        phone = self.cleaned_data.get('contact_number')
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Contact number must be exactly 10 digits.")
        return phone


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'tax', 'description']


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['customer', 'product', 'complaint_level', 'description', 'location', 'assigned_employee']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'location': forms.TextInput(attrs={'placeholder': 'Latitude, Longitude or Address'}),
        }


class ComplaintUpdateForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['status', 'report']
        widgets = {
            'report': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Work report or remarks'}),
        }

class EmployeeForm(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Employee
        fields = ['name', 'designation', 'phone_number', 'salary', 'email', 'username', 'password']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact_number', 'address', 'email', 'place']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'tax', 'description']
