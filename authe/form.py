from pyexpat import model
from django import forms

from authe.models import Department, Ticket_model, User


class Departmentform(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class Ticket_modelform(forms.ModelForm):
    class Meta:
        model = Ticket_model
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'password', 'email', 'phone', 'Department', 'role']
