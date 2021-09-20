from django import forms
from django.core.exceptions import ValidationError
from django.forms import CharField, PasswordInput

from core.models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('fio', 'username', 'password')

    password = CharField(widget=PasswordInput())

    def clean_password(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']

        if password > 8:
            raise ValidationError('лишком мало символов ')

        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
