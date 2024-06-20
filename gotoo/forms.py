from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from gotoo.models import Profile


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']