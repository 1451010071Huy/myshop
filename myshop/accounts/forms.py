from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()


class UserForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password")
        help_texts = {
            'username': None,
        }

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        ##user = authenticate(username=username, password=password)
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Username or password is incorrect")
        return super(UserForm, self).clean(*args,**kwargs)



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

class EditProfileForm(UserChangeForm):
        template_name = '/something/else'

        class Meta:
            model = User
            fields = (
                'email',
                'first_name',
                'last_name',
                'password'
            )