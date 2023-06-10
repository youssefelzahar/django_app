from django import forms
from .models import login

class LoginForm(forms.ModelForm):
    #user_name=forms.CharField(max_length=50)    
    #user_pasword=forms.CharField(max_length=50,widget=forms.PasswordInput) 
    class Meta:
        model=login
        fields = '__all__'
