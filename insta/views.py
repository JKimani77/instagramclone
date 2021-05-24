from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout 
from django.contrib.sites.shortcuts import get_current_site

from django.utils.http import urlsafe_base64_encode #encypt token to base64
from django.utils.encoding import force_bytes, force_text

from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .models import Image, Profile, Comment, Likes, Followers
from .forms import FormSignUp,FormLogin


from django.conf import settings
import os


# Create your views here.
def index(request):
    images = Image.get_images()
    return render(request, 'home.html', {"images":images})

# Create your views here.
def logout_view(request):
    logout(request)

    return redirect(index)

def login(request):
    '''
    view function to display login form
    '''
    if request.method=='POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            user = authenticate(username,password)
            if user.is_active:
                login(request,user)
                print("You have logged into your account")
                return redirect(index)
            else:
                return HttpResponse("Your account is inactive")
            
    else:
        form=FormLogin()
    return render(request, 'registration/login.html',{"form":form})

def signingup(request):
    if request.method == 'POST':
        form = FormSignUp(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_active = False
            user.save()
            current = get_current_site(request)
            subject = 'Activate your iNsTa'
            message = render_to_string('email/email.html', {
                'user': user, 
                'domain': current.domain, 
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
                })
            
            user.email_user(subject, message)
            return 'We have just sent you an email'
        else:
            form = FormSignUp()
        return render(request, 'registration/registration_form.html', {'form': form})

