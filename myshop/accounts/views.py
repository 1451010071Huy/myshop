from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import View
from .forms import UserForm, RegisterForm, EditProfileForm

# Create your views here.


def logins(request):
    form = UserForm()

    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request,user)

            return redirect("/")

    return render(request,'login.html',{'login_form': form})

class UserFromView(View):
    form_class = UserForm
    template_name= "account/register.html"

    def post(self,request):
        form= self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #normalized
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

def logout_view(request):
    logout(request)

    return redirect("/")

def register_user_view(request):
    form = RegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()

            return redirect("logins")


    return render(request,"registration.html",{'register_form':form})


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)