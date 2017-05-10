from django.forms import ModelForm, Textarea
from .models import Vendor
from django.contrib.auth.models import User
from django import forms
from django.contrib import auth


"""
class LoginValidMixin(forms.Form):
    def is_valid(self):
        """

class VendorUpdateForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ['additional_info']
        widgets = {
            'additional_info' : Textarea(attrs={'cols': 80, 'rows': 5}),
        }
        
class VendorSignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password' : forms.PasswordInput(),
        }

class VendorLoginForm(forms.Form):
    # defines fields for the login form
    username = forms.CharField(max_length=User._meta.get_field('username').max_length, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    def is_valid(self):
        valid = super(VendorLoginForm, self).is_valid()
        
        # confirms valid username and password
        user = auth.authenticate(
            username=self.cleaned_data.get('username'), 
            password=self.cleaned_data.get('password')
        )
        
        # returns error message if login invalid
        if user is None:
            self._errors['no_user'] = 'username or password is incorrect'
            return False
        return True
    
    # returns authenticated user
    def get_user(self):
        return auth.authenticate(
            username=self.cleaned_data.get('username'), 
            password=self.cleaned_data.get('password')
        )