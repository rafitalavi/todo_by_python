from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True)
    last_login = forms.DateTimeField(disabled=True, required=False, label="Last login")

    class Meta:
        model = User
        fields = [ 'email',   'last_login','date_joined' , 'is_active', 'is_staff', 'is_superuser']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role', 'phone_number']
