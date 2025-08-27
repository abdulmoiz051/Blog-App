from django import forms
from .models import blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
Own_User = get_user_model()
class login_system(UserCreationForm):
    class Meta:
        model = Own_User
        fields = ['username','profile_picture','phone_number','email','password1','password2']

class blog_form(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['Image','Title','Text']

class update_delete_user(forms.ModelForm):
    class Meta:
        model=Own_User
        fields = ['profile_picture']