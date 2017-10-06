from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password")
        help_texts = {
            'username': None,
        }


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields= ("first_name","last_name","username", "password","confirm_password","email")
        help_texts ={
            'username': None,
        }

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if not confirm_password == password:
            self.add_error('confirm_password', 'Password does not match.')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()

        return user