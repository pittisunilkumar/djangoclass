from django import forms
from .models import User

class register(forms.ModelForm):  # Rename this to RegisterForm
    class Meta:
        model = User
        fields = ['name', 'section', 'password', 'lastname']  # Ensure all fields are correct



class customform(forms.Form):
    username= forms.CharField(max_length=65,widget=(forms.TextInput(
        attrs={'placeholder':'Enter email','class':'form-control'}
    )))
    password = forms.CharField(max_length=65)

