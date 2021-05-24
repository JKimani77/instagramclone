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
#from .forms import FormSignUp, FormLogin, ProfileForm, FormImage, CommentForm 


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
