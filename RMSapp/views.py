from django.shortcuts import render
from django.http import HttpResponseServerError,HttpResponse
from urllib import request
from django.shortcuts import redirect
# from signup.models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import socket
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .auth_backends import CustomBackend
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
import random
from social_django.models import UserSocialAuth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html" 

class SettingsView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user

        try:
            github_login = user.social_auth.get(provider='github')
        except UserSocialAuth.DoesNotExist:
            github_login = None

        

        try:
            google_login = user.social_auth.get(provider='google')
        except UserSocialAuth.DoesNotExist:
            google_login = None

        can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

        return render(request, 'core/settings.html', {
            'github_login': github_login,
            'twitter_login': twitter_login,
            'facebook_login': facebook_login,
            'can_disconnect': can_disconnect
        })
        
        
        
def signup(request):
    user = request.user
    if request.user.is_authenticated:
        return redirect("signup")
    context = {}
    try:
        if request.method == 'POST':
            fname=request.POST.get("first_name")
            lname=request.POST.get("last_name")
            email=request.POST.get("email")
            username=request.POST.get("username")
            password1=request.POST.get("password1")
            password2=request.POST.get("password2")

            # print("Than correct!")
            if User.objects.filter(username=username).first():
                messages.error(
                    request, "This username is already taken! Please login with user id!")
                return redirect('signup')
            if User.objects.filter(email=email).first():
                messages.error(
                    request, "This email is already taken! Please login with user id")
                return redirect('signup')
            if password1 == password2:
                fname=request.POST.get("first_name")
                lname=request.POST.get("last_name")
                email=request.POST.get("email")
                username=request.POST.get("username")
                password1=request.POST.get("password1")
                password2=request.POST.get("password2")

                user = User.objects.create_user(
                    username=username, email=email, password=password1, first_name=fname, last_name=lname)
                user.save()
                
                # login(request, user)
                # messages.success(request, "Welcome {}".format(
                    # request.user.get_short_name()))
                
                return redirect("login")
            else:
                messages.warning(request, 'Password must be same!')
                return render(request, "signup.html", context)
        else:
            return render(request, "signup.html", context)
    except socket.gaierror:
        return HttpResponseServerError("Internet connection error")

 
    
def Login(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Login Successfully!!")
            return redirect("index")
        else:
            messages.warning(request,"User or password is not correct!")

    return render(request, "login.html")


def Logout(request):
    logout(request)
    return redirect('index')

# Create your views here.
def index(request):
    return render(request,"index.html")
def Profile(request,pk):
    if request.user.is_authenticated:
        user=User.objects.get(id=pk)
        context={
            'pdb':user,
        }
        return render(request,"profile.html",context)
    else:
        return redirect("login")
    
def forgotpassword(request):
    return render(request, 'forget-password.html')


class CustomLoginView(LoginView):
    template_name = 'login.html'
    # authentication_form = CustomAuthenticationForm
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True
    authentication_backend = CustomBackend()

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return self.authentication_backend.login_success_redirect(self.request, user)

@login_required
def Account_Deleted(request):
    if request.method=="POST":
        u=User.objects.get(username=request.user)
        u.delete()
        return render(request,'delete_confirm.html')
    return render(request, 'delete-account.html')
        
        


