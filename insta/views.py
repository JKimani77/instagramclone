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
from .forms import FormSignUp,FormLogin,ProfileForm,FormImage, CommentForm


from django.conf import settings
import os


# Create your views here.
def index(request):
    imagess = Image.get_images()
    return render(request, 'home.html', {"images":imagess})

def signingup(request):
    if request.method == 'POST':
        form = FormSignUp(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_active = False
            user.save()
            current = get_current_site(request)
            '''
            subject = 'Activate your iNsTa'
            message = render_to_string('email/email.html', {
                'user': user, 
                'domain': current.domain, 
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
                })
            
            user.email_user(subject, message)
            return 'We have just sent you an email'
            '''
        else:
            form = FormSignUp()
        return render(request, 'django_registration/registration_form.html', {'form': form})


@login_required(login_url='/login')
def profile(request):
    #print(request)
    '''
    function to create user profile 
    '''
    current_user = request.user
    
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.user = current_user 
            profile.save()
            return redirect(updatedprofile)
    else:
        form = ProfileForm()
    return render(request, 'profile.html',{"form":form})


@login_required(login_url='/login')
def updatedprofile(request, username):
    
    '''
    funcion to display user profile
    '''
    current_user = request.user
    user_id = current_user.id
    #userr = get_object_or_404(User, username=username)
    profile = Profile.objects.filter(id=user_id).all()
    #images = Image.objects.filter(profile_id=current_user.profile.id).all()
    #user_posts = userr.profile.posts.all()
    #if request.user == userr:
        #return redirect('updatedprofile', username=request.user.username)
    return render(request, 'viewprofile.html', {"profile":profile})

@login_required(login_url='/login')
def uploadimage(request):
    '''
    view function to post images
    '''
    user = User.objects.exclude(id=request.user.id)
    current_user = request.user
    if request.method=='POST':
        form = FormImage(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            #image.user = request.user.profile
            image.save()
            return redirect(index)
    else:
        form = FormImage()
    return render(request, 'uploadimage.html',{"form":form})

def search(request):
    if 'user' in request.GET and request.GET['user']:
        search_user = request.GET.get('user')
        username_searched = Profile.search_by_profile(search_user)
        message = f'{search_user}'
        return render(request, 'search.html',{"users":username_searched, "message":message})

def specific(request, img_id):
    '''
    view function to show details of a single image
    '''
    image = Image.objects.get(pk=img_id) 
    # likes = image.like_set.all().count()
    comments = Comment.objects.filter(image_id=img_id).all()
    return render(request,'singleimage.html',{"image":image, "comments":comments, "likes":likes})

def comment(request, id):
    '''
    view for the render form
    '''
    current_user = request.user
    image = Image.objects.get(pk=id)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_id = current_user
            comment.image_id = image
            comment.save_comment()
            return redirect(index)
    else:
        form= CommentForm()
    return render(request, 'comment.html', {"form":form, "image":image})

def likes(request, img_id):
    current_user = request.user
    current_image = Image.objects.get(pk=img_id)
    likey= Likes.objects.create(user=current_user, image=current_image)
    
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
        form = FormLogin()
    return render(request, 'registration/login.html',{"form":form})


def logout_view(request):
    logout(request)

    return redirect(index)