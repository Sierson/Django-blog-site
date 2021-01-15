from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import User_more_info

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email adress", required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ChangeProfileImageForm(forms.ModelForm):
    class Meta:
        model = User_more_info
        fields = ('profile_pic', )
