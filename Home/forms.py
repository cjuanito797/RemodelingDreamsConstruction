from django import forms
from django.forms.models import ModelForm
from .models import Employee, requestAQuote

# form that will be rendered whenever a user is requesting a quote.
class quoteForm(forms.ModelForm):
    class Meta:
        model = requestAQuote
        fields = ('name', 'email', 'phoneNumber', 'streetAddress',
            'city', 'state', 'zipcode', 'details')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class EmployeeApplication(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['hired']