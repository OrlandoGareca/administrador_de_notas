from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text=False)
    last_name = forms.CharField(max_length=30, required=False, help_text=False)
    email = forms.EmailField(max_length=254, help_text=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )
